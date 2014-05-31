import json
from pprint import pprint
import re
import urllib
import time
from geopy import geocoders
import Image
import os

# TODO: handle test cases
# testcases:
# hollywood & vine, hollywood and vine
# order of operations: hashtag, img, address, other text.
# hashtag allcaps or lowercase
# uploaded image, link to hosted image
# multiple urls? currently hard-coded to only accept the first url seen. probably best this way.

class TwitterJsonParser():
	
	# parser useful fields from file of json tweet objects
	def get_data_from_tweets(self, input_data):
		
		g = geocoders.GoogleV3()
		tweet_data = []
		processed_tweets = []
		
		with open(input_data) as f:
			for line in f:
				if line.strip():
					tweet_data = json.loads(line)
					
					tweet = tweet_data["text"]
						
					# scrub out any @mentions or #hashtags to leave behind address / text
					tweet_text = ' '.join(re.sub("(@[A-Za-z0-9]+)|(#[A-Za-z0-9]+)|(\w+:\/\/\S+)"," ",tweet).split())
					
					# geocode address to lat/long
					address, (lat, lng) = g.geocode(tweet_text)
					# TODO: this is a good place to validate the address for an LA coordinate.
					# if not LA, toss in a bucket to be human-examined
					
					# img uploaded via twitter
					if tweet_data["entities"].get('media'): 
						print "DEBUG: img uploaded"
						img_url = tweet_data["entities"]["media"][0]["media_url"]	
					# if img passed as url
					else:  
						print "DEBUG: img as url"
						img_url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', tweet)[0]
	
					print("tweet: %s") % tweet
					print("tweet_text: %s, img_url: %s") % (tweet_text, img_url)
					print("address: %s, lat: %s, lng: %s") % (address, lat, lng)
					self.save_img_from_tweet(str(lat), str(lng), img_url)
					
					processed_tweets.extend([address, str(lat), str(lng), img_url])
					
		return processed_tweets
						
	# this is run on one tweet at a time
	def save_img_from_tweet(self, lat, lng, img_url):
		DIR_FINISHED_IMGS = 'data_finished_images'
		IMG_NAME = lat + '_' + lng + '_.PNG'	
		
 		if (False == os.path.isfile(DIR_FINISHED_IMGS + '/' + IMG_NAME)): 			
			# save url to disk with address as filename
			try:
				file = urllib.urlretrieve(img_url, DIR_FINISHED_IMGS + '/' + IMG_NAME)
				print("Saved: %s" % DIR_FINISHED_IMGS + '/' + IMG_NAME)
			except IOError, e:
				print 'could not retrieve %s' % IMG_NAME

 	 		try:
 	 			im = Image.open(DIR_FINISHED_IMGS + '/' + IMG_NAME)
 	 			# TODO: need to figure out what thumbnail size looks best on projector
  				im2 = im.resize((20, 20), Image.NEAREST) 
  				im2.save(DIR_FINISHED_IMGS + '/thumb_' + IMG_NAME) 
  			except IOError, e:
				print 'could not open resize and save %s' % IMG_NAME
				
			time.sleep(1.5)

			print("--------------------------------------------------------") # DEBUG

		else:
 			print("file already exists. Skipping %s") % DIR_FINISHED_IMGS + '/' + IMG_NAME
 			return
 		
		return 
	