# Generated by Django 2.1.15 on 2021-05-28 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direccion',
            name='TipoDireccion',
            field=models.IntegerField(choices=[(0, 'Domicilio'), (1, 'Laboral'), (2, 'Temporal')]),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='Genero',
            field=models.IntegerField(choices=[(0, 'Femenino'), (1, 'Masculino'), (2, 'NoDefinido')]),
        ),
    ]