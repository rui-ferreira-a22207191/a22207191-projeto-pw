# Generated by Django 4.0.6 on 2024-04-16 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0013_remove_album_musicas_remove_musica_banda_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='banda',
            name='nacionalidade',
            field=models.CharField(max_length=200, null=True),
        ),
    ]