import pandas as pd
from sqlalchemy import text

from sources.common.db import get_engine

def get_latest_daily_prices():
    query = """
    select *
    from gold_marts.fct_gold_prices_daily
    where price_date = (
        select max(price_date)
        from gold_marts.fct_gold_prices_daily
    )
    order by brand
    """
    engine = get_engine()
    return pd.read_sql(text(query), engine)

def get_latest_hourly_prices():
    query = """
    select *
    from gold_marts.fct_gold_prices_hourly
    where price_hour = (
        select max(price_hour)
        from gold_marts.fct_gold_prices_hourly
    )
    order by brand
    """
    engine = get_engine()
    return pd.read_sql(text(query), engine)

def main():
    latest_daily = get_latest_daily_prices()
    latest_hourly = get_latest_hourly_prices()

    if latest_daily.empty:
        print("No daily data found.")
    else:
        latest_daily["price_spread"] = latest_daily["avg_sell_price"] - latest_daily["avg_buy_price"]

        print("\n=== Latest Daily Prices ===")
        print(latest_daily[["brand", "price_date", "avg_buy_price", "avg_sell_price", "price_spread"]])

    if latest_hourly.empty:
        print("No hourly data found.")
    else:
        latest_hourly["price_spread"] = latest_hourly["avg_sell_price"] - latest_hourly["avg_buy_price"]

        print("\n=== Latest Hourly Prices ===")
        print(latest_hourly[["brand", "price_hour", "avg_buy_price", "avg_sell_price", "price_spread"]])

if __name__ == "__main__":
    main()