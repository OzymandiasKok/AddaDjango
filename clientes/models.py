from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)  # Evitar duplicação de emails.
    telefone = models.CharField(max_length=15)
    empresa = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)  # A senha já vem hashada.

    def __str__(self):
        return self.nome
