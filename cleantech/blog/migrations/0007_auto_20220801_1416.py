# Generated by Django 3.2.13 on 2022-08-01 11:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20220801_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='last_update',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, editable=False, null=True, unique=True),
        ),
    ]
