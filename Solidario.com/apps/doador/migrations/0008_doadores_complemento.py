# Generated by Django 5.0.7 on 2024-09-09 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doador', '0007_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doadores',
            name='complemento',
            field=models.CharField(default='Rua de trás', max_length=255),
        ),
    ]
