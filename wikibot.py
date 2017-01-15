# -*- coding: utf-8 -*-
# Importing required packages
import praw
import wikipedia

# Setting up praw
reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit('all')
comments = subreddit.stream.comments()

print("wikibot started successfully")

for comment in comments:
    text = comment.body
    inputtext = comment.body
    author = comment.author

    if 'wikibot!' in text.lower():
        inputtext = inputtext.replace('wikibot!', '')
        outputtext = wikipedia.summary(inputtext)
        message = "**wikibot says: **" + outputtext
        comment.reply(message)
        print("Replied to a request about: ", inputtext)
