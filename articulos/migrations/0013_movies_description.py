# Generated by Django 4.0.2 on 2022-05-16 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0012_movies_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='description',
            field=models.CharField(default=None, max_length=300),
            preserve_default=False,
        ),
    ]
