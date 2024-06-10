from django.contrib import admin

# Register your models here.
from .models import Banda
from .models import Album
from .models import Musica


admin.site.register(Banda)
admin.site.register(Album)
admin.site.register(Musica)
