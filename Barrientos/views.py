from django.shortcuts import render

def inicio (request):
    return render (request, "Barrientos/inicio.html")
def registro(request):
    return render(request, 'Barrientos/formregistro.html')
