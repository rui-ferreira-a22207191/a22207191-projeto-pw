from django import forms    # formulários Django
from .models import *

class BandaForm(forms.ModelForm):
  class Meta:
    model = Banda        # classe para a qual é o formulário
    fields = '__all__'   # inclui no form todos os campos da classe Autor.

class MusicaForm(forms.ModelForm):
  class Meta:
    model = Musica        # classe para a qual é o formulário
    fields = '__all__'   # inclui no form todos os campos da classe Autor.

class AlbumForm(forms.ModelForm):
  class Meta:
    model = Album        # classe para a qual é o formulário
    fields = '__all__'   # inclui no form todos os campos da classe Autor.