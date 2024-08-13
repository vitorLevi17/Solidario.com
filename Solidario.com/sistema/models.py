from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class CustomUser(AbstractUser):
    is_donor = models.BooleanField(default=False)
    is_institution = models.BooleanField(default=False)

    # Adicionando related_name para evitar conflitos
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Nome único para evitar conflito
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_query_name='customuser',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # Nome único para evitar conflito
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='customuser',
    )

class Doador(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    cep = models.CharField(max_length=8)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    senha = models.CharField(max_length=255)
    def __str__(self):
        return self.nome

class Instituicao(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    cnpj = models.CharField(max_length=14)
    nome = models.CharField(max_length=255)
    cep = models.CharField(max_length=8)
    pix = models.CharField(max_length=255)
    email = models.EmailField()
    senha = models.CharField(max_length=255)
    def __str__(self):
        return self.nome

