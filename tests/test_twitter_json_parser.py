#!/usr/bin/python

from twitter_json_parser import TwitterJsonParser
from nose.tools import assert_equals
from mock import Mock

mock = Mock()
parser = TwitterJsonParser()

mock.get_data_from_tweets('data_raw_tweets/sample_mixed_data.json')

def test_get_data_from_tweets():
	assert_equals(str(parser.get_data_from_tweets('data_raw_tweets/sample_mixed_data.json')), 
	"[u'Hollywood and Vine #CRASHLACMA http://t.co/1yr7rB7rFJ', u'Hollywood and Vine', " \
	"u'http://pbs.twimg.com/media/BobePLhCEAA2qoI.jpg', u'Bagley and Venice #CRASHLACMA " \
	"http://t.co/ioPBJgPDtB', u'Bagley and Venice', u'http://pbs.twimg.com/media/BobeYT_CcAA1wFc.jpg', " \
	"u'#CRASHLACMA Motor and Venice 90034 http://t.co/BCyyL7zjIN', u'Motor and Venice 90034', " \
	"u'http://pbs.twimg.com/media/BobaovcIcAIeRNz.jpg', u'Culver and Washington #CRASHLACMA " \
	"https://t.co/3XNSeXyqgI', u'Culver and Washington', u'https://t.co/3XNSeXyqgI', " \
	"u'#CRASHLACMA Overland and Venice http://t.co/sfgHxU5h6h', u'Overland and Venice', " \
	"u'http://t.co/sfgHxU5h6h', u'#CRASHLACMA Sunset and Alverado http://t.co/CK4abafurB', " \
	"u'Sunset and Alverado', u'http://pbs.twimg.com/media/BoasuVvIIAAP9CS.jpg']")