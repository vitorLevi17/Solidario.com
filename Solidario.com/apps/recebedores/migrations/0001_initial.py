# Generated by Django 5.0.7 on 2024-08-24 22:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recebedores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nm_recebedor', models.CharField(max_length=255)),
                ('cnpj', models.CharField(max_length=14)),
                ('cep', models.CharField(default='00000000', max_length=8)),
                ('pix', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=13)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]