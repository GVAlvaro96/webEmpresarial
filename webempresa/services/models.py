from django.db import models

# Create your models here.
class ServicesModel(models.Model):
    title = models.CharField(max_length=200, verbose_name = 'titulo')
    subtitle = models.CharField(max_length=200, verbose_name = 'subtitulo')
    content = models.TextField(verbose_name = 'contenido')
    image = models.ImageField(verbose_name = 'foto')
    created = models.DateTimeField(verbose_name = 'fecha de creacion', auto_now_add=True)
    updated = models.DateTimeField(verbose_name = 'ultima actualizacion', auto_now=True)

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
        ordering = ['-created']

    def __str__(self):
        return self.title