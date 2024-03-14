from django.contrib import admin
from .models import ServicesModel

# Register your models here.
class ServicesAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(ServicesModel, ServicesAdmin)