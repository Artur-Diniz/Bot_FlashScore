from datetime import datetime

class OddMarket:
    def __init__(self):
        self.id = None
        self.match_id = None

        self.market_type = None
        self.market_line = None
        self.selection = None

        self.period = None   # FT | HT

        self.bet365 = None
        self.betano = None
        self.estrela_bet = None
        self.super_bet = None
        self.one_xbet = None

        self.extras = {}