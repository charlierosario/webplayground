# Generated by Django 2.0.2 on 2019-10-27 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pruebaformularios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='dni',
            field=models.CharField(max_length=8),
        ),
    ]
