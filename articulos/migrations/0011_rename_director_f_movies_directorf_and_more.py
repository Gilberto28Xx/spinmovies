# Generated by Django 4.0.2 on 2022-05-13 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0010_genero_rename_director_id_movies_director_f_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movies',
            old_name='director_f',
            new_name='directorf',
        ),
        migrations.RenameField(
            model_name='movies',
            old_name='genero_f',
            new_name='generof',
        ),
        migrations.RenameField(
            model_name='series',
            old_name='director_f',
            new_name='directorf',
        ),
    ]