import urllib.request
from bs4 import BeautifulSoup


def get_introduction(name):
    '''Accept the name of the currency, return its introduction'''
    if not name:
        return
    link = 'https://info.binance.com/en/currencies/'+name
    request = urllib.request.Request(link)
    try:
        response = urllib.request.urlopen(request)
    except urllib.error.HTTPError:
        return
    soup = BeautifulSoup(response,'html.parser')
    text = soup.get_text()
    start = text.find('Introduction')   # start location for introduction
    end = text.find('\n\n\n',start)
    print(text[start+14:end])     # print the intruction after the label

