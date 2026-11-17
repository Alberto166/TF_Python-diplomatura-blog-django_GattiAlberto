from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Post
from .forms import PostForm


def post_list(request):
    query = request.GET.get('q', '').strip()
    posts = Post.objects.all()

    if query:
        posts = posts.filter(
            Q(titulo__icontains=query) | Q(contenido__icontains=query)
        )

    return render(request, 'blog/post_list.html', {'posts': posts, 'query': query})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            messages.success(request, 'Publicación creada correctamente.')
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form, 'accion': 'Crear'})


@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.autor != request.user:
        messages.error(request, 'No tenés permiso para editar esta publicación.')
        return redirect('post_detail', pk=post.pk)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Publicación actualizada correctamente.')
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form, 'accion': 'Editar'})


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.autor != request.user:
        messages.error(request, 'No tenés permiso para eliminar esta publicación.')
        return redirect('post_detail', pk=post.pk)

    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Publicación eliminada correctamente.')
        return redirect('post_list')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})

