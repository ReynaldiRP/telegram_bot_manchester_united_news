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
- `config.example.py`: Stores configuration variables such as the Telegram token, channel ID, check intervals, and feed URLs.

## Prerequisites

To run this project, you will need Python installed on your system along with the following primary libraries:

- `python-telegram-bot`
- `apscheduler`
- `feedparser`

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
   pip install python-telegram-bot apscheduler feedparser
   ```
4. Rename `config.example.py` to `config.py` and Update `config.py` with your specific credentials:
   - `TELEGRAM_TOKEN`: Your Telegram Bot token obtained from BotFather.
   - `CHANNEL_ID`: The target channel ID or username (e.g., `@manchesternews04`).
   - Custom configurations like `RSS_FEEDS` or `CHECK_INTERVAL_MINUTES`.
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
