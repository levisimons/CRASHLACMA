import json
from pprint import pprint
import re
import urllib
import time

# TODO: handle test cases
# testcases:
# hollywood & vine, hollywood and vine
# order of operations: hashtag, img, address, other text.
# hashtag allcaps or lowercase
# uploaded image, link to hosted image
# multiple urls? currently hard-coded to only accept the first url seen. probably best this way.

DIR_RAW_TWEET_DATA='data_raw_tweets'
DIR_FINISHED_IMGS='data_finished_images'

json_data=open(DIR_RAW_TWEET_DATA + '/sample_http_img.json')
###json_data=open(DIR_RAW_TWEET_DATA + '/sample_upload_img.json')

data = json.load(json_data)
#pprint(data)

tweet = data["text"]
hashtag = data["entities"]["hashtags"][0]["text"] # won't need this 
tweet_text = ' '.join(re.sub("(@[A-Za-z0-9]+)|(#[A-Za-z0-9]+)|(\w+:\/\/\S+)"," ",tweet).split())

# img uploaded via twitter
if data["entities"].get('media'): 
	###print "DEBUG: img uploaded"
	img_url = data["entities"]["media"][0]["media_url"]	
# if img passed as url
else:  
	###print "DEBUG: img as url"
	img_url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', tweet)[0]

# TODO: check first to make sure filename does not already exist

# clean address to be usable as a filename
title = re.sub('[^a-zA-Z0-9\n]', '_', tweet_text) + '.jpg'

# save url to disk with address as filename
try:
	file = urllib.urlretrieve(img_url, DIR_FINISHED_IMGS + '/' + title)
	print("Saved: %s" % title)
except IOError, e:
	print 'could not retrieve %s' % url

time.sleep(1.5)
	
print(tweet)
print(hashtag)
print(img_url)
print(tweet_text)

json_data.close()