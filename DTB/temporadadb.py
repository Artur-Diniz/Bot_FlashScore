
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