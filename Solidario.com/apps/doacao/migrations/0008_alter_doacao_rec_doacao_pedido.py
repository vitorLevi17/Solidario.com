# Generated by Django 5.0.7 on 2024-08-26 20:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doacao', '0007_remove_doacao_rec_status_doacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doacao_rec',
            name='doacao_pedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doacao_pedido', to='doacao.doacao'),
        ),
    ]
