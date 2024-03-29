from django.db import models

# Create your models here.
class Page(models.Model):
    title =models.CharField(verbose_name = 'Titulo', max_length=200)
    content = models.TextField(verbose_name= 'contenido')
    created = models.DateTimeField(verbose_name = 'fecha de creacion', auto_now_add=True)
    updated = models.DateTimeField(verbose_name = 'ultima actualizacion', auto_now=True)

    class Meta:
        verbose_name = 'pagina'
        verbose_name_plural = 'paginas'
        ordering = ['title']

    def __str__(self):
        return self.title