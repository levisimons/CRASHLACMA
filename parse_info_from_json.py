import json
from pprint import pprint
import re

#json_data=open('sample_http_img.json')
json_data=open('sample_upload_img.json')

data = json.load(json_data)

# TODO: handle test cases
# testcases:
# hollywood & vine, hollywood and vine
# order of operations: hashtag, img, address, other text.
# hashtag allcaps or lowercase
# uploaded image, link to hosted image
# multiple urls? currently hard-coded to only accept the first url seen. probably best this way.

#pprint(data)

tweet = data["text"]
print tweet

if data["entities"].get('media'): # img uploaded via twitter
	###print "img uploaded"
	img_url = data["entities"]["media"][0]["media_url"]	
else: # img passed as url 
	###print "img as url"
	img_url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', tweet)[0]
		
hashtag = data["entities"]["hashtags"][0]["text"] # won't need this parsed

# this regex scrapes out URLs. that'll need to change to handle imgs as hosted links
tweet_text = ' '.join(re.sub("(@[A-Za-z0-9]+)|(#[A-Za-z0-9]+)|(\w+:\/\/\S+)"," ",tweet).split())

print(hashtag)
print(img_url)
print(tweet_text)

json_data.close()