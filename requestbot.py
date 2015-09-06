#!/usr/bin/python

import praw
import time

#USER = ''
#PASS = '' 
r = praw.Reddit('AMA request compiler /u/metaranha')
#r.login(USER, PASS)
r.login()

DESIRED_AMOUNT = 5
print("creating output file")
file = open('output.txt', 'a')
r = praw.Reddit('IAMA')
print("grabbing subreddit")
subreddit = r.get_subreddit('IAMA').get_hot(limit=10)
print("getting hot list")
count = 0
for post in subreddit:
    if post.link_flair_text.lower() == 'request':
        print post
        count += 1
        print count

file.close()
