#! /usr/bin/python3
import praw
from info import *

reddit = praw.Reddit(client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent,
        password=password,
        username=username)

subreddit = reddit.subreddit('askreddit')

foundComment=False

searchNum = 0

for submission in subreddit.rising(limit=50):
    title = submission.title
    original_time = submission.created
    print("original title is: ",title)
    for result in subreddit.search(title):
        searchNum = searchNum + 1
        if searchNum > 3:
            searchNum = 0
            break
        searchedTitle = result.title
        print("Searched Title is: ",result.title)
        time = result.created
        if time == original_time or result.score < 50:
            continue
        topComment = result.comments[0]
        if topComment.body == '[deleted]' or topComment.is_root == False:
            continue
        foundComment=True
        print("top comment is: ",topComment.body)
        break
    if foundComment ==True:
      for comments in reddit.redditor(username).comments.new(limit=10):
            print("comment is: ",comments.body)
            if comments.body == topComment.body:
                foundComment = False
                break
    if foundComment==True:
        break

if foundComment == True:
    submission.reply(topComment.body)
    print("success")

print("Posted: ",topComment.body)
print("Posted in: ",title)
