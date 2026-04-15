import os
import pandas as pd
import matplotlib.pyplot as plt
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

def get_hourly_trend():
    query = """
    select *
    from gold_marts.fct_gold_prices_hourly
    order by price_hour, brand
    """
    engine = get_engine()
    return pd.read_sql(text(query), engine)

def plot_latest_daily_bar_chart(df: pd.DataFrame, output_path: str):
    if df.empty:
        print("No daily data available for bar chart.")
        return

    plt.figure(figsize=(12, 6))
    plt.bar(df["brand"], df["avg_sell_price"])
    plt.xticks(rotation=45, ha="right")
    plt.title("Latest Daily Average Sell Price by Brand")
    plt.xlabel("Brand")
    plt.ylabel("Average Sell Price")
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()

def plot_hourly_trend_chart(df: pd.DataFrame, output_path: str, brand: str = None):
    if df.empty:
        print("No hourly data available for trend chart.")
        return

    working_df = df.copy()

    if brand:
        working_df = working_df[working_df["brand"] == brand]

    if working_df.empty:
        print(f"No hourly trend data available for brand: {brand}")
        return

    working_df = working_df.sort_values("price_hour")

    plt.figure(figsize=(12, 6))
    plt.plot(working_df["price_hour"], working_df["avg_sell_price"])
    plt.xticks(rotation=45, ha="right")
    title = f"Hourly Sell Price Trend - {brand}" if brand else "Hourly Sell Price Trend"
    plt.title(title)
    plt.xlabel("Hour")
    plt.ylabel("Average Sell Price")
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()

def main():
    os.makedirs("images", exist_ok=True)

    latest_daily = get_latest_daily_prices()
    hourly_trend = get_hourly_trend()

    plot_latest_daily_bar_chart(
        latest_daily,
        "images/latest_daily_avg_sell_price.png"
    )

    if not hourly_trend.empty:
        first_brand = hourly_trend["brand"].dropna().iloc[0]
        plot_hourly_trend_chart(
            hourly_trend,
            "images/hourly_trend_first_brand.png",
            brand=first_brand
        )

    print("Charts saved to images/")

if __name__ == "__main__":
    main()