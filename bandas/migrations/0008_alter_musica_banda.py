# Generated by Django 4.0.6 on 2024-03-29 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0007_banda_nacionalidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musica',
            name='banda',
            field=models.ForeignKey(default='none', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='musicas', to='bandas.banda'),
        ),
    ]
