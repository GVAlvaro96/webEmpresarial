from django.db import models

# Create your models here.
class Link(models.Model):
    key = models.SlugField(verbose_name = 'Nombre clave', unique = True, max_length = 100)
    name =models.CharField(verbose_name = 'Red Social', max_length=200)
    url = models.URLField(verbose_name= 'Enlace',null = True, blank = True , max_length=200)
    created = models.DateTimeField(verbose_name = 'fecha de creacion', auto_now_add=True)
    updated = models.DateTimeField(verbose_name = 'ultima actualizacion', auto_now=True)

    class Meta:
        verbose_name = 'enlace'
        verbose_name_plural = 'enlaces'
        ordering = ['name']

    def __str__(self):
        return self.key