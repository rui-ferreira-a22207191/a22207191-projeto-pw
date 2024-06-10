import json
from .models import Docente, Curso, LinguagemProgramacao, AreaCientifica, Disciplina, CursoDisciplina


# Carregar dados do JSON
with open('curso/curso.json') as f:
    data = json.load(f)

# Criar instâncias dos modelos com base nos dados do JSON
    for info_docente in data['docentes']:
        Docente.objects.create(nome=info_docente['nome'], apelido=info_docente['apelido'])

    for info_curso in data['cursos']:
        Curso.objects.create(
            nome=info_curso['nome'],
            apresentacao=info_curso['apresentacao'],
            objetivos=info_curso['objetivos'],
            competencias=info_curso['competencias'],
            duracao=info_curso['duracao'],
            vagas=info_curso['vagas'],
            creditos=info_curso['creditos'],
            codigo=info_curso['codigo'],
            grau=info_curso['grau'],
            localizacao=info_curso['localizacao']
        )

    for info_linguagem in data['linguagens_programacao']:
        LinguagemProgramacao.objects.create(nome=info_linguagem['nome'])

    for info_area in data['areas_cientificas']:
        AreaCientifica.objects.create(nome=info_area['nome'])

    for info_disciplina in data['disciplinas']:
        disciplina = Disciplina.objects.create(
            nome=info_disciplina['nome'],
            ano=info_disciplina['ano'],
            semestre=info_disciplina['semestre'],
            ects=info_disciplina['ects'],
            curricularIUnitReadableCode=info_disciplina['curricularIUnitReadableCode'],
            areaCientifica=AreaCientifica.objects.get(nome=info_disciplina['areaCientifica'])
        )
        disciplina.docentes.add(Docente.objects.get(nome=info_disciplina['docentes']))

    for info_curso_disciplina in data['cursos_disciplinas']:
        CursoDisciplina.objects.create(
            curso=Curso.objects.get(nome=info_curso_disciplina['curso']),
            disciplina=Disciplina.objects.get(nome=info_curso_disciplina['disciplina'])
        )
