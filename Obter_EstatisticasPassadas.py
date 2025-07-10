from models.Partidas import Partidas
from typing import List 

from Obter_Estatisticas import Obter_Estatisticas
from API.HttpPartidas import GetPartidasPassadas
from API.ResetSimplesBanco import ResetSimplesDatabase
from resetarBanco import Reset_Banco



def ObterEstatisticasPassadas():
    partidas_analisadas: List[Partidas] = GetPartidasPassadas()

    if partidas_analisadas!= []:
        Reset_Banco()
        ResetSimplesDatabase()

        for partida in partidas_analisadas:     
            Obter_Estatisticas(partida.Url_Partida, "Analisada")
    
    return

#ObterEstatisticasPassadas()