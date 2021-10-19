from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Evento(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    description = models.TextField(blank=True, verbose_name='Descrição') #blak=True: pode ser em branco
    event_date = models.DateTimeField(verbose_name='Data do evento') #Sem parãmetro: Não pode ser vazio
    creation_date = models.DateTimeField(auto_now=True, verbose_name='Data de criação') #auto_now=True: Preenchimento automático
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) #on_delete=models.CASCADE: Se o usuário for excluído, todos os seus eventos também serão

    #Define o nome da tabela (pelo desenvolvedor)
    class Meta:
        db_table = 'evento'
    
    def __str__(self):
        return self.title