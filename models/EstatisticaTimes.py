from datetime import datetime

class EstatisticasTimes():
    def __init__(self):
        
        self.Id = 0
        self.Nome = ""
        
        
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
        
        
        self.Gol_adversaria = 0
        self.GolSofrido_adversaria = 0
        self.Posse_de_bola_adversaria = 0
        self.Total_Finalizacao_adversaria = 0
        self.Chances_claras_adversaria = 0
        self.Escanteios_adversaria = 0
        self.Bolas_na_trave_adversaria = 0
        self.Gols_de_cabeca_adversaria = 0
        self.Defesas_do_goleiro_adversaria = 0
        self.Impedimentos_adversaria = 0
        self.Faltas_adversaria = 0
        self.Cartoes_Amarelos_adversaria = 0
        self.Cartoes_Vermelhos_adversaria = 0
        self.Laterais_Cobrados_adversaria = 0
        self.Toques_na_area_adversaria_adversaria = 0
        self.Passes_adversaria = 0
        self.Passes_Totais_adversaria = 0
        self.Precisao_Passes_adversaria = 0
        self.Passes_no_terco_final_adversaria = 0
        self.Cruzamentos_adversaria = 0
        self.Desarmes_adversaria = 0
        self.Bolas_afastadas_adversaria = 0
        self.Interceptacoes_adversaria = 0
        
        
        
        self.Gol_Confronto = 0
        self.GolSofrido_Confronto = 0
        self.Posse_de_bola_Confronto = 0
        self.Total_Finalizacao_Confronto = 0
        self.Chances_claras_Confronto = 0
        self.Escanteios_Confronto = 0
        self.Bolas_na_trave_Confronto = 0
        self.Gols_de_cabeca_Confronto = 0
        self.Defesas_do_goleiro_Confronto = 0
        self.Impedimentos_Confronto = 0
        self.Faltas_Confronto = 0
        self.Cartoes_Amarelos_Confronto = 0
        self.Cartoes_Vermelhos_Confronto = 0
        self.Laterais_Cobrados_Confronto = 0
        self.Toques_na_area_adversaria_Confronto = 0
        self.Passes_Confronto = 0
        self.Passes_Totais_Confronto = 0
        self.Precisao_Passes_Confronto = 0
        self.Passes_no_terco_final_Confronto = 0
        self.Cruzamentos_Confronto = 0
        self.Desarmes_Confronto = 0
        self.Bolas_afastadas_Confronto = 0
        self.Interceptacoes_Confronto = 0
        
        
        self.Gol_HT = 0
        self.GolSofrido_HT = 0
        self.Posse_de_bola_HT = 0
        self.Total_Finalizacao_HT = 0
        self.Chances_claras_HT = 0
        self.Escanteios_HT = 0
        self.Bolas_na_trave_HT = 0
        self.Gols_de_cabeca_HT = 0
        self.Defesas_do_goleiro_HT = 0
        self.Impedimentos_HT = 0
        self.Faltas_HT = 0
        self.Cartoes_Amarelos_HT = 0
        self.Cartoes_Vermelhos_HT = 0
        self.Laterais_Cobrados_HT = 0
        self.Toques_na_area_adversaria_HT = 0
        self.Passes_HT = 0
        self.Passes_Totais_HT = 0
        self.Precisao_Passes_HT = 0
        self.Passes_no_terco_final_HT = 0
        self.Cruzamentos_HT = 0
        self.Desarmes_HT = 0
        self.Bolas_afastadas_HT = 0
        self.Interceptacoes_HT = 0
        
        
        self.Gol_adversaria_HT = 0
        self.GolSofrido_adversaria_HT = 0
        self.Posse_de_bola_adversaria_HT = 0
        self.Total_Finalizacao_adversaria_HT = 0
        self.Chances_claras_adversaria_HT = 0
        self.Escanteios_adversaria_HT = 0
        self.Bolas_na_trave_adversaria_HT = 0
        self.Gols_de_cabeca_adversaria_HT = 0
        self.Defesas_do_goleiro_adversaria_HT = 0
        self.Impedimentos_adversaria_HT = 0
        self.Faltas_adversaria_HT = 0
        self.Cartoes_Amarelos_adversaria_HT = 0
        self.Cartoes_Vermelhos_adversaria_HT = 0
        self.Laterais_Cobrados_adversaria_HT = 0
        self.Toques_na_area_adversaria_adversaria_HT = 0
        self.Passes_adversaria_HT = 0
        self.Passes_Totais_adversaria_HT = 0
        self.Precisao_Passes_adversaria_HT = 0
        self.Passes_no_terco_final_adversaria_HT = 0
        self.Cruzamentos_adversaria_HT = 0
        self.Desarmes_adversaria_HT = 0
        self.Bolas_afastadas_adversaria_HT = 0
        self.Interceptacoes_adversaria_HT = 0
        
        
        
        self.Gol_Confronto_HT = 0
        self.GolSofrido_Confronto_HT = 0
        self.Posse_de_bola_Confronto_HT = 0
        self.Total_Finalizacao_Confronto_HT = 0
        self.Chances_claras_Confronto_HT = 0
        self.Escanteios_Confronto_HT = 0
        self.Bolas_na_trave_Confronto_HT = 0
        self.Gols_de_cabeca_Confronto_HT = 0
        self.Defesas_do_goleiro_Confronto_HT = 0
        self.Impedimentos_Confronto_HT = 0
        self.Faltas_Confronto_HT = 0
        self.Cartoes_Amarelos_Confronto_HT = 0
        self.Cartoes_Vermelhos_Confronto_HT = 0
        self.Laterais_Cobrados_Confronto_HT = 0
        self.Toques_na_area_adversaria_Confronto_HT = 0
        self.Passes_Confronto_HT = 0
        self.Passes_Totais_Confronto_HT = 0
        self.Precisao_Passes_Confronto_HT = 0
        self.Passes_no_terco_final_Confronto_HT = 0
        self.Cruzamentos_Confronto_HT = 0
        self.Desarmes_Confronto_HT = 0
        self.Bolas_afastadas_Confronto_HT = 0
        self.Interceptacoes_Confronto_HT = 0
        