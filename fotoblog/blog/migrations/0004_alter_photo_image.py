# Generated by Django 4.0.1 on 2022-01-18 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_word_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(error_messages={'unique': "L'image existe déjà dans la base de donnée"}, unique=True, upload_to='', verbose_name='image'),
        ),
    ]
