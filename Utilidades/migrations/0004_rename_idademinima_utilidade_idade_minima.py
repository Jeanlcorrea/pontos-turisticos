# Generated by Django 4.1.5 on 2023-01-04 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Utilidades', '0003_utilidade_descricao_utilidade_horariofunc_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='utilidade',
            old_name='idademinima',
            new_name='idade_minima',
        ),
    ]
