# Generated by Django 3.2.3 on 2021-05-20 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/profile/%Y/%m/%d/'),
        ),
    ]
