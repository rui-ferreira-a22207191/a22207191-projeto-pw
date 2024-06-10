import json
from cursoV2.models import Docente, Curso, LinguagemProgramacao, AreaCientifica, Disciplina, CursoDisciplina

# Limpar todos os dados existentes
Docente.objects.all().delete()
Curso.objects.all().delete()
LinguagemProgramacao.objects.all().delete()
AreaCientifica.objects.all().delete()
Disciplina.objects.all().delete()
CursoDisciplina.objects.all().delete()

# Carregar dados do JSON
with open('cursoV2/curso.json') as f:
    data = json.load(f)

    # Criar instâncias dos modelos com base nos dados do JSON
    for info_docente in data['docentes']:
        nome_docente = info_docente['nome']
        apelido_docente = info_docente['apelido']
        docente, created = Docente.objects.get_or_create(nome=nome_docente, apelido=apelido_docente)
        if created:
            print(f"Novo docente criado: {docente}")

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
        nome_docente = info_disciplina['docentes']
        try:
            docente = Docente.objects.get(nome=nome_docente)
        except Docente.DoesNotExist:
            print(f"Aviso: Docente com nome '{nome_docente}' não encontrado no banco de dados.")
            continue

        disciplina = Disciplina.objects.create(
            nome=info_disciplina['nome'],
            ano=info_disciplina['ano'],
            semestre=info_disciplina['semestre'],
            ects=info_disciplina['ects'],
            curricularIUnitReadableCode=info_disciplina['curricularIUnitReadableCode'],
            areaCientifica=AreaCientifica.objects.get(nome=info_disciplina['areaCientifica'])
        )
        disciplina.docentes.add(docente)

    for info_curso_disciplina in data['cursos_disciplinas']:
        CursoDisciplina.objects.create(
            curso=Curso.objects.get(nome=info_curso_disciplina['curso']),
            disciplina=Disciplina.objects.get(nome=info_curso_disciplina['disciplina'])
        )
