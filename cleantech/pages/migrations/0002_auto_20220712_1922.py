# Generated by Django 3.2.13 on 2022-07-12 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='header_section_url',
            field=models.URLField(blank=True, null=True, verbose_name='Header Button Url'),
        ),
        migrations.AlterField(
            model_name='home',
            name='middle_section_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='home',
            name='tut1_url',
            field=models.URLField(blank=True, null=True, verbose_name='Tutorial 1 Url'),
        ),
        migrations.AlterField(
            model_name='home',
            name='tut4_description',
            field=models.TextField(blank=True, null=True, verbose_name='Tutorial 4 Description'),
        ),
    ]
