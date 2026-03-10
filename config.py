import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
FOOTBALL_API_KEY = os.getenv("FOOTBALL_API_KEY")
MAN_UTD_TEAM_ID = os.getenv("MAN_UTD_TEAM_ID")
CHECK_INTERVAL_MINUTES = int(os.environ.get("CHECK_INTERVAL_MINUTES", "30"))

RSS_FEEDS = [
    "https://www.skysports.com/rss/12040",
    "https://www.manchestereveningnews.co.uk/all-about/manchester-united-fc/?service=rss",
    "https://www.bbc.com/sport/football/teams/manchester-united/rss.xml",
]
