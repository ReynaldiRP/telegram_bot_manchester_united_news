import asyncio
from telegram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from news_fetcher import fetch_news
from database import init_db
from config import TELEGRAM_TOKEN, CHANNEL_ID, CHECK_INTERVAL_MINUTES

bot = Bot(token=TELEGRAM_TOKEN)
scheduler = AsyncIOScheduler()


async def send_news():
    try:
        articles = fetch_news()
        print(articles)
        for article in articles:
            msg = (
                f"\U0001f534 *MAN UTD NEWS*\n"
                f"━━━━━━━━━━━━━━\n"
                f'*{article["title"]}*\n\n'
                f'\U0001f4f0 Source: {article["published"]}\n'
                f'\U0001f517 [Read more]({article["url"]})'
            )
            await bot.send_message(CHANNEL_ID, msg, parse_mode="Markdown")
    except Exception as e:
        print(f"Error sending news: {e}")


async def main():
    init_db()
    scheduler = AsyncIOScheduler()
    scheduler.add_job(
        send_news, "interval", minutes=CHECK_INTERVAL_MINUTES, misfire_grace_time=30
    )
    scheduler.start()
    print("Bot is running...")
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
