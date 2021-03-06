# Generated by Django 2.0.2 on 2019-10-27 15:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pruebaformularios', '0003_auto_20191027_0521'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Fecha de creación'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='persona',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de edición'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='apellidos',
            field=models.CharField(max_length=60, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='direccion',
            field=models.CharField(help_text='Ej. Rosario 2000', max_length=100, verbose_name='Localidad (Ciudad y CP)'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='dni',
            field=models.IntegerField(),
        ),
    ]
