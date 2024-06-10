from django.contrib import admin

# Register your models here.
from .models import AreaCientifica
from .models import LinguagemProgramacao
from .models import Projeto
from .models import Docente
from .models import Cadeira
from .models import Curso


admin.site.register(AreaCientifica)
admin.site.register(LinguagemProgramacao)
admin.site.register(Projeto)
admin.site.register(Docente)
admin.site.register(Cadeira)
admin.site.register(Curso)