import json
import os
import time
import requests
from PIL import Image
from StringIO import StringIO
from requests.exceptions import ConnectionError
 
def go(query, path):
	start = 1
	BASE_URL = 'https://ajax.googleapis.com/ajax/services/search/images?'\
	'v=1.0&q=' + query + '&start=%d'
	BASE_PATH = os.path.join(path, query)
 
 	if not os.path.exists(BASE_PATH):
 		os.makedirs(BASE_PATH)
    
	r = requests.get(BASE_URL % start)
	for image_info in json.loads(r.text)['responseData']['results']:
		url = image_info['unescapedUrl']
	try:
		image_r = requests.get(url)
  	except ConnectionError, e:
  		print 'could not download %s' % url
  		
  	title = image_info['titleNoFormatting'].replace('/', '').replace('\\', '')
	file = open(os.path.join(BASE_PATH, '%s.jpg') % title, 'w')
	try:
		Image.open(StringIO(image_r.content)).save(file, 'JPEG')
	except IOError, e:
		print 'could not save %s' % url
		
	finally:
		file.close()
	
	time.sleep(1.5)
    
go('LACMA', 'MapImages')
