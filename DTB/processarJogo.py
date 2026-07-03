import sys
from pathlib import Path

# Adiciona o diretório pai ao Python Path
PROJECT_ROOT = Path(__file__).parent.parent  # Ajuste conforme necessário
sys.path.append(str(PROJECT_ROOT))

from DTB.connectionDtb import get_connection
from DTB.EnviarEstatisticas import salvar_jogo
from DTB.Partidasdb import get_partida 
from models.partidas import Partidas
from models.EstatisticaPartidas import Estatisticas

def ProcessarJogo(partida:Partidas,estCasa:Estatisticas,estFora:Estatisticas):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        salvar_jogo(cursor, partida, estCasa, estFora)

        conn.commit()  # 🔥 ESSENCIAL

    except Exception as e:
        conn.rollback()
        print("Erro:", e)

    finally:
        cursor.close()
        conn.close()
        
def GetPartidabyNamesAndDate(nomeCasa,nomeFora,Date):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        partida = get_partida(cursor,nomeCasa,nomeFora,Date)
        
        

        conn.commit()  # 🔥 ESSENCIAL
        
    
    except Exception as e:
        conn.rollback()
        print("Erro:", e)

    finally:
        cursor.close()
        conn.close()        
        if partida == None:
            return 0
        
        return partida
