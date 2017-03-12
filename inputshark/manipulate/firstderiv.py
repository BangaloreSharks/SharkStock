import pickle
import matplotlib.pyplot as plt

def derive(ticker):
    stock_data = pickle.load(open('pickles/stock/WIKI_'+ticker))
    plot_data = []
    for index,row in stock_data.iterrows():
        plot_data.append(row['Close'])
    plot_derv1 = []
    i = 1
    while i < len(plot_data):
        plot_derv1.append(plot_data[i]-plot_data[i-1])
        i += 1
    pickle.dump(plot_derv1,open('pickles/firstderiv/WIKI_'+ticker,'wb'))
