# Generated by Django 5.0.7 on 2024-09-09 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recebedores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recebedores',
            name='complemento',
            field=models.CharField(default='Rua de trás', max_length=255),
        ),
        migrations.AlterField(
            model_name='recebedores',
            name='cnpj',
            field=models.CharField(max_length=14, unique=True),
        ),
        migrations.AlterField(
            model_name='recebedores',
            name='nm_recebedor',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='recebedores',
            name='telefone',
            field=models.CharField(max_length=13, unique=True),
        ),
    ]