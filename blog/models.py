from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=250, blank=True)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='posts/', blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.titulo

