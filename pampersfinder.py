from twython import Twython

APP_KEY = 'kjI2hXHYaMPqdMqDCl5piuttl' #supply the appropriate value
APP_SECRET = '5qH0Ha7wE0Q2683rAxU3OE53BGDjvFXszeDxGcmYvb6A0Feb6c'


twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

search = twitter.search(q='#pampers',   #**supply whatever query you want here**
                  count=100)

tweets = search['statuses']
f = open('pampers.txt','w', encoding="utf8")
for tweet in tweets:
    f.write(tweet['user']['name']+' from '+tweet['user']['location'] + " at "+ tweet['created_at'] +": \n" +tweet['text']+"\n //\n")
f.close()
  #print tweet['id_str'], '\n', tweet['text'], '\n\n\n'
