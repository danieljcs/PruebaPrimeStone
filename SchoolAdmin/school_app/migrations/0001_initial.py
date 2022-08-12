# Generated by Django 2.1.15 on 2021-05-28 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CodigoCurso', models.CharField(max_length=250)),
                ('NombreCurso', models.CharField(max_length=250)),
                ('FechaInicio', models.DateTimeField()),
                ('FechaFin', models.DateTimeField()),
                ('FechaCreacion', models.DateTimeField(auto_now_add=True)),
                ('FechaActualizacion', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Direccion', models.CharField(max_length=500)),
                ('TipoDireccion', models.IntegerField(choices=[('Domicilio', 0), ('Laboral', 1), ('Temporal', 2)])),
                ('FechaCreacion', models.DateTimeField(auto_now_add=True)),
                ('FechaActualizacion', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Entidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EstaBorrado', models.BooleanField()),
                ('FechaCreacion', models.DateTimeField(auto_now_add=True)),
                ('FechaBorrado', models.DateTimeField()),
                ('FechaActualizacion', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombres', models.CharField(max_length=300)),
                ('Apellidos', models.CharField(max_length=300)),
                ('FechaNacimento', models.DateTimeField()),
                ('Genero', models.IntegerField(choices=[('Femenino', 0), ('Masculino', 1), ('NoDefinido', 2)])),
                ('FechaCreacion', models.DateTimeField(auto_now_add=True)),
                ('FechaActualizacion', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='EstudianteCurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FechaCreacion', models.DateTimeField(auto_now_add=True)),
                ('FechaActualizacion', models.DateTimeField(auto_now=True)),
                ('Curso', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='school_app.Curso')),
                ('Estudiante', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='school_app.Estudiante')),
            ],
        ),
        migrations.AddField(
            model_name='direccion',
            name='Estudiante',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='school_app.Estudiante'),
        ),
    ]
