from twython import Twython
import re
import difflib

TWITTER_APP_KEY = 'FE01Tcf6sDZpLG0vabqA' 
TWITTER_APP_KEY_SECRET = 'zuqcRA0XIoMU0o6swx6vzWENtWZNIAXHQtZWbfk' 
TWITTER_ACCESS_TOKEN = '31018035-FbvB97V4QDqoAcQAg49z1UYlgrssenP4L8cgzWah6'
TWITTER_ACCESS_TOKEN_SECRET = 'jPqA3vQkAvrjV2XUVIfjFBgHJWpNgvubrfsR6E9EJTuCH'

t = Twython('FE01Tcf6sDZpLG0vabqA', 'zuqcRA0XIoMU0o6swx6vzWENtWZNIAXHQtZWbfk', '31018035-FbvB97V4QDqoAcQAg49z1UYlgrssenP4L8cgzWah6', 'jPqA3vQkAvrjV2XUVIfjFBgHJWpNgvubrfsR6E9EJTuCH')

search = t.search(q='#yolo', count=100)

tweets = search['statuses']

for tweet in tweets:
  tweetString = tweet['text']
  urlString = re.findall(r'https?://\S+',tweetString)
  addressString = tweetString.split("%s" %urlString)
  print "Original tweet: %s" %tweetString, '\n', "Address location: %s" %addressString, '\n', "Image url: %s" %urlString, '\n'
