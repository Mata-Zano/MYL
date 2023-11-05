from django.shortcuts import render
def indexAdministrador (request):
    return render(request, 'administradorAppTemplates/indexAdministrador.html')

def gestionVentas(request):
    return render(request, 'administradorAppTemplates/ventas.html')
def gestionUsuarios(request):
    return render(request, 'administradorAppTemplates/usuarios.html')
def perfilAdm(request):
    return render(request, 'administradorAppTemplates/perfil.html')
# Create your views here.   