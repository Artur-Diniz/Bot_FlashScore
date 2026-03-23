
import sys
from pathlib import Path

# Adiciona o diretório pai ao Python Path
PROJECT_ROOT = Path(__file__).parent.parent  # Ajuste conforme necessário
sys.path.append(str(PROJECT_ROOT))

def inserir_partida(cursor, partida, temporada_id):
    cursor.execute("""
        INSERT INTO partidas (
            temporada_id,
            nome_time_casa,
            nome_time_casa_normalizado,
            nome_time_fora,
            nome_time_fora_normalizado,
            data,
            tipo_partida,
            url_partida
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        RETURNING id;
    """, (
        temporada_id,
        partida.Nome,
        partida.Nome,  
        partida.NomeRival,
        partida.NomeRival,
        partida.data,
        partida.TipoPartida,
        partida.Url_Partida
    ))

    return cursor.fetchone()[0]

def get_partida(cursor, nomeCasa, nomeFora, data):
    query = """
        SELECT *
        FROM partidas
        WHERE nome_time_casa = %s
        AND nome_time_fora = %s
        AND data = %s
        LIMIT 1;
    """

    cursor.execute(query, (nomeCasa, nomeFora, data))

    result = cursor.fetchone()

    if not result:
        return None

    return result