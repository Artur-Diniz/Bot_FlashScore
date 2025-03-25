from datetime import datetime

class Partidas:
    def __init__(self):
        self.Id_Partida = 0
        self.NomeTimeCasa = ""
        self.NomeTimeFora = ""
        self.data = datetime.today()
        self.Campeonato = ""
        self.PartidaAnalise = False
        self.TipoPartida = ""

    def exibir_dados(self):
        print(f"Time Casa: {self.NomeTimeCasa}")
        print(f"Time Fora: {self.NomeTimeFora}")
        print(f"Campeonato: {self.Campeonato}")
        print(f"Data: {self.data}")
        print(f"Partida Analisada: {self.PartidaAnalise}")
        print(f"Tipo de Partida: {self.TipoPartida}")