# Generated by Django 4.0.2 on 2022-05-16 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0016_alter_movies_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies',
            name='description',
        ),
    ]
