# Generated by Django 4.2.7 on 2023-12-04 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_users_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='codigoPostal',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='users',
            name='edad',
            field=models.IntegerField(),
        ),
    ]
