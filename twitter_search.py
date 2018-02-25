from TwitterSearch import *

def get_Twitter_result(keywords):
    '''accept keywords, and return the grabed messages'''
    try:
        tso = TwitterSearchOrder() # create a TwitterSearchOrder object
        tso.set_keywords([keywords]) # let's define all words we would like to have a look for
        tso.set_language('en') # we want to see German tweets only
        #tso.set_include_entities(True) # and don't give us all those entity information

        # it's about time to create a TwitterSearch object with our secret tokens
        ts = TwitterSearch(
            consumer_key = '8w4uVi0RWPrgJKAftuRjRd8K7',
            consumer_secret = '4kqXXhCcrOAkYt0y7fSd3Q2Ksx6OkRSeR3yOXRDmxznOVH4d9Z',
            access_token = '967595883184390144-osmGFGyegfWRiNz35J0XfXI7g4hHo0x',
            access_token_secret = 'yD6A2NyagzADIz2qTQ5it0uIg448m6OtJT8XhGFQrhAq5'
         )

         # this is where the fun actually starts :)
        messages = []
        f = open('messages.txt','w',encoding='utf-8')
        for tweet in ts.search_tweets_iterable(tso):
            # print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
            messages.append(tweet['text'])
            f.writelines(format('@%s tweeted: %s\n' % ( tweet['user']['screen_name'], tweet['text'] )))
        f.close()
        return messages
    except TwitterSearchException as e: # take care of all those ugly errors if there are some
        print(e)