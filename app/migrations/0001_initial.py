# Generated by Django 4.2.7 on 2023-12-04 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('apellido', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('edad', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=100)),
                ('domicilio', models.CharField(max_length=100)),
                ('codigoPostal', models.CharField(max_length=100)),
                ('contrasena', models.CharField(max_length=100)),
            ],
        ),
    ]
