# Generated by Django 2.0.2 on 2019-10-28 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pruebaformularios', '0005_auto_20191028_0404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='prono',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='persona',
            name='prosi',
            field=models.IntegerField(),
        ),
    ]