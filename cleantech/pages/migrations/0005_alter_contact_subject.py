# Generated by Django 3.2.13 on 2022-08-01 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=300, null=True, verbose_name='Subject'),
        ),
    ]
