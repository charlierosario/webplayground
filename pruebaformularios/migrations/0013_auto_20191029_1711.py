# Generated by Django 2.0.2 on 2019-10-29 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pruebaformularios', '0012_auto_20191029_0528'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='codigo',
            options={},
        ),
        migrations.AlterField(
            model_name='codigo',
            name='codur',
            field=models.CharField(max_length=7),
        ),
    ]
