import praw
import wikipedia

reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit('all')
comments = subreddit.stream.comments()

counter = 0

print wikipedia.summary("Wikipedia")

for comment in comments:
    text = comment.body
    author = comment.author

    if 'spongebob' in text.lower():
        message = "http://imgur.com/a/nLXF3"
        comment.reply(message)
        print("Replied to a spongebob")