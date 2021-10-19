from django.contrib import admin
from core.models import Evento

# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    #Para exibir outras informações na tabela, além do título:
    list_display = ('title', 'event_date', 'creation_date')

    #Inserir um filtro: Pode haver mais de um parâmetro e deve haver uma vírgula após o último elemento
    list_filter = ('title', 'event_date')

 
admin.site.register(Evento, EventoAdmin)



