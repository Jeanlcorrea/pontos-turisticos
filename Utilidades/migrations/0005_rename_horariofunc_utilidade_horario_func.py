# Generated by Django 4.1.5 on 2023-01-04 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Utilidades', '0004_rename_idademinima_utilidade_idade_minima'),
    ]

    operations = [
        migrations.RenameField(
            model_name='utilidade',
            old_name='horariofunc',
            new_name='horario_func',
        ),
    ]
