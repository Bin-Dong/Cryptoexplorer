# importing the requests library
import requests

def main():
	writer = open("mapping.txt", "w+")
	url = "https://api.coinmarketcap.com/v1/ticker/?limit=1530"
	result = requests.get(url)
	JSON = result.json()
	counter = 0;
	for x in range (0,len(JSON)):
		writer.write(JSON[x]["symbol"] + ":" + JSON[x]["name"].replace(" ","-") +"\n")
	writer.close()

def format(JSON):
	print("Name: " + JSON["name"])
	print("Symbol: " + JSON["symbol"])
	print("USD: " + JSON["price_usd"])
	print("Percent Change in last hour" +
	JSON["percent_change_1h"])

main()
