# Generated by Django 3.1.8 on 2021-05-09 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libs', '0004_auto_20210113_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='tracker',
            field=models.IntegerField(default=''),
        ),
    ]
