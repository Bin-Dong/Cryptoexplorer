import twitter

api = twitter.api(consumer_key='8w4uVi0RWPrgJKAftuRjRd8K7',
  consumer_secret='4kqXXhCcrOAkYt0y7fSd3Q2Ksx6OkRSeR3yOXRDmxznOVH4d9Z',
  access_token_key='967595883184390144-osmGFGyegfWRiNz35J0XfXI7g4hHo0x',
  access_token_secret='yD6A2NyagzADIz2qTQ5it0uIg448m6OtJT8XhGFQrhAq5')


search = api.GetSearch("Bitcoin") # Replace happy with your search
for tweet in search:
    print(tweet.id, tweet.text)
 