# importing the requests library
import requests
import json
from pprint import pprint

def main():
	fopen = open("Bitcoin_2018-02-19.json","r")
	writer = open("text.txt","w")
	sline = ""

	for line in fopen:
		sline+=line.replace('":',"")

	sline = sline.split('",');
	for x in range(0,len(sline)):
		if sline[x].startswith(' "text') and ("bitcoin" in sline[x] or "Bitcoin" in sline[x] or "BitCoin" in sline[x] or "bitCoin" in sline[x]):
			writer.write(sline[x].replace(' "text ','') + "\n")

	fopen.close()
	writer.close()

main()
