import csv
import pickle
import time
import os
import inputshark.getdata as gd
import traceback
import quandl as q

# files already downloaded
downloaded_list = []
failed_list = []
for root, dirs, files in os.walk("pickles/stock"):
    for file in files:
        downloaded_list.append(str(file))

# downloading the files
dic = pickle.load(open('company','rb'))
l = len(dic.keys())
count = len(downloaded_list)
d_count = 0
for ticker in dic.keys():
    d_count += 1
    tick = 'WIKI/'+str(ticker)
    filename = 'WIKI_'+str(ticker)
    if(filename not in downloaded_list):
        try:
            gd.pickle_TrainData(str(tick))
            print '{}/{} - {}'.format(count,l,tick)
            time.sleep(1)
        except q.LimitExceededError:
            print "limit exceeded so waiting 10 mins"
            time.sleep(600)
        except Exception as err:
            failed_list.append(tick)
            print '{}/{} - {} failed'.format(count,l,tick)
            traceback.print_exc()
            time.sleep(1)
        count = count+1
    if(d_count == 20):
        sleep(600)

pickle.dump(failed_list,open('failed','wb'))
