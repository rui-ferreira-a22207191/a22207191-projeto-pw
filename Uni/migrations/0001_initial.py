# Generated by Django 4.0.6 on 2024-06-04 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaCientifica1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cadeira1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('ano', models.IntegerField()),
                ('semestre', models.CharField(max_length=20)),
                ('ects', models.IntegerField()),
                ('tempo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Docente1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LinguagemProgramacao1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Projeto1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('autor', models.CharField(max_length=100)),
                ('video', models.URLField(blank=True, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('linguagens', models.ManyToManyField(related_name='projetos', to='Uni.linguagemprogramacao1')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('ects', models.IntegerField()),
                ('bio', models.TextField()),
                ('competencia', models.TextField()),
                ('semestres', models.IntegerField()),
                ('departamento', models.CharField(max_length=100)),
                ('secretario', models.CharField(max_length=100)),
                ('tempo', models.CharField(max_length=100)),
                ('areaCientifica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cursos', to='Uni.areacientifica1')),
                ('cadeiras', models.ManyToManyField(related_name='cursos', to='Uni.cadeira1')),
            ],
        ),
        migrations.AddField(
            model_name='cadeira1',
            name='prof',
            field=models.ManyToManyField(related_name='cadeiras', to='Uni.docente1'),
        ),
    ]
