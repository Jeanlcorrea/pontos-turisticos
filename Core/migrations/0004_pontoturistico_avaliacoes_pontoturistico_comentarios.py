# Generated by Django 4.1.5 on 2023-01-02 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comentarios', '0002_alter_comentario_data'),
        ('Avaliacoes', '0001_initial'),
        ('Core', '0003_pontoturistico_utilidades'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='Avaliacoes',
            field=models.ManyToManyField(to='Avaliacoes.avaliacao'),
        ),
        migrations.AddField(
            model_name='pontoturistico',
            name='Comentarios',
            field=models.ManyToManyField(to='Comentarios.comentario'),
        ),
    ]