# Generated by Django 4.0.6 on 2024-03-13 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Artigos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='redeSocial',
            field=models.URLField(blank=True, null=True),
        ),
    ]
