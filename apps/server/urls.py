from django.urls import path

from . import views

urlpatterns = [
    # Apenas requisições GETs
    path('get/user/', view=views.getUserById, name="get-user"), # Faz a busca de um usuário no banco de dados a partir do número de telefone dele
    path('get/config/', view=views.getConfigs, name="get-config"), # Obtém as configurações do bot determinadas pelo dono [prefixo, nome-bot...]
    path('get/apikey/', view=views.getAPIKeys, name="get-apikey"), # Obtém uma chave api de algum sistema externo a partir do nome dada à chave e sua senha
    path('get/user/ban/', view=views.getUsersBaned, name="get-banlist"), # Obtém uma lista de usuários que estão banidos para executarem comandos no bot
    path('get/user/premium/', view=views.getUsersPremium, name="get-premiumlist"), # Obtém uma lista de usuários premiums do bot

    # Apenas requisições POSTs
    path('post/create-user/', view=views.createUser, name="post-create-user"), # Rota para criar um novo usuário no banco de dados
    path('post/editUserAttribute/', view=views.editUserAttributes, name="get-editUserAttribute"), # Rota para editar um atributo de um usuário a partir de seu jid
    path('post/editUserIsPremium/', view=views.editUserIsPremium, name="get-editUserIsPremium"), # Rota para editar o atributo premium de um usuário a partir de seu jid

    # Apenas requisições TESTs
    path('test-api/', view=views.testApi, name="test-api"), # Retorna que a API está no ar
    path('help/', view=views.helpAPI, name="help-API"), # Retorna que a API está no ar
]