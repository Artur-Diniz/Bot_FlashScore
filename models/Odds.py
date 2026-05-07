from datetime import datetime
from decimal import Decimal


class Odds:
    def __init__(self):
        self.id: int = 0
        self.partida_id: int = 0
        self.bookmaker: str = ""
        self.mercado: str = ""
        self.periodo: str = ""
        self.linha: str | None = None
        self.selecao: str = ""
        self.odd: Decimal = Decimal("0.00")
        self.created_at: datetime = datetime.now()

    def __repr__(self):
        return (
            f"Odds(partida_id={self.partida_id}, bookmaker='{self.bookmaker}', "
            f"mercado='{self.mercado}', periodo='{self.periodo}', "
            f"linha={self.linha}, selecao='{self.selecao}', odd={self.odd})"
        )