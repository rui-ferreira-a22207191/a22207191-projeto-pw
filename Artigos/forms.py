from django import forms    # formulários Django
from .models import *

class ArtigoForm(forms.ModelForm):
  class Meta:
    model = Artigo        # classe para a qual é o formulário
    fields = '__all__'   # inclui no form todos os campos da classe Autor.

class AutorForm(forms.ModelForm):
  class Meta:
    model = Autor        # classe para a qual é o formulário
    fields = '__all__'   # inclui no form todos os campos da classe Autor.

class ComentarioForm(forms.ModelForm):
  class Meta:
    model = Comentario        # classe para a qual é o formulário
    fields = '__all__'   # inclui no form todos os campos da classe Autor.