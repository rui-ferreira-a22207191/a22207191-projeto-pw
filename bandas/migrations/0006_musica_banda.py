# Generated by Django 4.0.6 on 2024-03-29 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0005_alter_banda_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='musica',
            name='banda',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='musicas', to='bandas.banda'),
        ),
    ]
