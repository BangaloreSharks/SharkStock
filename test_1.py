import inputshark.vocab as vocab
import pickle

news_data = pickle.load(open('pickles/news/WIKI_GE'))

for key in news_data.keys():
    for i in news_data[key]:
        if i != None:
            i = i.encode('ascii','ignore')
            vocab.add_vocab(i)
