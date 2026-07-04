import sys
from pathlib import Path

# Adiciona o diretório pai ao Python Path
PROJECT_ROOT = Path(__file__).parent.parent  # Ajuste conforme necessário
sys.path.append(str(PROJECT_ROOT))

from DTB.connectionDtb import get_connection
from DTB.oddDb import inserir_odds
from DTB.Partidasdb import get_partida 
from models.Partidas import Partidas
from models.EstatisticaPartidas import Estatisticas

def ProcessarOdds(all_rows):

    conn = get_connection()
    cursor = conn.cursor()

    try:
        inserir_odds(cursor, all_rows)

        conn.commit()  # ESSENCIAL

        return True

    except Exception as e:
        conn.rollback()
        print("Erro ao salvar odds:", e)

        return False

    finally:
        cursor.close()
        conn.close()