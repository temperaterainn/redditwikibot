# -*- coding: utf-8 -*-
# Importing required packages
import praw
import wikipedia

# Setting up praw
reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit('all')
comments = subreddit.stream.comments()

print("Wikipedia! started successfully")

for comment in comments:
    text = comment.body
    inputtext = comment.body
    author = comment.author
    
    # Looping the script
    while True:
        # If the text 'Wikipedia!' is found
        if 'Wikipedia!' in text.lower():
            # Remove 'Wikipedia!' from the search term
            inputtext = inputtext.replace('Wikipedia!', '')
            inputtext = inputtext.replace('wikipedia!', '')
            # Run the search term through Wikipedia
            outputtext = wikipedia.summary(inputtext)
            # Add the summary with some fun text
            message = "Wikipedia says: " + outputtext
            # Reply to the search request with the summary
            comment.reply(message)
