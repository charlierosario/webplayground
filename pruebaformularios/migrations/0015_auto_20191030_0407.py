# Generated by Django 2.0.2 on 2019-10-30 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pruebaformularios', '0014_auto_20191030_0354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='dni',
            field=models.PositiveSmallIntegerField(help_text='Dni válido ej. 22222222', unique=True),
        ),
    ]
