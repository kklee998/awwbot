import praw
import os

CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
CLIENT_AGENT = f'android:{CLIENT_ID}:v (by /u/HolyFireX)'
POST_LIMIT = 15
MULTI = 'awwbot'
USER = 'HolyFireX'

reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     user_agent=CLIENT_AGENT)

for submission in reddit.multireddit(USER, MULTI).hot(limit=POST_LIMIT):
    print(submission.title, submission.url)
