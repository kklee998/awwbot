import praw
import os
from telegram.ext import Updater, CommandHandler
import logging
from random import randrange
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(format='%(asctime)s - %(name)s \
                    - %(levelname)s - %(message)s')

logger = logging.getLogger()

IS_PROD = os.environ['APP_ENV']

if IS_PROD == 'dev':
    logger.setLevel(logging.DEBUG)

if IS_PROD == 'prod':
    logger.setLevel(logging.INFO)

print("Logger loaded")

REDDIT_CLIENT_ID = os.environ['REDDIT_CLIENT_ID']
REDDIT_CLIENT_SECRET = os.environ['REDDIT_CLIENT_SECRET']
CLIENT_AGENT = f'Telegram Bot:awwbot:v0.2 (by /u/HolyFireX)'
TELEGRAM_TOKEN = os.environ['TELEGRAM_ID']

print("Env loaded")

updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
dispatcher = updater.dispatcher

print("Telegram Bot initialised")

reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID,
                     client_secret=REDDIT_CLIENT_SECRET,
                     user_agent=CLIENT_AGENT)

print("Initialised Reddit")

POST_LIMIT = 5
MULTI = 'awwbot'
USER = 'HolyFireX'
MULTI_REDDIT = reddit.multireddit(USER, MULTI)


def aww(update, context):
    '''
    Get Top 5 HOT submission from /u/HolyFireX/m/awwbot
    '''
    for submission in MULTI_REDDIT.hot(limit=POST_LIMIT):
        context.bot.send_message(
            chat_id=update.message.chat_id, text=submission.url)


def random(update, context):
    '''
    Get random submission from /u/HolyFireX/m/awwbot
    '''
    sub_reddit = randrange(0, len(MULTI_REDDIT.subreddits))
    random_submission = MULTI_REDDIT.subreddits[sub_reddit].random()
    context.bot.send_message(
        chat_id=update.message.chat_id, text=random_submission.url)


def golden(update, context):
    '''
    Get golden retriver from /r/goldenretrievers/
    '''
    golden = reddit.subreddit('goldenretrievers')
    msg = f'Have a nice golden boye!~ \n {golden.random().url}'
    context.bot.send_message(chat_id=update.message.chat_id, text=msg)


def start(update, context):
    '''
    Message returned for /start
    '''
    context.bot.send_message(
        chat_id=update.message.chat_id, text="AWwBOT ACTIVATED!!")


print("Register handlers")

start_handler = CommandHandler('start', start)
aww_handler = CommandHandler('aww', aww)
random_handler = CommandHandler('random', random)
golden_handler = CommandHandler('goldie', golden)

print("Added handlers")

dispatcher.add_handler(start_handler)
dispatcher.add_handler(aww_handler)
dispatcher.add_handler(random_handler)
dispatcher.add_handler(golden_handler)


if __name__ == "__main__":
    updater.start_polling()
    updater.idle()
