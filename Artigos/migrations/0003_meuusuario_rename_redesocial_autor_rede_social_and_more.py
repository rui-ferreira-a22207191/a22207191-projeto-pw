# Generated by Django 4.0.6 on 2024-04-19 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Artigos', '0002_alter_autor_redesocial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeuUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('foto_perfil', models.ImageField(blank=True, null=True, upload_to='fotos_perfil')),
                ('descricao', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='autor',
            old_name='redeSocial',
            new_name='rede_social',
        ),
        migrations.RenameField(
            model_name='comentario',
            old_name='comentario',
            new_name='texto',
        ),
        migrations.RenameField(
            model_name='comentario',
            old_name='nome',
            new_name='titulo',
        ),
        migrations.RemoveField(
            model_name='artigo',
            name='data',
        ),
        migrations.RemoveField(
            model_name='autor',
            name='fotoDePerfil',
        ),
        migrations.AddField(
            model_name='artigo',
            name='data_publicacao',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='autor',
            name='foto_de_perfil',
            field=models.ImageField(blank=True, null=True, upload_to='fotos_perfil'),
        ),
        migrations.AlterField(
            model_name='artigo',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artigos', to='Artigos.autor'),
        ),
        migrations.AlterField(
            model_name='artigo',
            name='comentario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artigos', to='Artigos.comentario'),
        ),
        migrations.AlterField(
            model_name='artigo',
            name='imagem',
            field=models.ImageField(upload_to='artigos'),
        ),
        migrations.AlterField(
            model_name='artigo',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='autor',
            name='sobre',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='avaliacao',
            field=models.IntegerField(choices=[(1, 'Mau'), (2, 'Normal'), (3, 'Bom'), (4, 'Excelente')]),
        ),
        migrations.AddField(
            model_name='comentario',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comentario', to='Artigos.meuusuario'),
        ),
    ]
