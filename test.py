import pickle

stockcode = pickle.load(open('pickles/stockcodes'))

for ticker in stockcode.keys():
    print(ticker)
