import urllib
import urllib2
import secret
import json


def getArchived(company_name,year,month):
    url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json'
    api_key = secret.NYTapikey()
    values = {'api-key' : api_key}
    values['q'] = company_name
    values['fq'] = 'news_desk:("Financial")'
    values['begin_date'] = str(year)+str(month)+'01'
    values['end_date'] = str(year)+str(month)+'31'
    data = urllib.urlencode(values)
    url = url +'?'+data
    response = urllib2.urlopen(url)

    #json parsing
    data = response.read()
    parsed_data = json.loads(data)
    doc_list = parsed_data['response']['docs']
    news_list = []
    for doc in doc_list:
        news_list.append(doc['lead_paragraph'])
    return news_list
