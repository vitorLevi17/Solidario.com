# Generated by Django 5.0.7 on 2024-09-09 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doacao', '0015_doacaorec_delete_doacao_rec'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doacaorec',
            old_name='data_recebimento',
            new_name='data_rec',
        ),
    ]
