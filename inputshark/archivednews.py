import urllib
import urllib2
import secret


def getArchived(company_Name,year,month):
    url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json'
    api-key = secret.NYTapikey()







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
