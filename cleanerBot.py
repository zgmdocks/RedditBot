#! /usr/bin/python3

import praw
from info import *

reddit = praw.Reddit(client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent,
        password=password,
        username=username)

for comment in reddit.redditor(username).comments.new(limit=None):
    print('Comment is: ',comment.body)
    print('SCORE IS: ', comment.score)
    if comment.score <= 0:
        print('delete')
        comment.delete()

