#!/usr/bin/env python
import tweepy

#Coloca dentro de las comillas tus claves...
CONSUMER_KEY = 'S9Tw7CnZCRWtjzPC0ZLzmKwwq'
CONSUMER_SECRET = '135h3fOF662hGneAMTSBVvOh4Bq9RIbF7i0hqpXPYJlGugHZg0'
ACCESS_KEY = '2815404050-huITDbiIcS6oaVJ6DyfFnlbVJEOIHnGHukseoUw'
ACCESS_SECRET = 'yp5GgjLAnaaD3srr7w8Nd0nvnt2wxCAYtUzFsHhfVOn20'

#En esta parte nos identifica para poder realizar operaciones
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

x = tweepy.API(auth)
for tweets in x.search(q='GeekyTheory',count=4, result_type='recent'):
    print(tweets.created_at)
    print(tweets.user.screen_name)
    print(tweets.text)
    print(' *'*40)
