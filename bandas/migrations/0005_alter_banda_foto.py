# Generated by Django 4.0.6 on 2024-03-29 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0004_remove_musica_album_album_musicas_alter_album_banda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banda',
            name='foto',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
