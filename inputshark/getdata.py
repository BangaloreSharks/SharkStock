import pickle
import csv
import quandl
from yahoo_finance import Share

def pickle_TrainData(code):
    """"""
    data = quandl.get(code)
    direc = 'pickles/stock/'+code.split('/')[0]+'_'+code.split('/')[1]
    pickle.dump(data,open(direc,'wb'))
    print('data pickled at '+ direc)
    return

def currentstock(code):
    stock = Share(code)
    return stock
