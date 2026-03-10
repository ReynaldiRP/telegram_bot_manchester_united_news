# Manchester United Telegram News Bot

This project is a learning exercise to build a Telegram bot that automatically fetches and shares related news and information about Manchester United.

The bot periodically checks specific RSS feeds for articles containing Manchester United keywords, ensuring no duplicate news is sent by tracking them in a local SQLite database, and automatically forwards the news to a designated Telegram channel.

## Features

- **Automated News Fetching:** Pulls the latest articles from configured RSS feeds (e.g., Sky Sports, Manchester Evening News, BBC).
- **Keyword Filtering:** Only processes articles that mention Manchester United related terms ("manchester united", "man utd", "man united", "mufc").
- **Duplicate Prevention:** Uses an SQLite database to track URLs of previously sent articles to prevent spamming the channel.
- **Scheduled Tasks:** Uses `apscheduler` to run the checking process automatically at defined intervals.

## Project Structure

- `bot.py`: The main entry point. Initializes the Telegram bot, sets up the job scheduler, and defines the message sending logic.
- `news_fetcher.py`: Contains the logic to parse RSS feeds, extract data, and filter articles based on keywords and database records.
- `database.py`: Handles the SQLite database operations (`sent_articles.db`) for keeping track of sent news URLs.
- `config.py`: Loads configuration from environment variables using `python-dotenv`.
- `.env`: Stores environment variables such as your Telegram token, channel ID, and API keys.

## Prerequisites

To run this project, you will need Python installed on your system. The required libraries can be installed via `requirements.txt` and include:

- `python-telegram-bot`
- `apscheduler`
- `feedparser`
- `python-dotenv`
- `requests`
- `httpx`

## Setup and Installation

1. Clone or navigate to the project repository.
2. (Optional but recommended) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Linux/macOS
   # For Windows use: venv\Scripts\activate
   ```
3. Install the required dependency packages using pip:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the root directory and add your specific credentials:
   ```env
   TELEGRAM_TOKEN=your_telegram_bot_token
   CHANNEL_ID=@your_target_channel_id
   FOOTBALL_API_KEY=your_api_key
   MAN_UTD_TEAM_ID=66
   CHECK_INTERVAL_MINUTES=30
   ```
5. Run the bot:
   ```bash
   python bot.py
   ```

## Learning Objectives

This repository was created specifically for learning purposes to understand:

- How to interact with the Telegram Bot API using Python.
- How to parse and extract useful data from external RSS feeds.
- Implementing asynchronous task scheduling in a Python application.
- Managing basic persistent data storage using SQLite.
