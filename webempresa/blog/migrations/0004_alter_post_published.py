# Generated by Django 5.0.3 on 2024-03-14 10:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_categories_alter_post_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 14, 10, 18, 31, 789191, tzinfo=datetime.timezone.utc), verbose_name='fecha de publicacion'),
        ),
    ]
