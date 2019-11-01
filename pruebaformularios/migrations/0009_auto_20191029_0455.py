# Generated by Django 2.0.2 on 2019-10-29 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pruebaformularios', '0008_persona_procurador'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='codigocurso',
            field=models.CharField(blank=True, max_length=7),
        ),
        migrations.AlterField(
            model_name='persona',
            name='procurador',
            field=models.CharField(choices=[('N', 'NO'), ('S', 'SI')], max_length=1),
        ),
    ]
