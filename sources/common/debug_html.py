from sources.config.settings import settings
from sources.scraper.client import fetch_page

def main():
    html = fetch_page(settings.SOURCE_URL)
    with open("data/debug_page.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Saved HTML to data/debug_page.html")

if __name__ == "__main__":
    main()