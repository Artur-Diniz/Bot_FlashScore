from datetime import datetime
from models.Partidas import Partidas

class Estatisticas():
    def __init__(self):
        
        self.Id = 0
        self.CasaOuFora=""
        self.Nome = ""
        self.NomeRival = ""
        self.TipoPartida = ""

        
        
        self.Gol = 0
        self.GolSofrido = 0
        self.Posse_de_bola = 0
        self.Total_Finalizacao = 0
        self.Chances_claras = 0
        self.Escanteios = 0
        self.Bolas_na_trave = 0
        self.Gols_de_cabeca = 0
        self.Defesas_do_goleiro = 0
        self.Impedimentos = 0
        self.Faltas = 0
        self.Cartoes_Amarelos = 0
        self.Cartoes_Vermelhos = 0
        self.Laterais_Cobrados = 0
        self.Toques_na_area_adversaria = 0
        self.Passes = 0
        self.Passes_Totais = 0
        self.Precisao_Passes = 0
        self.Passes_no_terco_final = 0
        self.Cruzamentos = 0
        self.Desarmes = 0
        self.Bolas_afastadas = 0
        self.Interceptacoes = 0
        