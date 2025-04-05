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

   