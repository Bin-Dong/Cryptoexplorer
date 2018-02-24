# importing the requests library
import requests

def main():
	currency = input("Enter your title\n").upper()

	url = "https://api.coinmarketcap.com/v1/ticker/" + currency
	result = requests.get(url)
	JSON = result.json()
	result.close()
	try:
		format(JSON[0])
	except:
		returned = findSymbols(currency)
		if returned == 0:
			print("No results found!")
		else:
			url = "https://api.coinmarketcap.com/v1/ticker/" + returned[1][:-1]
			result = requests.get(str(url))
			JSON = result.json()
			format(JSON[0])
			result.close()


def format(JSON):
	print("Name: " + JSON["name"])
	print("Symbol: " + JSON["symbol"])
	print("USD: " + JSON["price_usd"])
	print("Percent Change in last hour" +
	JSON["percent_change_1h"])

def findSymbols(currency):
	fopen = open("mapping.txt", "r")
	for line in fopen:
		split = line.split(":")
		if split[0] == currency:
			return split
	return 0

