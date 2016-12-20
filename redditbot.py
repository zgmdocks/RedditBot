#! /usr/bin/python3
import praw
import difflib

# umm_totally_real
# redditbot

reddit = praw.Reddit(client_id='PUtf-2W1mJ2cvQ',
        client_secret='54sg78JWGZbibmaMFJ6Dq3WBUjk',
        user_agent='test script by /u/umm_totally_real',
        password='redditbot',
        username='umm_totally_real')

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
        topComment = result.comments[1]
        if topComment.body == '[deleted]':
            continue
        foundComment=True
        print("top comment is: ",topComment.body)
        break
    if foundComment ==True:
        for comments in reddit.redditor('umm_totally_real').comments.new():
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
