# Generated by Django 3.2.13 on 2022-08-01 10:19

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(blank=True, to='blog.Category', verbose_name='Categories'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
