import json
import os
import time
import requests
import Image
import re
import urllib
#from PIL import Image
from StringIO import StringIO
from requests.exceptions import ConnectionError

# Scrapes Google Image Search for images containing parameter 'query'
# 'query' is currently hard-coded. TODO: Change to passed in via args
# TODO: glue this script and the hashtag script together to grab from twitter instead of google image search
  
def go(query, path):
    start = 1
    BASE_URL = 'https://ajax.googleapis.com/ajax/services/search/images?'\
               'v=1.0&q=' + query + '&start=%d'
    BASE_PATH = os.path.join(path, query)

    if not os.path.exists(BASE_PATH):
        os.makedirs(BASE_PATH)
    
    r = requests.get(BASE_URL % start)
    # TODO: implement restrictions on image size
    for image_info in json.loads(r.text)['responseData']['results']:
        url = image_info['unescapedUrl']
        print url

        title = re.sub('[^a-zA-Z0-9\n]', '_', image_info['titleNoFormatting'])

        try:
            file = urllib.urlretrieve(url, BASE_PATH+'/'+title+'.jpg')
        except IOError, e:
            print 'could not retrieve %s' % url

        time.sleep(1.5)

go('LACMA', 'MapImages')


