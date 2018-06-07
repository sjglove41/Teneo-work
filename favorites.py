from __future__ import unicode_literals
import tweepy
import numpy

ckey= 'key'
c_secret='secret'
atoken='token'
atokensecret='token_secret'
auth = tweepy.OAuthHandler(ckey, c_secret)
auth.set_access_token(atoken, atokensecret)


#This allows access to the free Twitter API through Tweepy. Tweepy now will automatically sleep, and notify
#you when it is sleeping by setting the two rate limit arguments to True.
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

favorites= []
for page in tweepy.Cursor(api.favorites,screen_name="user").pages():
#This loop is necessary to find the attributes of the individual tweets.    
    count=1
    while (count <= (len(page) - 1)):
        print('Tweet Text: '+ str(page[count].text))
        print('User: ' +str(page[count].user.screen_name))
        print('Favorite Count: '+ str(page[count].favorite_count))
        print('Retweet Count: '+ str(page[count].retweet_count))
        print('User Followers Count: ' +str(page[count].user.followers_count))
        print('User statuses Count: ' +str(page[count].user.statuses_count))   
        count= count + 1
    favorites.extend(page)
    
#print(favorites)
