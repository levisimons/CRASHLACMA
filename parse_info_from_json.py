import json
from pprint import pprint
import re

json_data=open('crashlacma.20140524-102001.json')

data = json.load(json_data)

# TODO: handle test cases
# testcases:
# hollywood & vine, hollywood and vine
# order of operations: hashtag, img, address, other text.
# hashtag allcaps or lowercase
# uploaded image, link to hosted image

# if image is uploaded via twitter
img_url = data["entities"]["media"][0]["media_url"]
hashtag = data["entities"]["hashtags"][0]["text"]    # won't need this parsed
tweet = data["text"]
# this regex scrapes out URLs. that'll need to change to handle imgs as hosted links
tweet_text = ' '.join(re.sub("(@[A-Za-z0-9]+)|(#[A-Za-z0-9]+)|(\w+:\/\/\S+)"," ",tweet).split())

print(hashtag)
print(img_url)
print(tweet)
print(tweet_text)


json_data.close()