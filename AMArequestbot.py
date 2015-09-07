#!/usr/bin/python
# This script will pull AMA requests for the last month /u/metaranha, /u/flyryan

import praw
import time

USER = '<add reddit username'
PASS = '<add password>' 
r = praw.Reddit('AMA request compiler /u/metaranha')
r.login(USER, PASS)

print("creating output file")
f = open('output.txt', 'w')
r = praw.Reddit('IAMA')
print("grabbing subreddit")
subreddit = r.get_subreddit('IAMA').get_top_from_month(limit=25)
print("getting hot list")
count = 0
for post in subreddit:
    if post.link_flair_text.lower() == 'request':
        f.write(str(post))
        f.write('\n')
        print post
        count += 1
        print count
    if AttributeError:
        pass
f.close()
