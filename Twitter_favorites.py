from __future__ import unicode_literals
import tweepy
import pandas as pd

ckey='key'
c_secret='secret'
atoken='token'
atokensecret='token_secret'
auth = tweepy.OAuthHandler(ckey, c_secret)
auth.set_access_token(atoken, atokensecret)


#This allows access to the free Twitter API through Tweepy. Tweepy now will automatically sleep, and notify
#you when it is sleeping by setting the two rate limit arguments to True.
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
#This creates empty lists to add the attributes of favorited tweets to.
texts=[]
names=[]
fav_counts=[]
retw_counts=[]
followers=[]
statuses=[]
#This performs the API call to find the user's favorited tweets.
favorites= []
for page in tweepy.Cursor(api.favorites,screen_name="user").pages():
#This loop is necessary to find the attributes of the individual tweets and append them to the appropriate lists.
    count=1
    while (count <= (len(page) - 1)):
        texts.append(page[count].text)
        names.append(page[count].user.screen_name)
        fav_counts.append(page[count].favorite_count)
        retw_counts.append(page[count].retweet_count)
        followers.append(page[count].user.followers_count)
        statuses.append(page[count].user.statuses_count)
        count= count + 1
    favorites.extend(page)

#This creates a dataframe from the lists above.
df= pd.DataFrame(columns=['texts','names','fav_counts','retw_counts','followers','statuses'])
d = {'Text':texts,'Name':names, 'Favorite Count':fav_counts, 'Retweet Counts':retw_counts, 'User Followers':followers, 'User Statuses':statuses}
df=pd.DataFrame(d)