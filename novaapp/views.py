from django.shortcuts import render

def inicio_view(request):
    return render(request, "novaapp/BytedeSabor.html")

def sobre_view(request):
    return render(request, "novaapp/SobreMim.html")

def bolo_view(request):
    return render(request, "novaapp/bolodechocolate.html")

def receitas_view(request):
    return render(request, "novaapp/receitas.html")

# Create your views here.
