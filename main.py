from  get_introduction import *
from  get_api import *
from twitter_search import *

currency = get_coin_info()
get_introduction(currency)
messages = get_Twitter_result(currency)


