from django.contrib import admin

# Register your models here.
from .models import AreaCientifica1
from .models import LinguagemProgramacao1
from .models import Projeto1
from .models import Docente1
from .models import Cadeira1
from .models import Curso1


admin.site.register(AreaCientifica1)
admin.site.register(LinguagemProgramacao1)
admin.site.register(Projeto1)
admin.site.register(Docente1)
admin.site.register(Cadeira1)
admin.site.register(Curso1)
