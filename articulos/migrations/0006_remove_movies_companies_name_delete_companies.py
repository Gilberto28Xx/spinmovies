# Generated by Django 4.0.2 on 2022-05-12 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0005_companies_remove_movies_companies_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies',
            name='companies_name',
        ),
        migrations.DeleteModel(
            name='Companies',
        ),
    ]