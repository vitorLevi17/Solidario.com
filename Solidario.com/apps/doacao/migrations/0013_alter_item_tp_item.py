# Generated by Django 5.0.7 on 2024-09-06 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doacao', '0012_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='tp_item',
            field=models.CharField(choices=[('COMIDA', 'comida'), ('ROUPA', 'roupa'), ('BRINQUEDOS', 'brinquedos'), ('HIGIENE', 'higiene')], max_length=50),
        ),
    ]
