# Generated by Django 4.2.13 on 2024-06-27 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arte',
            name='precio_Arte',
            field=models.CharField(max_length=8),
        ),
    ]
