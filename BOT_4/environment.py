import numpy as np
import pickle
import matplotlib.pyplot as plt

class Stock:
    'generic stock class'
    starting_capital = 10000
    capital = 10000
    stocks_holding = 0
    day = 0
    nb_days = 0
    data = []

    #graph data value
    graph_stk = []
    graph_holding = []
    graph_liquidasset = []
    static_buy_flag = False  # flag indicating if the record for only holding stocks has started
    static_holding = 0
    graph_staticasset = []

    reward_buy_nocapital = -1
    reward_sell_nostock = -1

    def __init__(self):
        self.stocks_holding = 0
        self.starting_capital = 10000
        self.capital = self.starting_capital
        self.data = pickle.load(open('pickles/stock/WIKI_MSFT','rb'))
        self.day = 0
        self.nb_days = len(self.data)-1
        self.reward_buy_nocapital = 0
        self.reward_sell_nostock = 0
        self.graph_stk = []
        self.graph_holding = []
        self.graph_liquidasset = []
        self.static_buy_flag = False
        self.graph_staticasset = []
        self.static_holding = 0
        self.action_space = [0,1,2]

    def reset(self):
        self.stocks_holding = 0
        self.capital = self.starting_capital
        self.day = 0
        self.graph_stk = []
        self.graph_holding = []
        self.graph_liquidasset = []
        self.static_buy_flag = False
        self.graph_staticasset = []
        self.static_holding = 0
        return self.observation()[0]

    def step(self,action):
        reward = 0
        #static buy
        if self.static_buy_flag == False:
            i = self.day
            stock_today = self.data.iloc[i]['Close']
            nb_stocks_buyable = int(self.capital/stock_today)
            self.static_holding = nb_stocks_buyable
            self.static_buy_flag = True

        action = np.argmax(action)
        if action == 0: #buy
            reward = self.buy()
        elif action == 1:    #sell
            reward = self.sell()
        elif action == 2:   #hold
            reward = self.hold()
        #go to the next day
        obs,rwd = self.observation()
        self.day = self.day + 1
        done = False
        if(self.nb_days == self.day):
            # plt.subplot(211)
            # plt.plot(self.graph_holding)
            # plt.subplot(212)
            # plt.plot(self.graph_stk)
            # plt.show()
            done = True
        info = {}
        return obs,float(rwd),done,info

    def buy(self):
        i = self.day
        stock_today = self.data.iloc[i]['Close']
        nb_stocks_buyable = int(self.capital/stock_today)
        #Check if there is no capital
        if(nb_stocks_buyable == 0):
            return self.reward_buy_nocapital
        else:
            self.capital = self.capital - (stock_today*nb_stocks_buyable)
            self.stocks_holding = self.stocks_holding + nb_stocks_buyable
            return self.stocks_holding*stock_today

    def sell(self):
        i = self.day
        stock_today = self.data.iloc[i]['Close']
        if(self.stocks_holding == 0):
            return self.reward_sell_nostock
        else:
            self.capital = self.capital +(self.stocks_holding*stock_today)
            self.stocks_holding = 0
            return self.capital - self.starting_capital*1000

    def hold(self):
        return 0

    def observation(self):
        """[captial,stockvalue,prediction,stocks_holding]"""
        i = self.day
        stock_today = self.data.iloc[i]['Close']
        stock_tomorrow = self.data.iloc[i+1]['Close']
        diff = 0
        if (stock_tomorrow-stock_today)<0:
             diff = 0
        else:
            diff = 1
        # prediction is only 87% accurate
        # if np.random.uniform() < 0.03:
        #     if(diff==0):
        #         diff = 1
        #     else:
        #         diff = 0
        l = []
        l.append(self.capital)
        l.append(stock_today)
        l.append(diff)
        l.append(self.stocks_holding)
        # graphing
        self.graph_stk.append(stock_today)
        self.graph_holding.append(self.stocks_holding)
        liq =  (stock_today*self.stocks_holding)+self.capital
        self.graph_liquidasset.append(liq)
        stag = self.static_holding*stock_today
        self.graph_staticasset.append(stag)
        reward = liq-stag
        return l,reward

    def graphing(self):
        return self.graph_stk,self.graph_holding,self.graph_liquidasset,self.graph_staticasset
