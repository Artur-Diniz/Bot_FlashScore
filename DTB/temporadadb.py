
import sys
from pathlib import Path

# Adiciona o diretório pai ao Python Path
PROJECT_ROOT = Path(__file__).parent.parent  # Ajuste conforme necessário
sys.path.append(str(PROJECT_ROOT))



def get_temporada_id(cursor, competicao_nome, ano):
    query = """
    SELECT t.id
    FROM temporadas t
    JOIN competicoes c ON c.id = t.competicao_id
    WHERE c.nome = %s AND t.ano = %s
    LIMIT 1;
    """

    cursor.execute(query, (competicao_nome, ano))
    result = cursor.fetchone()

    if not result:
        raise Exception(f"Temporada não encontrada: {competicao_nome} {ano}")

    return result[0]


def get_competicao(cursor, nome):
    query = """
    SELECT id, nome, temporada_cruzada
    FROM public.competicoes
    WHERE nome = %s
    LIMIT 1;
    """

    cursor.execute(query, (nome,))
    result = cursor.fetchone()

    if not result:
        raise Exception(f"Competição não encontrada: {nome}")

    return {
        "id": result[0],
        "nome": result[1],
        "temporada_cruzada": result[2]
    }

def resolver_ano_temporada(data_partida, temporada_cruzada):
    ano = data_partida.year
    mes = data_partida.month

    if not temporada_cruzada:
        return ano

    # temporada europeia (ano final)
    if mes >= 7:
        return ano + 1
    else:
        return ano