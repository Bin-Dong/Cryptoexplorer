# importing the requests library
import requests
import json
from pprint import pprint

def parse_data(name):
	fopen = open(name+'/'+name+"_2018-02-19.json","r")
	writer = open(name+".txt","w")
	sline = ""

	for line in fopen:
		sline+=line.replace('":',"")

	sline = sline.split('",');
	for x in range(0,len(sline)):
		if sline[x].startswith(' "text') and 'RT' not in sline[x]:
			writer.write(sline[x].replace(' "text ','') + "\n")

	fopen.close()
	writer.close()
