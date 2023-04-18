from django.shortcuts import HttpResponse, render


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
