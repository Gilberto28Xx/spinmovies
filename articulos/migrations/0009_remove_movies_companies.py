# Generated by Django 4.0.2 on 2022-05-13 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0008_alter_movies_companies'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies',
            name='companies',
        ),
    ]
