import json
from .models import Cadeira1, Curso1, AreaCientifica1

# Carregar dados do JSON
with open('Uni/lei.json') as f:
    data = json.load(f)

    # Dicionário para armazenar as cadeiras criadas
    cadeiras_criadas = []

    # Criar instâncias dos modelos com base nos dados do JSON
    for info_cadeiras in data["courseFlatPlan"]:
        cadeira, created = Cadeira1.objects.get_or_create(
            nome=info_cadeiras["curricularUnitName"],
            ano=info_cadeiras["curricularYear"],
            semestre=info_cadeiras["semester"],
            ects=info_cadeiras["ects"],
            tempo=info_cadeiras["hrTotalContactoInt"]
        )
        # Adicionar cadeira à lista
        cadeiras_criadas.append(cadeira)

    tempoCurso = data["hrContactoSoma"]
    info_curso = data["courseDetail"]

    # Criar ou obter a área científica
    area_cientifica, created = AreaCientifica1.objects.get_or_create(
        nome=info_curso["scientificArea"]
    )

    # Criar ou obter o curso
    curso, created = Curso1.objects.get_or_create(
        nome=info_curso["courseName"],
        ects=info_curso["courseECTS"],
        bio=info_curso["careerOportunities"],
        competencia=info_curso["competences"],
        semestres=info_curso["semesters"],
        departamento=info_curso["departement"],
        secretario=info_curso["coorCursoContacto"],
        tempo=tempoCurso,
        areaCientifica=area_cientifica
    )

    # Associar as cadeiras ao curso
    curso.cadeiras.set(cadeiras_criadas)