# Generated by Django 5.0.7 on 2024-08-26 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doacao', '0006_doacao_rec_doacao_pedido'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doacao_rec',
            name='status_doacao',
        ),
        migrations.RemoveField(
            model_name='doacao_rec',
            name='urgencia',
        ),
    ]
