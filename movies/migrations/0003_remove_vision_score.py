# Generated by Django 3.2.3 on 2021-05-24 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_vision'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vision',
            name='score',
        ),
    ]
