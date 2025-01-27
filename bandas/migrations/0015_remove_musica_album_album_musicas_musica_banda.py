# Generated by Django 4.0.6 on 2024-04-16 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0014_banda_nacionalidade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musica',
            name='album',
        ),
        migrations.AddField(
            model_name='album',
            name='musicas',
            field=models.ManyToManyField(related_name='albuns', to='bandas.musica'),
        ),
        migrations.AddField(
            model_name='musica',
            name='banda',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='musicas', to='bandas.banda'),
        ),
    ]
