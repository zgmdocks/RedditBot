#! /usr/bin/python3

import praw

reddit = praw.Reddit(client_id='PUtf-2W1mJ2cvQ',
        client_secret='54sg78JWGZbibmaMFJ6Dq3WBUjk',
        user_agent='test script by /u/umm_totally_real',
        password='redditbot',
        username='umm_totally_real')

for reply in reddit.inbox.comment_replies():
    if 'wrong thread' in reply.body:
        print(reply.body)
        comment.delete()
