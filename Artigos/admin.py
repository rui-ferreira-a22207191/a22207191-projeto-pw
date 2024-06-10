from django.contrib import admin

from .models import Artigo
from .models import Comentario
from .models import Autor
from .models import MeuUsuario

# Register your models here.


admin.site.register(Artigo)
admin.site.register(Autor)
admin.site.register(Comentario)
admin.site.register(MeuUsuario)