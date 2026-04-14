import re
from bs4 import BeautifulSoup

def sanitize_price(price_str: str) -> int:
    digits = re.sub(r"\D", "", price_str)
    return int(digits) if digits else 0

def parse_gold_prices(html: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")

    table = soup.find("table", class_="gia-vang-search-data-table")
    if not table:
        raise ValueError("Could not find gold price table in HTML")

    rows = table.find_all("tr")
    results = []

    for row in rows:
        cols = row.find_all("td")
        if len(cols) < 3:
            continue

        brand_node = cols[0].find("h2")
        brand = brand_node.get_text(strip=True) if brand_node else cols[0].get_text(strip=True)

        buy_node = cols[1].find("span", class_="fixW")
        sell_node = cols[2].find("span", class_="fixW")

        buy_text = buy_node.get_text(strip=True) if buy_node else cols[1].get_text(strip=True)
        sell_text = sell_node.get_text(strip=True) if sell_node else cols[2].get_text(strip=True)

        buy_price = sanitize_price(buy_text)
        sell_price = sanitize_price(sell_text)

        if brand:
            results.append({
                "brand": brand,
                "buy": buy_price,
                "sell": sell_price
            })

    return results