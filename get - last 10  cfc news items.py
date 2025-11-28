"""
The latest 5 items from the Official CFC website
"""
from datetime import datetime
import feedparser


def fetch_cfc_entries(url: str) -> list:
    """Fetches CFC entries from a given url"""
    news_items = feedparser.parse(url)["entries"]
    return [{
        "title": entry["description"].replace("|", "-"),
        "url": entry["link"].split("#")[0],
        "published": convert_cfc_date(entry["published"]),
    } for entry in news_items]


def convert_cfc_date(input_d: str) -> str:
    """Converts CFC's standard date format to a more readable format"""
    working = datetime.strptime(input_d, "%a, %d %b %Y %H:%M:%S %z")
    friendly_date = datetime.strftime(working, "%d %b")
    return friendly_date


if __name__ == "__main__":

    URL = "[source xml]"
    entries = fetch_cfc_entries(URL)[:10]
    OUTPUT = "".join([
        f"- {entry['title']} - ({entry['published']})\n" for entry in entries
    ])

    print(OUTPUT)

