# RedditBot
Bots to post on Reddit:

**CommentBot** proceeds through rising posts in askreddit and searches for old posts that are similar to the rising post but with a karma amount over a certain threshold. Using the old post, CommentBot will then submit the top comment of that post and submit it to the rising post.

**CleanerBot** iterates through the comments already posted and deletes any posts under a certain score threshold. This is important to get rid of posts that have been downvoted due to irrelevancy.

**ReplyBot** iterates through replies to all comments and searches for keywords that would indicate that commentBot posted an irrelevant submission to a thread.
