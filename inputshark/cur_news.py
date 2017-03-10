import urllib2
import urllib
import json
import feedparser

def current_news(value):
	values = {'q': value,
			'output': 'rss'}
	url = 'https://www.google.co.uk/finance/company_news'
	values = urllib.urlencode(values)
	url = url +'?'+ values
	response = urllib2.urlopen(url)
	data = feedparser.parse(response.read())
	news_desc = []
	for item in data['items']:
		news_desc.append(item['description'])
	print(news_desc)
