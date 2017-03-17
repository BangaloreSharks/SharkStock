import urllib2
import urllib
import json
import feedparser
import re
import pickle
import os
import secret
import quandl
import inputshark.getdata as gd

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

def getallcompanynews():
    #get already donwloaded file
    news_list = []
    failed_list = []
    for root, dirs, files in os.walk("pickles/currnews/news/1/"):
        for file in files:
            news_list.append(str(file))
    stock = pickle.load(open('pickles/stockcodes'))
    print news_list
    for key in stock.keys():
        if key not in news_list:
            newlist = []
            try:
                print key
                newlist = current_news(key)
            except:
                print 'failed -'+key
                failed_list.append(key)
            pickle.dump(newlist,open('pickles/currnews/news/1/'+key,'wb'))
    print failed_list

def getallcompanystock():
    news_list = []
    for root, dirs, files in os.walk("pickles/currnews/news/1/"):
        for file in files:
            news_list.append(str(file))
    dic = {}
    # Download
    count = 0
    total = len(news_list)
    for ticker in news_list:
        count += 1
        print (ticker,' -',count,'/',total)
        try:
            t = gd.currentstock(ticker)
            x = t.get_change()
            if(x<0):
                dic[ticker] = 0
            else:
                dic[ticker] = 1
        except:
            print (ticker,'failed')
    pickle.dump(dic,open('pickles/currnews/stock/1/stock.pickle','wb'))
