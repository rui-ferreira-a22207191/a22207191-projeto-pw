from django.shortcuts import render
from .models import *
# Create your views here.
def index_view(request):
    context = {
      'regioes': Regiao.objects.all(),
   }
    return render(request, "praias/praias.html", context)

def praia_view(request,id_praia):
    context = {
      'praia': Praia.objects.get(id = id_praia),
   }
    return render(request, "praias/praia.html", context)