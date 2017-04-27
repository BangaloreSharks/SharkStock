import pickle

data = pickle.load(open('pickles/stock/WIKI_GE','rb'))
temp = data.loc['2015-06-01':'2016-06-20']
print temp
pickle.dump(temp,open('pickles/shortstock/WIKI_GE','wb'))
