# Generated by Django 3.0.5 on 2020-05-07 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0010_charsheet_damage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charsheet',
            name='damage',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='charsheet',
            name='weapon',
            field=models.CharField(max_length=18, null=True),
        ),
    ]
