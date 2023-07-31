import pandas as pd
import openai

dados_aluno = pd.read_excel('adm_test.xlsm', '2019.2')
disciplinas = dados_aluno[6:53]
nome_aluno = dados_aluno.iloc[4][2]

# print(disciplinas)

# Inicializar uma lista vazia para armazenar todos os dicionários de disciplinas
lista_disciplinas = []

# Inicializar variáveis para acompanhar o semestre atual e a lista de disciplinas
semestre_atual = ""
lista_disciplinas_semestre = []

# Iterar por cada linha do DataFrame
for index, row in disciplinas.iterrows():
    # Verificar se a linha corresponde a um novo semestre
    if "Cód." in str(row[1]):
        # Se for um novo semestre, adicionar as disciplinas do semestre anterior à lista
        if semestre_atual and lista_disciplinas_semestre:
            lista_disciplinas.append({semestre_atual: lista_disciplinas_semestre})

        # Reiniciar a lista de disciplinas e atualizar o semestre atual
        lista_disciplinas_semestre = []
        semestre_atual = row[2].strip()

    # Verificar se o nome da disciplina e a carga horária não são NaN
    if isinstance(row[2], str) and not pd.isna(row[3]):
        nome_disciplina = row[2]
        carga_horaria = row[3]

        # Verificar se a carga horária é um valor numérico antes de convertê-la para um número inteiro
        if isinstance(carga_horaria, (int, float)):
            carga_horaria = int(carga_horaria)
        if type(carga_horaria) == int:
          lista_disciplinas_semestre.append({nome_disciplina: carga_horaria})

# Adicionar as disciplinas do último semestre à lista
if semestre_atual and lista_disciplinas_semestre:
    lista_disciplinas.append({semestre_atual: lista_disciplinas_semestre})

# Agora, 'lista_disciplinas' contém a lista de dicionários com as disciplinas e suas cargas horárias agrupadas por semestre
# print(lista_disciplinas[1]['Disciplinas 2º semestre'])
print(lista_disciplinas)