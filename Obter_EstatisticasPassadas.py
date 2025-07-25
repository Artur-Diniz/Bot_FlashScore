from models.Partidas import Partidas
from typing import List 

from Obter_Estatisticas import Obter_Estatisticas
from API.HttpPartidas import GetPartidasPassadas
from API.HttpPalpites import analisando_Palpite
from API.ResetSimplesBanco import ResetSimplesDatabase
from resetarBanco import Reset_Banco



def analisando_Fim_do_Dia():
    partidas_analisadas = GetPartidasPassadas()

    if partidas_analisadas!= []:


        for partida in partidas_analisadas:     
            Obter_Estatisticas(partida, "Analisada")

    analisando_Palpite()

    Reset_Banco()
    ResetSimplesDatabase()
    return

#analisando_Fim_do_Dia()

        
#Obter_Estatisticas("https://www.flashscore.com.br/jogo/futebol/lnfKCiaE/#/resumo-de-jogo", "Analisada")

