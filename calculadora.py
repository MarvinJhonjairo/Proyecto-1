import tweepy
import time

def find_between( s, first, last ):
        try:
                start = s.index( first ) + len( first )
                end = s.index( last, start )
                return s[start:end]
        except:
                return ""

#Coloca dentro de las comillas tus claves...
CONSUMER_KEY = 'S9Tw7CnZCRWtjzPC0ZLzmKwwq'
CONSUMER_SECRET = '135h3fOF662hGneAMTSBVvOh4Bq9RIbF7i0hqpXPYJlGugHZg0'
ACCESS_KEY = '2815404050-huITDbiIcS6oaVJ6DyfFnlbVJEOIHnGHukseoUw'
ACCESS_SECRET = 'yp5GgjLAnaaD3srr7w8Nd0nvnt2wxCAYtUzFsHhfVOn20'



#En esta parte nos identifica para poder realizar operaciones
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

last_mention = api.mentions_timeline(count=1)
for last_men in last_mention:
        last = last_men

while True:
        time.sleep(60)
        mentions = api.mentions_timeline(count=1)
        for mention in mentions:
                cur = mention
        if not (cur.text==last.text and cur.user.screen_name==last.user.screen_name):
                last = cur
                res = find_between(cur.text, "[", "]")
                if not (res==""):
                        res = eval(res)
                        time.sleep(60)
                        api.update_status('@'+cur.user.screen_name+" Result: "+s
