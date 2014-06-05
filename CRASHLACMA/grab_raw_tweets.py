#!/usr/bin/python

from slistener import SListener
import time, tweepy, sys

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler('FE01Tcf6sDZpLG0vabqA', 'zuqcRA0XIoMU0o6swx6vzWENtWZNIAXHQtZWbfk')
auth.set_access_token('31018035-FbvB97V4QDqoAcQAg49z1UYlgrssenP4L8cgzWah6', 'jPqA3vQkAvrjV2XUVIfjFBgHJWpNgvubrfsR6E9EJTuCH')
api = tweepy.API(auth)

DIR_RAW_TWEET_DATA='../data_raw_tweets'

output_file_prefix = 'crashlacma'

def main():
    track = ['#CRASHLACMA']
 
    listen = SListener(api, DIR_RAW_TWEET_DATA + '/' + output_file_prefix)
    stream = tweepy.Stream(auth, listen)

    print "Streaming started..."

    try: 
        stream.filter(track = track)
    except:
        print "error!"
        stream.disconnect()

if __name__ == '__main__':
    main()