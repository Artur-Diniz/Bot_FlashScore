
import sys
from pathlib import Path

# Adiciona o diretório pai ao Python Path
PROJECT_ROOT = Path(__file__).parent.parent  # Ajuste conforme necessário
sys.path.append(str(PROJECT_ROOT))

from DTB.temporadadb import get_temporada_id 
from DTB.Partidasdb import inserir_partida 



def inserir_estatistica(cursor, partida_id, est):
    cursor.execute("""
        INSERT INTO estatisticas (
            partida_id,
            nome,
            nome_normalizado,
            adversario,
            adversario_normalizado,
            casa_ou_fora,
            tipo_partida,

            gol,
            gol_sofrido,
            posse_de_bola,
            total_finalizacao,
            chances_claras,
            escanteios,
            bolas_na_trave,
            gols_de_cabeca,
            defesas_do_goleiro,
            impedimentos,
            faltas,
            cartoes_amarelos,
            cartoes_vermelhos,
            laterais_cobrados,
            toques_area,
            passes,
            passes_totais,
            precisao_passes,
            passes_terco_final,
            cruzamentos,
            desarmes,
            interceptacoes,

            gol_ht,
            gol_sofrido_ht,
            posse_de_bola_ht,
            total_finalizacao_ht,
            chances_claras_ht,
            escanteios_ht,
            bolas_na_trave_ht,
            gols_de_cabeca_ht,
            defesas_do_goleiro_ht,
            impedimentos_ht,
            faltas_ht,
            cartoes_amarelos_ht,
            cartoes_vermelhos_ht,
            laterais_cobrados_ht,
            toques_area_ht,
            passes_ht,
            passes_totais_ht,
            precisao_passes_ht,
            passes_terco_final_ht,
            cruzamentos_ht,
            desarmes_ht,
            interceptacoes_ht
        )
        VALUES (
            %s,%s,%s,%s,%s,%s,%s,
            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s
        )
    """, (
        partida_id,
        est.Nome,
        est.Nome,
        est.NomeRival,
        est.NomeRival,
        est.CasaOuFora.lower(),
        est.TipoPartida,

        est.Gol,
        est.GolSofrido,
        est.Posse_de_bola,
        est.Total_Finalizacao,
        est.Chances_claras,
        est.Escanteios,
        est.Bolas_na_trave,
        est.Gols_de_cabeca,
        est.Defesas_do_goleiro,
        est.Impedimentos,
        est.Faltas,
        est.Cartoes_Amarelos,
        est.Cartoes_Vermelhos,
        est.Laterais_Cobrados,
        est.Toques_na_area_adversaria,   # 🔥 ajustado
        est.Passes,
        est.Passes_Totais,
        est.Precisao_Passes,
        est.Passes_no_terco_final,       # 🔥 ajustado
        est.Cruzamentos,
        est.Desarmes,
        est.Interceptacoes,

        est.Gol_HT,
        est.GolSofrido_HT,
        est.Posse_de_bola_HT,
        est.Total_Finalizacao_HT,
        est.Chances_claras_HT,
        est.Escanteios_HT,
        est.Bolas_na_trave_HT,
        est.Gols_de_cabeca_HT,
        est.Defesas_do_goleiro_HT,
        est.Impedimentos_HT,
        est.Faltas_HT,
        est.Cartoes_Amarelos_HT,
        est.Cartoes_Vermelhos_HT,
        est.Laterais_Cobrados_HT,
        est.Toques_na_area_adversaria_HT,  # 🔥 ajustado
        est.Passes_HT,
        est.Passes_Totais_HT,
        est.Precisao_Passes_HT,
        est.Passes_no_terco_final_HT,      # 🔥 ajustado
        est.Cruzamentos_HT,
        est.Desarmes_HT,
        est.Interceptacoes_HT
    ))
    
def salvar_jogo(cursor, partida, est_casa, est_fora):

    temporada_id = get_temporada_id(
        cursor,
        partida.Campeonato,
        partida.data.year
    )

    partida_id = inserir_partida(cursor, partida, temporada_id)

    inserir_estatistica(cursor, partida_id, est_casa)
    inserir_estatistica(cursor, partida_id, est_fora)
    