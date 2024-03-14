# Generated by Django 5.0.3 on 2024-03-13 15:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(related_name='get_posts', to='blog.category', verbose_name='categorias'),
        ),
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 13, 15, 28, 57, 381430, tzinfo=datetime.timezone.utc), verbose_name='fecha de publicacion'),
        ),
    ]