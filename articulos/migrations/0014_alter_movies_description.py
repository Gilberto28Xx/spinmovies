# Generated by Django 4.0.2 on 2022-05-16 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0013_movies_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='description',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
