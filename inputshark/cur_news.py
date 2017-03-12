import urllib2
import urllib
import json
import feedparser
import re

#remove \n, convert unicodes to ascii, ignore if conversion isn't possible,remove (..),remove <..>
def cleanhtml(raw_html):
  cleantext = raw_html.encode('ascii','ignore')
  cleanr = re.compile('(<.*?>|\\n|\(.*?\))')
  cleantext = re.sub(cleanr, '', cleantext)
  return cleantext

#get google financial/company news using html request
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
		news_desc.append(cleanhtml(item['description']))
	return news_desc
