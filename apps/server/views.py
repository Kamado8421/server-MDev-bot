from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from django.db.utils import IntegrityError

from .models import Usuario, Rank, APIKey
from apps.client.models import ConfigBot

def testApi(request):
    return JsonResponse({"mensagem": "A API está no Ar!!"})

def helpAPI(request):
    return render(request, 'pages/help-api.html')

@csrf_exempt
def getUserById(request):
    if request.method == 'GET':

        try:
            jid = request.GET.get('jid')

            user = Usuario.objects.get(jid=jid)

            if user == None:
                response = {"mensagem": 'usuário não existe', "usuario": None}
                return JsonResponse(response)
            
            response = {"mensagem": "usuário encontrado com sucesso!", "usuario": {
                "id": user.jid,
                "nome": user.nome,
                "xp": user.xp,
                "saldo": user.saldo,
                "level": user.level,
                "rank": {
                    "rankname": user.rank.name,
                    "bonus": user.rank.bonus
                },
                "debito": user.debito,
                "banido": user.banido,
                "isPremium": user.isPremium
            }}

            return JsonResponse(response)
        except:
            return JsonResponse({"mensagem": 'Você não passou os parâmetros necessários para a requisição', "usuario": None, "status": 500}, status=500)
    else:
        response = {"mensagem": 'Requisição POST não aceita para url. Utilize requisição GET.'}
        return JsonResponse(response)
    

@csrf_exempt
def createUser(request):
    if request.method == "POST":

        body = json.loads(request.body)

        try:
            jid = body.get('jid')
            nome = body.get('nome')
            xpInicial = body.get('xpInicial')
            saldoInicial = body.get('saldoInicial')

            menor_rank = Rank.objects.get(id=1)
            levelInicial = menor_rank.minLevel

            user = Usuario.objects.create(jid=jid, nome=nome, xp=xpInicial, saldo=saldoInicial, level=levelInicial, rank=menor_rank)
            user.save()
        
            if user == None:
                response = {"mensagem": "usuário já existe. Não pode ser criado", "usuario": False}
                return JsonResponse(response)

            response = {"mensagem": "Usuário criado com sucesso!", "usuario": {
                "id": user.jid,
                "nome": user.nome,
                "xp": user.xp,
                "saldo": user.saldo,
                "level": user.level,
                "rank": {
                    "rankname": user.rank.name,
                    "bonus": user.rank.bonus,
                    "minLevel": user.rank.minLevel
                },
                "debito": user.debito,
                "banido": user.banido,
                "isPremium": user.isPremium
            }}

            return JsonResponse(response)
        except IntegrityError as e:
            print(e)
            return JsonResponse({"mensagem": "Ocorreu um erro ao criar o usuário. Usuário com jid="+jid+" já existe.", "usuario": None})
    else:
        response = {"mensagem": 'Requisição GET não aceita para url. Utilize requisição POST.'}
        return JsonResponse(response)


@csrf_exempt
def getConfigs(request):
    if request.method == 'GET':

        try:
            identificadorNomeBot = request.GET.get('identificadorNomeBot')

            configuracao = ConfigBot.objects.get(identificadorNomeBot=identificadorNomeBot)

            if configuracao == None:
                response = {"mensagem": "Configuração não encontrada. Verifique um identificador válido no banco de dados", "config": None}
                return JsonResponse(response)

            response = {"mensagem": "Configuração encontrada com sucesso", "config": {
                    "identificadorNomeBot": configuracao.identificadorNomeBot,
                    "prefix": configuracao.prefix,
                    "nomeBot": configuracao.nomeBot,
                    "nomeDono": configuracao.nomeDono,
                    "numeroDono": configuracao.numeroDono,
                    "numeroBot": configuracao.numeroBot,
                    "nomeDinheiro": configuracao.nomeDinheiro,
                }}
            
            return JsonResponse(response)
        except ConfigBot.DoesNotExist as e:
            print(e)
            return JsonResponse({"mensagem": "identificadorNomeBot inválido. verifique um identificadorNomeBot válido no banco de dados e tente novamente", "config": None})
    else:
        response = {"mensagem": 'Requisição POST não aceita para url. Utilize requisição GET.'}
        return JsonResponse(response)
    

@csrf_exempt
def getAPIKeys(request):
    if request.method == 'GET':

        try:
            name = request.GET.get('apiname')
            password = request.GET.get('password')

            apikey = APIKey.objects.get(name=name, password=password)

            response = {"mensagem": "Chave API encontrada com sucesso!", "apikey": {
                "name": apikey.name,
                "key": apikey.key,
            }}
            
            return JsonResponse(response)
        except APIKey.DoesNotExist as e:
            print(e)
            return JsonResponse({"mensagem": "Nome ou Senha inválado(s). Verifique as informações válidas da sua api no banco de dados e tente novamamente.", "apikey": None})

        
    else:
        response = {"mensagem": 'Requisição POST não aceita para url. Utilize requisição GET.'}
        return JsonResponse(response)


@csrf_exempt
def editUserAttributes(request):
    if request.method == "POST":

        body = json.loads(request.body)

        try:

            jid = body.get('jid')
            edicao = body.get('editarAtributo')
            valor = body.get('novoValor')
            addInAttribute = body.get('adicionarNoAtributo')

            if not jid or not edicao or not valor:
                return JsonResponse({'mensagem': 'Ocorreu um erro. Você não passou os parâmetros necessários para a requisição.', 'usuario': None})
            
            usuario = Usuario.objects.get(jid=jid)

            if edicao == 'saldo':
                usuario.editarSaldo(valor, addInAttribute)

            elif edicao == 'debito':
                usuario.editarDebito(valor, addInAttribute)

            elif edicao == 'xp':
                usuario.adicionarXp(valor)

            else:
                return JsonResponse({"mensagem": f'atributo "{edicao}" do usuário {usuario.nome} não encontrado', "atributosValidos": ['saldo', 'debito', 'xp'], "usuario": None})

            response = {"mensagem": f"Atributo {edicao} do usuário {jid} - ({usuario.nome}) alterado com sucesso!", "usuario": {
                "id": usuario.jid,
                "nome": usuario.nome,
                "xp": usuario.xp,
                "saldo": usuario.saldo,
                "level": usuario.level,
                "rank": {
                    "rankname": usuario.rank.name,
                    "bonus": usuario.rank.bonus,
                    "minLevel": usuario.rank.minLevel
                },
                "debito": usuario.debito,
                "banido": usuario.banido,
                "isPremium": usuario.isPremium
            }}

            return JsonResponse(response)
        except Usuario.DoesNotExist as e:
            print(e)
            return JsonResponse({"mensagem": "Usuário não encontrado"}, status=500)
    else:
        response = {"mensagem": 'Requisição GET não aceita para url. Utilize requisição POST.'}
        return JsonResponse(response)


@csrf_exempt
def getUsersBaned(request):

    users = Usuario.objects.all()

    userBans = []
    for user in users:
        if user.banido:

            x = {
                "id": user.jid,
                "nome": user.nome,
                "rank": user.rank.name,
            }

            userBans.append(x)

    return JsonResponse({'usuariosBanidos':  userBans})


@csrf_exempt
def getUsersPremium(request):

    users = Usuario.objects.all()

    userBans = []
    for user in users:
        if user.isPremium:

            x = {
                "id": user.jid,
                "nome": user.nome,
                "rank": user.rank.name,
            }

            userBans.append(x)

    return JsonResponse({'usuariosPremiums':  userBans})


@csrf_exempt
def editUserIsPremium(request):
    if request.method == "POST":

        body = json.loads(request.body)

        try:

            jid = body.get('jid')
            promoverPremium = body.get('promoverPremium')


            if not jid or not promoverPremium:
                return JsonResponse({'mensagem': 'Ocorreu um erro. Você não passou os parâmetros necessários para a requisição.', 'usuario': None})
            
            usuario = Usuario.objects.get(jid=jid)

            usuario.editarIsPremium(promoverPremium)
            
            response = {"mensagem": f"Usuário Promovido à PREMIUM com sucesso!", "usuario": {
                "id": usuario.jid,
                "nome": usuario.nome,
                "xp": usuario.xp,
                "saldo": usuario.saldo,
                "level": usuario.level,
                "rank": {
                    "rankname": usuario.rank.name,
                    "bonus": usuario.rank.bonus,
                    "minLevel": usuario.rank.minLevel
                },
                "debito": usuario.debito,
                "banido": usuario.banido,
                "isPremium": usuario.isPremium
            }}

            return JsonResponse(response)
        except Usuario.DoesNotExist as e:
            print(e)
            return JsonResponse({"mensagem": "Usuário não encontrado"}, status=500)
    else:
        response = {"mensagem": 'Requisição GET não aceita para url. Utilize requisição POST.'}
        return JsonResponse(response)


