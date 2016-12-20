#! /usr/bin/python3

import praw

reddit = praw.Reddit(client_id='PUtf-2W1mJ2cvQ',
                   client_secret='54sg78JWGZbibmaMFJ6Dq3WBUjk',
                    user_agent='test script by /u/umm_totally_real',
                     password='redditbot',
                      username='umm_totally_real')

for comment in reddit.redditor('umm_totally_real').comments.new(limit=None):
    print('Comment is: ',comment.body)
    print('SCORE IS: ', comment.score)
    if comment.score <= -1:
        print('delete')
        comment.delete()

