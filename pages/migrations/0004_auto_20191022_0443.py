# Generated by Django 2.0.2 on 2019-10-22 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20191022_0221'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='horacurso',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Horario'),
        ),
        migrations.AlterField(
            model_name='page',
            name='fechacurso',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha'),
        ),
    ]
