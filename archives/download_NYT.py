import pickle
import os
import inputshark.archivednews as an
import time
import urllib2

def get_dates(stock_data):
    date =  {}
    nb_datapoints = len(stock_data)
    date['s_year'] = str(stock_data.iloc[0].name.year)
    date['s_month'] = str(stock_data.iloc[0].name.month)
    date['l_year'] = str(stock_data.iloc[nb_datapoints-1].name.year)
    date['l_month'] = str(stock_data.iloc[nb_datapoints-1].name.month)
    if(date['l_year']>2013):
        date['l_year'] = '2013'
        date['l_month'] = '12'
    return date

def datetolist(date):
    date_list = []
    for year in range(int(date['s_year']),int(date['l_year'])+1):
        if(year == int(date['s_year'])):
            month = int(date['s_month'])
        else:
            month = 1
        for m in range(month,13):
            if(m<10):
                m = '0'+str(m)
            else:
                m = str(m)
            date_dic = {'year':str(year),
                        'month':m}
            date_list.append(date_dic)
    return date_list

# Stock data of companies available
stock_list = []
for root, dirs, files in os.walk("pickles/stock"):
    for file in files:
        stock_list.append(str(file.split('_')[1]))

# Load ticker -> company_name
stock = pickle.load(open('pickles/stockcodes'))


# News data of companies available
news_list = []
for root, dirs, files in os.walk("pickles/news"):
    for file in files:
        news_list.append(str(file.split('_')[1]))

for ticker in stock_list:
    if(stock[ticker]!=''):
        if(ticker not in news_list):
            # Load stock data
            stock_data = pickle.load(open('pickles/stock/WIKI_'+ticker,'rb'))
            date = get_dates(stock_data)
            date_list = datetolist(date)
            dic = {}
            for date in date_list:
                print(date['year'],'-',date['month'])
                while True:
                    try:
                        news_list = an.getArchived(stock[ticker],date['year'],date['month'])
                    except urllib2.HTTPError:
                        continue
                    break
                print(news_list)
                dic[date['year']+date['month']] = news_list
                time.sleep(10)
            pickle.dump(dic,open('pickles/news/WIKI_'+ticker,'wb'))
