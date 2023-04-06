from django.http import HttpResponse
from datetime import datetime


# def natal(request):     # FUNÇÃO
#  return HttpResponse("Não é natal.")    ## funcao importada do django cria um objeto de retorno

# O QUE É UMA VIEW
#Função em python que recebe uma requisição (objeto, request http) e devolve uma resposta
# A lógica de negócio pode ficar na view, mas nem sempre é indicado

# def mentira(request):
#    return HttpResponse("Dia da mentira")

    
def natal(request):
    if datetime.now().day == 25 and datetime.now().month == 12:
        return HttpResponse("É Natal")
    else:
        return HttpResponse("Não é Natal")
    
def tiradentes(requests):
    if datetime.now().day == 21 and datetime.now().month == 4:
        return HttpResponse("É feriado de Tiradentes")
    else:
        return HttpResponse("Não é feriado de Tiradentes")