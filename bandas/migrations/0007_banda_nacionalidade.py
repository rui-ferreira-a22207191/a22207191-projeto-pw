# Generated by Django 4.0.6 on 2024-03-29 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0006_musica_banda'),
    ]

    operations = [
        migrations.AddField(
            model_name='banda',
            name='nacionalidade',
            field=models.CharField(default='none', max_length=200),
        ),
    ]
