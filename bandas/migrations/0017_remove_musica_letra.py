# Generated by Django 4.0.6 on 2024-05-26 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0016_musica_letra'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musica',
            name='letra',
        ),
    ]
