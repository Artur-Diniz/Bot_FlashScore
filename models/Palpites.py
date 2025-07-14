from datetime import datetime

class Palpites:
    def __init__(self):
        self.Id = 0
        self.IdPartida = 0
        self.TipoPartida = 0
        self.Num = 0
        self.Descricao = ""
        self.GreenRed = ""
        self.ODD = 0.00
        self.data = datetime.today()

   