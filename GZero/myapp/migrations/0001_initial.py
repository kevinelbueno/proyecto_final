# Generated by Django 4.2.13 on 2024-06-27 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arte',
            fields=[
                ('id_Arte', models.AutoField(db_column='idArte', primary_key=True, serialize=False)),
                ('titulo_Arte', models.CharField(max_length=100)),
                ('descripcion_Arte', models.CharField(max_length=400)),
                ('precio_Arte', models.IntegerField(max_length=8)),
                ('tecnica_Arte', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('rut_Artista', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre_Artista', models.CharField(max_length=100)),
                ('Telefono', models.CharField(max_length=45)),
                ('email', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
            ],
        ),
    ]
