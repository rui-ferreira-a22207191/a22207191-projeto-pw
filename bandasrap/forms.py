from django import forms    # formulários Django
from .models import *   

class ArtistaForm(forms.ModelForm):
  class Meta:
    model = Artista       
    fields = '__all__'   
    
class AlbumForm(forms.ModelForm):
  class Meta:
    model = Album       
    fields = '__all__'  
    
class MusicaForm(forms.ModelForm):
  class Meta:
    model = Musica       
    fields = '__all__'