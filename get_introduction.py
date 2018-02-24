import urllib.request
from bs4 import BeautifulSoup

def get_introduction(name):
    '''Accept the name of the currency, return its introduction'''
    link = 'https://info.binance.com/en/currencies/'+name
    request = urllib.request.Request(link)
    response = urllib.request.urlopen(request)
    soup = BeautifulSoup(response,'html.parser')
    text = soup.get_text()
    start = text.find('Introduction')   # start location for introduction
    end = text.find('\n\n\n',start)
    return text[start:end]      # return the introduction