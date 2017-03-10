import urllib
import urllib2
import secret


def getArchived(company_name,year,month):
    url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json'
    api_key = secret.NYTapikey()
    values = {'api-key' : api_key}
    values['q'] = company_name
    values['fq'] = 'news_desk:("Financial")'
    values['begin_date'] = 20110101
    values['end_date'] = 20110201
    data = urllib.urlencode(values)
    url = url +'?'+data
    response = urllib2.urlopen(url)
    print(response.read())



# url = 'http://www.someserver.com/cgi-bin/register.cgi'
#
# values = {'name' : 'Michael Foord',
#           'location' : 'Northampton',
#           'language' : 'Python' }
#
# data = urllib.urlencode(values)
# req = urllib2.Request(url, data)
# response = urllib2.urlopen(req)
# the_page = response.read()
