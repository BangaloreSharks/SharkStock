import pickle
import csv
import quandl

def pickle_TrainData(code):
    """"""
    data = quandl.get(code)
    direc = 'pickles/'+code.split('/')[0]+'_'+code.split('/')[1]
    pickle.dump(data,open(direc,'wb'))
    print('data pickled at '+ direc)
    return
