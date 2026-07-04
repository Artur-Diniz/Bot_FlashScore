from psycopg2.extras import execute_values
import json

def inserir_odds(cursor, odds):

    if not odds:
        return

    values = [
        (
            odd["match_id"],
            odd["period"],
            odd["market_type"],
            odd["market_line"],
            odd["selection"],
            odd["bet365"],
            odd["betano"],
            odd["estrela_bet"],
            odd["super_bet"],
            odd["one_xbet"],
            json.dumps(odd["extras"])
        )
        for odd in odds
    ]

    query = """
        INSERT INTO odd (
            match_id,
            period,
            market_type,
            market_line,
            selection,
            bet365,
            betano,
            estrela_bet,
            super_bet,
            one_xbet,
            extras
        )
        VALUES %s
    """

    execute_values(cursor, query, values, page_size=1000)