import feedparser
from config import RSS_FEEDS
from database import is_sent, mark_sent

KEYWORDS = ["manchester united", "man utd", "man united", "mufc"]


def fetch_news():
    new_articles = []
    for feed_url in RSS_FEEDS:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries:
            try:
                title = entry.get("title", "")
                url = entry.get("link", "")

                if not title or not url:
                    continue

                if is_sent(url):
                    continue

                if any(keyword in title.lower() for keyword in KEYWORDS):
                    new_articles.append(
                        {
                            "title": title,
                            "url": url,
                            "published": entry.get(
                                "published", "No date"
                            ),  
                            "source": feed.feed.get(
                                "title", "Unknown"
                            ),  
                        }
                    )
                    mark_sent(url)

            except Exception as e:
                print(f"Skipping entry due to error: {e}")
                continue

    return new_articles
