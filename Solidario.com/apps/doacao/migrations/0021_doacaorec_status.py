# Generated by Django 5.0.7 on 2024-09-10 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doacao', '0020_alter_doacaorec_data_rec'),
    ]

    operations = [
        migrations.AddField(
            model_name='doacaorec',
            name='status',
            field=models.CharField(default='aberto', max_length=50),
        ),
    ]
