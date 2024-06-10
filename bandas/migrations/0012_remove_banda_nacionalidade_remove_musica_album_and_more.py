# Generated by Django 4.0.6 on 2024-04-16 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0011_remove_musica_banda'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banda',
            name='nacionalidade',
        ),
        migrations.RemoveField(
            model_name='musica',
            name='album',
        ),
        migrations.AddField(
            model_name='album',
            name='musicas',
            field=models.ManyToManyField(related_name='musicas', to='bandas.musica'),
        ),
        migrations.AddField(
            model_name='musica',
            name='banda',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='musicas', to='bandas.banda'),
        ),
        migrations.AlterField(
            model_name='album',
            name='banda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='banda', to='bandas.banda'),
        ),
    ]
