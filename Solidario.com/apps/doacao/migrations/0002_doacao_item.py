# Generated by Django 5.0.7 on 2024-08-26 14:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doacao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doacao_Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='doacao.item')),
            ],
        ),
    ]
