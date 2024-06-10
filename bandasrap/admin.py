from django.contrib import admin

# Register your models here.
from .models import Artista
from .models import Album
from .models import Musica


admin.site.register(Artista)
admin.site.register(Album)
admin.site.register(Musica)
