from django.db import models
from django.forms import ModelForm
from datetime import date
from django.utils import timezone
#from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class agendamento(models.Model):

    data_agendamento = models.DateField('Data')
    horario_inicio = models.TimeField('Horario Inicio')
    horario_fim = models.TimeField('Horario Fim')
    motivo = models.CharField('Motivo', max_length=100)
    google_link = models.CharField('Google Link', max_length=500)
    criado_em = models.DateTimeField(
        'Criado em', auto_now_add=True
    )
    #objects = agendamentoManager() #sobrescreve metodo objects para que use essa funcao

    def __str__(self): #sobrescreve metodo str para que ao retornar o objeto, volte o nome dele **para pagina admin**
        return self.name


class usuario_acesso(models.Model):#modelo para acesso de escrita ou nao de usuario
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    escrita = models.BooleanField(blank=True)

class recursos(models.Model):
    tipo_CHOICES = (
        (0, 'Sala'),
        (1, 'Aparelho'),
    )
    nome=models.CharField('Nome', max_length=50)
    nome_google=models.CharField('nome_google', max_length=70)
    email_responsavel = models.EmailField (blank=True)
    tipo = models.IntegerField('tipo', choices=tipo_CHOICES)
