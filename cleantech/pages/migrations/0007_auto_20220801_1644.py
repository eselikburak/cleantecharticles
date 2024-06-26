# Generated by Django 3.2.13 on 2022-08-01 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_alter_contact_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=90, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(verbose_name='Message'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=80, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=255, verbose_name='Subject'),
        ),
    ]
