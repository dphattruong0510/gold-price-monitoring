from datetime import datetime

from sources.config.settings import settings
from sources.scraper.client import fetch_page
from sources.scraper.parser import parse_gold_prices
from sources.storage.local_writer import append_to_json
from sources.storage.mongo_writer import save_to_mongodb

def scrape_gold_prices() -> dict:
    html = fetch_page(settings.SOURCE_URL)
    entries = parse_gold_prices(html)

    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "date": datetime.now().strftime("%Y-%m-%d"),
        "entries": entries
    }

def main():
    data = scrape_gold_prices()

    append_to_json(data)
    print("Saved raw data to local JSON")

    save_to_mongodb(data)
    print("Saved raw data to MongoDB")

    print(data)

if __name__ == "__main__":
    main()