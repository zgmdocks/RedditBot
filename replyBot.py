#! /usr/bin/python3

import praw
from info import *

reddit = praw.Reddit(client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent,
        password=password,
        username=username)

for comment in reddit.redditor(username).comments.new(limit=25):
    comment.refresh()
    replies = comment.replies
    for reply in replies:
        if 'wrong thread' in reply.body:
            comment.delete()
