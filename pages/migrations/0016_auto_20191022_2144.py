# Generated by Django 2.0.2 on 2019-10-22 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_auto_20191022_2107'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['-fechacurso'], 'verbose_name': 'página', 'verbose_name_plural': 'páginas'},
        ),
        migrations.RemoveField(
            model_name='page',
            name='order',
        ),
    ]
