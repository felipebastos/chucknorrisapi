from django.shortcuts import HttpResponse, render

from django.http import JsonResponse

import json

import requests


def home(request):
    resp = ""

    for k, v in request.headers.items():
        resp += f"{k}: {v}<br>"

    context = {
        "resp": resp,
    }

    return render(request, "chucknorrisapi/index.html", context=context)


def calc(request, val1, op, val2):
    return HttpResponse(f"{val1}{op}{val2} = {val1+val2}")


def digaOi(request):
    nome = request.GET.get("nome")
    sobrenome = request.GET.get("sobrenome")

    return HttpResponse(f"Bem vinda(o) {nome} {sobrenome}")


def quote(request):
    # frases = [
    # "Uma vez uma cobra mordeu a perna de Chuck Norris. Depois de cinco dias com terríveis dores e alucinações, a cobra morreu.",
    # "A Gillette continua adicionando lâminas em seus aparelhos com a esperança de que um dia elas cortem a barba de Chuck Norris. O último aparelho, o Mach Razor 3, sequer consegue ficar mais de 0,39 segundos na mesma sala em que Chuck Norris se encontra.",
    # "Chuck Norris não agride a camada de ozônio, desde que ela fique no seu canto e não encha o saco.",
    # ]
    #
    # pos = random.randrange(0, len(frases))

    resp = requests.get("https://api.chucknorris.io/jokes/random")

    dic = json.loads(resp.text)

    frase = {"quote": dic["value"]}

    return JsonResponse(frase)
