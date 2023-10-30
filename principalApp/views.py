from django.shortcuts import render

def Index (request):
    return render(request, 'principalTemplates/index.html')
def Contacto (request):
    return render(request, 'principalTemplates/contacto.html')
def Catalogo (request):
    return render(request, 'principalTemplates/catalogo.html')
def Sobre (request):
    return render(request, 'principalTemplates/sobre.html')

# Create your views here.
