from django.db import models
from django.contrib.auth.models import AbstractUser

class Time(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    favorite_team = models.CharField(max_length=100, blank=True, null=True)
    # Outros campos personalizados podem ser adicionados aqui
    def __str__(self):
        return self.username

    


# Modelo para redefinição de senha (se necessário)
class PasswordResetRequest(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="password_resets")
    token = models.CharField(max_length=64, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Password Reset for {self.user.email}"
