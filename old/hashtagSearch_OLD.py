from twython import Twython
import re
import difflib
import urllib
import time

# TODO: bug: if two urls are present, they are glued together as one
TWITTER_APP_KEY = 'FE01Tcf6sDZpLG0vabqA' 
TWITTER_APP_KEY_SECRET = 'zuqcRA0XIoMU0o6swx6vzWENtWZNIAXHQtZWbfk' 
TWITTER_ACCESS_TOKEN = '31018035-FbvB97V4QDqoAcQAg49z1UYlgrssenP4L8cgzWah6'
TWITTER_ACCESS_TOKEN_SECRET = 'jPqA3vQkAvrjV2XUVIfjFBgHJWpNgvubrfsR6E9EJTuCH'

BASE_PATH="MapImages"

t = Twython('FE01Tcf6sDZpLG0vabqA', 'zuqcRA0XIoMU0o6swx6vzWENtWZNIAXHQtZWbfk', '31018035-FbvB97V4QDqoAcQAg49z1UYlgrssenP4L8cgzWah6', 'jPqA3vQkAvrjV2XUVIfjFBgHJWpNgvubrfsR6E9EJTuCH')

search = t.search(q='#CRASHLACMA', count=5)

tweets = search['statuses']
count=0
for tweet in tweets:
    tweetString = tweet['text']
    urlString = re.findall(r'https?://\S+',tweetString)
    urlString = "".join(urlString)
    addressString = tweetString.replace("%s" %urlString,'')
    addressString = "".join(addressString)
    tweetString = "".join(tweetString)
    print "Original tweet: %s" %tweetString, '\n', "Address location: %s" %addressString, '\n', "Image url: %s" %urlString

    #title = re.sub('[^a-zA-Z0-9\n]', '_', addressString)
    title = str(count)
    try:
        url = urlString.encode('utf-8').decode('ascii')
        
        try:
            file = urllib.urlretrieve(url, title + '.jpg')
        except IOError, e:
            print 'could not retrieve %s' % url
    except UnicodeDecodeError:
        print "url was not a ascii-encoded unicode string"

    time.sleep(1.5)

    count = count + 1

