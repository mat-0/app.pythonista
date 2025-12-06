# importing modules
import pathlib
import feedparser
import helper
import config
from datetime import datetime, timedelta

URL_1 = config.URL_1
URL_2 = config.URL_2
URL_3 = config.URL_3
URL_4 = config.URL_4


def time_ago(published_parsed):
            published_date = datetime(*published_parsed[:6])
            now = datetime.now()
            diff = now - published_date
            if diff.days > 0:
                return f"{diff.days} days ago"
            elif diff.seconds > 3600:
                return f"{diff.seconds // 3600} hours ago"
            elif diff.seconds > 60:
                return f"{diff.seconds // 60} minutes ago"
            else:
                return "just now"



# processing
if __name__ == "__main__":
    try:
        root = pathlib.Path(__file__).parent.parent.resolve()

        urls = [URL_1, URL_2, URL_3, URL_4]
        all_items = []

        for URL in urls:
            feed = feedparser.parse(URL)
            all_items.extend(feed["items"][:25])

        all_items.sort(key=lambda x: x["published_parsed"], reverse=True)


        for item in all_items:
            item["published"] = time_ago(item["published_parsed"])

            cutoff_date = datetime.now() - timedelta(days=30)
            all_items = [item for item in all_items if datetime(*item["published_parsed"][:6]) > cutoff_date]

        string = ""
        for item in all_items:
            string += f"- {item['title']} ([{item['published']}]({item['link']}))\n"

        print(string)
        print("News completed")

    except FileNotFoundError:
        print("File does not exist, unable to proceed")
