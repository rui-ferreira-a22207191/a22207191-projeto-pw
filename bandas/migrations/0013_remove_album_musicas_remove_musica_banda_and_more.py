# Generated by Django 4.0.6 on 2024-04-16 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0012_remove_banda_nacionalidade_remove_musica_album_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='musicas',
        ),
        migrations.RemoveField(
            model_name='musica',
            name='banda',
        ),
        migrations.AddField(
            model_name='musica',
            name='album',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='musicas', to='bandas.album'),
        ),
        migrations.AlterField(
            model_name='album',
            name='banda',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='albuns', to='bandas.banda'),
        ),
    ]
