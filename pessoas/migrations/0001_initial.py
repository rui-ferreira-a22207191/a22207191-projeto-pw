# Generated by Django 4.0.6 on 2024-03-12 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('aplido', models.CharField(max_length=200)),
                ('idade', models.IntegerField()),
            ],
        ),
    ]
