# Generated by Django 4.1.5 on 2023-01-04 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Utilidades', '0002_remove_utilidade_horario_func_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilidade',
            name='descricao',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='utilidade',
            name='horariofunc',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='utilidade',
            name='idademinima',
            field=models.IntegerField(null=True),
        ),
    ]