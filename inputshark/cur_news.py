import urllib2
import urllib
import json
import feedparser

def current_news(value):
	values = {'q': value,
			'output': 'xml'}
	url = 'https://www.google.co.uk/finance/company_news'
	values = urllib.urlencode(values)
	url = url +'?'+ values
	response = urllib2.urlopen(url)
	# print response.read()
	data = feedparser.parse(response.read())
	print data['channel']
	return data


