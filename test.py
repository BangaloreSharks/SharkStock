import pickle
import BOT_1.env as env

def liq(i):
    print 'LIQ_VAL'+str(capital+fb_stock.liquid_value(data.iloc[[i]]))

data = pickle.load(open('pickles/WIKI_FB','rb'))
capital = 1000
    
fb_stock = env.Stock()

capital = fb_stock.buy(capital,data.iloc[[0]],10,debug=True)
liq(0)
capital = fb_stock.buy(capital,data.iloc[[1]],200,debug=True)
liq(1)
capital = fb_stock.sell(capital,data.iloc[[2]],3,debug=True)
liq(2)
capital = fb_stock.buy(capital,data.iloc[[0]],10,debug=True)
liq(0)
capital = fb_stock.buy(capital,data.iloc[[1]],200,debug=True)
liq(1)
capital = fb_stock.sell(capital,data.iloc[[2]],3,debug=True)
liq(2)
capital = fb_stock.buy(capital,data.iloc[[0]],10,debug=True)
liq(0)
capital = fb_stock.buy(capital,data.iloc[[1]],200,debug=True)
liq(1)
capital = fb_stock.sell(capital,data.iloc[[2]],3,debug=True)
liq(2)
