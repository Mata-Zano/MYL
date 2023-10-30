from django.shortcuts import render

def Ingreso (request):
    return render(request, 'loginTemplates/login.html')


def Recuperar (request):
    return render(request, 'loginTemplates/recuperar.html')


# Create your views here.
