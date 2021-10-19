AGENDA DIO

1º cria venv:
python -m venv venv

2º Cria projeto:
django-admin startproject agenda_dio

3º Cria app:
django-admin startapp core

Acrescentar core ao settings, em INSTALLED_APPS 

4º Verificar se funciona:
python manage.py runserver

5º Migrassão das tabelas padrão:
python manage.py migrate

6º Criando siper usuário
python manage.py createsuperuser --usermane admin

#Criando tabelas com models
Migração dos dados
- Para migração dos dados no Django, é necessário que haja classes criadas.
- Com as classes criadas, para a migração é utilizado o comando migrate.
- Também pode-se utilizar o comando migrations para criação de arquivo de migração,
sem a necessidade de migrar "às cegas".
- Também pode-se utilizar o comando sqlmigrate, que ao invés de aplicar a migração,
é gerado todo comando para que essa migração possa ser efetuada manualmente no banco de dados.

MODELS
1 - Criação da tabela Evento
#Ao final da classe:
Define o nome da tabela (pelo desenvolvedor):
    class Meta:
        db_table = 'evento'

2 - Migração
python manage.py makemigrations core

python manage.py sqlmigrate core 0001

Se quiser modificar o nome da tabela no db, basta apagar o arquivo 0001_initial.py dentro do app e dar novamente o comando:
python manage.py sqlmigrate core 0001

3 - Para concluir a migração:
python manage.py migrate core 100

4 - Registrar a classe em admin.py:

from core.models import Evento

admin.site.register(Evento)

A tabela estará acessível pela tela de administração

########################################################
Para especificar o nome do objeto na tela de admin:
Na tabela:
def __str__(self):
    return self.title


########################################################

Em admin.py criar a classe:
class EventoAdmin(admin.ModelAdmin):
    #Para exibir outras informações na tabela, além do título:
    display_info = ('title', 'event_date', 'creation_date')
    #Inserir um filtro
    list_filter = ('title',) Pode haver mais de um parâmetro


