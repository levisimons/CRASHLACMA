from slistener import SListener
import time, tweepy, sys

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler('FE01Tcf6sDZpLG0vabqA', 'zuqcRA0XIoMU0o6swx6vzWENtWZNIAXHQtZWbfk')
auth.set_access_token('31018035-FbvB97V4QDqoAcQAg49z1UYlgrssenP4L8cgzWah6', 'jPqA3vQkAvrjV2XUVIfjFBgHJWpNgvubrfsR6E9EJTuCH')
api = tweepy.API(auth)

# testcases:
# hollywood & vine, hollywood and vine
# order of operations: hashtag, img, address, other text.
# hashtag allcaps or lowercase
# uploaded image, link to hosted image


def main():
    track = ['#CRASHLACMA']
 
    listen = SListener(api, 'crashlacma')
    stream = tweepy.Stream(auth, listen)

    print "Streaming started..."

    try: 
        stream.filter(track = track)
    except:
        print "error!"
        stream.disconnect()

if __name__ == '__main__':
    main()