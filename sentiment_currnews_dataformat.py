import os
import pickle
import numpy as np
import inputshark.vocab as vocab
import progressbar


stock = pickle.load(open('pickles/currnews/stock/1/stock.pickle','rb'))
y_train = []

#get all company names
company_list = stock.keys()

# get all the headlines to one single list
sentence_list = []
for company in company_list:
    x = pickle.load(open('pickles/currnews/news/1/'+company,'rb'))
    for  i in range(len(x)):
        y_train.append(stock[company])
    sentence_list = sentence_list + x

# process each sentence
print "cleaning the text corpus ..."
cleaned_sentence_list = []
bar = progressbar.ProgressBar(maxval=len(sentence_list), \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
bar.start()
count = 0
for i,sentence in enumerate(sentence_list):
    x = vocab.process_sentence(sentence)
    if x == None:
        del(y_train[i])
    else:
        cleaned_sentence_list.append(x)
    bar.update(count)
    count += 1
bar.finish()

pickle.dump(y_train,open('pickles/currnews/train_ytrain_01.pickle','wb'))

# # creating the bagofwords
# print "creating bag of words ..."
# vocab.addtovocab(cleaned_sentence_list)
#
#
# #indexing the sentences
# print "indexing the sentences"
# indexed_sentence_list = []
# bar = progressbar.ProgressBar(maxval=len(sentence_list), \
#     widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
# bar.start()
# count = 0
# for sentence in cleaned_sentence_list:
#     indexed_sentence_list.append(vocab.index_sentence(sentence))
#     bar.update(count)
#     count += 1
# bar.finish()

#pickle the training data
pickle.dump(indexed_sentence_list,open('pickles/currnews/train_Xtrain_01.pickle','wb'))
