import inputshark.vocab as vocab
import pickle
import inputshark.manipulate.firstderiv as man
import numpy as np

# l = []
# for i in news_index:
#     print len(i)
#     l.append(len(i))
# print np.mean(l)
#print len(news_index)
# news_index = pickle.load(open('pickles/news_index/y_train/WIKI_GE'))
# print len(news_index)

# l = []
# for key in news_index.keys():
#     for sentence in news_index[key]:
#         if sentence != None:
#             l.append(len(sentence))
#
# print np.median(l)

# man.derive('AGN')
# man.derive('BSRR')
# man.derive('GE')
# man.derive('MAR')
# man.derive('NOC')
# man.derive('REMY')
# man.derive('XPO')
#man.derive('MAN')

#vocab.vocab_index('WIKI_GE')
#vocab.vocab_index('WIKI_MAR')

#
# vocab.process_news_pickle('WIKI_GE')
# vocab.process_news_pickle('WIKI_MAR')
# vocab.process_news_pickle('WIKI_BSRR')
# vocab.process_news_pickle('WIKI_AGN')
# vocab.process_news_pickle('WIKI_MAN')
# vocab.process_news_pickle('WIKI_NOC')
# vocab.process_news_pickle('WIKI_REMY')
# vocab.process_news_pickle('WIKI_XPO')

# vocab.vocab_index('WIKI_GE')
# vocab.vocab_index('WIKI_MAR')
# vocab.vocab_index('WIKI_BSRR')
# vocab.vocab_index('WIKI_AGN')
# vocab.vocab_index('WIKI_MAN')
# vocab.vocab_index('WIKI_NOC')
# vocab.vocab_index('WIKI_REMY')
# vocab.vocab_index('WIKI_XPO')



# for key in news_data.keys():
#     for i in news_data[key]:
#         if i != None:
#             i = i.encode('ascii','ignore')
#             vocab.add_vocab(i)
