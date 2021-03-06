# Generated by Django 2.0.2 on 2019-10-22 21:07

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_auto_20191022_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='arancelcurso',
            field=models.DecimalField(decimal_places=2, help_text='Solo 2 decimales si corresponde y usar la coma no el punto', max_digits=6, verbose_name='Arancel $'),
        ),
        migrations.AlterField(
            model_name='page',
            name='disertantescurso',
            field=ckeditor.fields.RichTextField(verbose_name='Disertantes'),
        ),
        migrations.AlterField(
            model_name='page',
            name='fechacurso',
            field=models.DateField(verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='page',
            name='horacurso',
            field=models.CharField(max_length=200, verbose_name='Horario'),
        ),
        migrations.AlterField(
            model_name='page',
            name='localizacioncurso',
            field=models.CharField(help_text='Cómo obtener las coordenadas de un lugar <br> 1. ir a www.latlong.net <br> 2. Introducir la direccion: ej. Rioja 2045, Rosario, Santa Fe<br>3.Dar al boton Find <br> 4. Aparecera una marca azul en el mapa si ve que no esta exactamente haga doble click en la localizacion exacta<br>5. Listo copie la latitud y longitud tal cual.<br><br>En el campo de localizacion debe introducir de esta forma esos datos incluidos las llaves:<br>{lat: -32.952917, lng: -60.655833}', max_length=400, verbose_name='Localizacion (Coordenadas)'),
        ),
        migrations.AlterField(
            model_name='page',
            name='temariocurso',
            field=ckeditor.fields.RichTextField(verbose_name='Temario'),
        ),
    ]
