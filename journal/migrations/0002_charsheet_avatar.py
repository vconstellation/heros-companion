# Generated by Django 3.0.5 on 2020-05-03 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='charsheet',
            name='avatar',
            field=models.ImageField(default='def_avatar.jpg', upload_to='avatars'),
        ),
    ]
