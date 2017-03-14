import pickle
import matplotlib.pyplot as plt

news_data = pickle.load(open('pickles/news/WIKI_MAR'))
stock_data = pickle.load(open('pickles/firstderiv/WIKI_MAR'))

print stock_data
print news_data.keys()
