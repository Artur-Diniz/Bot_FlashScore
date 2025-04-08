from pydantic import BaseModel
from datetime import datetime
from models.Partidas import Partidas
from models.EstatisticaPartidas import Estatisticas

class PartidaCompletaDto():
    estatistica_casa: Estatisticas
    estatistica_fora: Estatisticas
    partida: Partidas