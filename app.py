import praw
import os
from telegram.ext import Updater, CommandHandler
import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
CLIENT_AGENT = f'android:{CLIENT_ID}:v (by /u/HolyFireX)'
TELEGRAM_TOKEN = os.environ['TELEGRAM_ID']
POST_LIMIT = 5
MULTI = 'awwbot'
USER = 'HolyFireX'


updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
dispatcher = updater.dispatcher

reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     user_agent=CLIENT_AGENT)


def aww(update, context):
    for submission in reddit.multireddit(USER, MULTI).hot(limit=POST_LIMIT):
        context.bot.send_message(
            chat_id=update.message.chat_id, text=submission.url)


def start(update, context):
    context.bot.send_message(
        chat_id=update.message.chat_id, text="AWwBOT ACTIVATED!!")


start_handler = CommandHandler('start', start)
aww_handler = CommandHandler('aww', aww)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(aww_handler)

updater.start_polling()
