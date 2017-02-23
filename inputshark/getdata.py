import pickle
import csv

def makePickle(filename,output="pickle.p"):
    """makePickle(filename,output="_pickle.p"): Reads dictionary csv and generates pickle"""
    out_dic = {}
    with open(filename,'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            out_dic[row[0]] = row[1]
    pickle.dump( out_dic , open( 'pickles/'+output , "wb" ) )
    return
