import pickle
import matplotlib.pyplot as plt

news_data = pickle.load(open('pickles/news/WIKI_MAR'))
stock_data = pickle.load(open('pickles/stock/WIKI_MAR'))

# price plot
plot_data = []
for index,row in stock_data.iterrows():
    plot_data.append(row['Close'])
# plt.plot(plot_data)
# plt.show()

# first derivative plot
plot_derv1 = []
i = 1
while i < len(plot_data):
    plot_derv1.append(plot_data[i]-plot_data[i-1])
    i += 1

plt.plot(plot_derv1)
plt.show()
