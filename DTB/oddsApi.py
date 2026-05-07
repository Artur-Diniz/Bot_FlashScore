import sys
from pathlib import Path
from decimal import Decimal

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.append(str(PROJECT_ROOT))

from models.Odds import Odds


# ──────────────────────────────────────────────
# INSERT
# ──────────────────────────────────────────────

def insert_odd(cursor, odd: Odds) -> int:
    """Insere uma odd e retorna o id gerado."""
    query = """
    INSERT INTO public.odds
        (partida_id, bookmaker, mercado, periodo, linha, selecao, odd)
    VALUES
        (%s, %s, %s, %s, %s, %s, %s)
    RETURNING id;
    """
    cursor.execute(query, (
        odd.partida_id,
        odd.bookmaker,
        odd.mercado,
        odd.periodo,
        odd.linha,
        odd.selecao,
        odd.odd,
    ))
    result = cursor.fetchone()
    return result[0]


def insert_odds_batch(cursor, odds: list[Odds]) -> int:
    """Insere uma lista de odds de uma vez. Retorna a quantidade inserida."""
    if not odds:
        return 0

    query = """
    INSERT INTO public.odds
        (partida_id, bookmaker, mercado, periodo, linha, selecao, odd)
    VALUES
        (%s, %s, %s, %s, %s, %s, %s);
    """
    valores = [
        (o.partida_id, o.bookmaker, o.mercado, o.periodo, o.linha, o.selecao, o.odd)
        for o in odds
    ]
    cursor.executemany(query, valores)
    return len(valores)


# ──────────────────────────────────────────────
# SELECT
# ──────────────────────────────────────────────

def get_odds_by_partida(cursor, partida_id: int) -> list[Odds]:
    """Retorna todas as odds de uma partida."""
    query = """
    SELECT id, partida_id, bookmaker, mercado, periodo, linha, selecao, odd, created_at
    FROM public.odds
    WHERE partida_id = %s
    ORDER BY bookmaker, mercado, periodo, selecao;
    """
    cursor.execute(query, (partida_id,))
    return _rows_to_odds(cursor.fetchall())


def get_odds_by_mercado(cursor, partida_id: int, mercado: str) -> list[Odds]:
    """Retorna as odds de uma partida filtradas por mercado (ex: '1x2', 'over_under')."""
    query = """
    SELECT id, partida_id, bookmaker, mercado, periodo, linha, selecao, odd, created_at
    FROM public.odds
    WHERE partida_id = %s AND mercado = %s
    ORDER BY bookmaker, periodo, selecao;
    """
    cursor.execute(query, (partida_id, mercado))
    return _rows_to_odds(cursor.fetchall())


def get_odds_by_bookmaker(cursor, partida_id: int, bookmaker: str) -> list[Odds]:
    """Retorna as odds de uma partida filtradas por bookmaker."""
    query = """
    SELECT id, partida_id, bookmaker, mercado, periodo, linha, selecao, odd, created_at
    FROM public.odds
    WHERE partida_id = %s AND bookmaker = %s
    ORDER BY mercado, periodo, selecao;
    """
    cursor.execute(query, (partida_id, bookmaker))
    return _rows_to_odds(cursor.fetchall())


# ──────────────────────────────────────────────
# VALIDAÇÃO / CHECAGEM
# ──────────────────────────────────────────────

def odd_exists(cursor, partida_id: int, bookmaker: str, mercado: str,
               periodo: str, selecao: str, linha: str | None = None) -> bool:
    """Checa se uma odd já existe para evitar duplicatas."""
    if linha is not None:
        query = """
        SELECT 1 FROM public.odds
        WHERE partida_id = %s AND bookmaker = %s AND mercado = %s
          AND periodo = %s AND selecao = %s AND linha = %s
        LIMIT 1;
        """
        cursor.execute(query, (partida_id, bookmaker, mercado, periodo, selecao, linha))
    else:
        query = """
        SELECT 1 FROM public.odds
        WHERE partida_id = %s AND bookmaker = %s AND mercado = %s
          AND periodo = %s AND selecao = %s AND linha IS NULL
        LIMIT 1;
        """
        cursor.execute(query, (partida_id, bookmaker, mercado, periodo, selecao))

    return cursor.fetchone() is not None


# ──────────────────────────────────────────────
# DELETE
# ──────────────────────────────────────────────

def delete_odds_by_partida(cursor, partida_id: int) -> int:
    """Remove todas as odds de uma partida. Retorna a quantidade deletada."""
    query = "DELETE FROM public.odds WHERE partida_id = %s;"
    cursor.execute(query, (partida_id,))
    return cursor.rowcount


# ──────────────────────────────────────────────
# HELPER INTERNO
# ──────────────────────────────────────────────

def _rows_to_odds(rows) -> list[Odds]:
    resultado = []
    for row in rows:
        o = Odds()
        o.id         = row[0]
        o.partida_id = row[1]
        o.bookmaker  = row[2]
        o.mercado    = row[3]
        o.periodo    = row[4]
        o.linha      = row[5]
        o.selecao    = row[6]
        o.odd        = Decimal(str(row[7]))
        o.created_at = row[8]
        resultado.append(o)
    return resultado