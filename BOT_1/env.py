class Stock:
    'generic stock class'
    stocks_holding = 0

    def __init__(self):
        self.stocks_holding = 0

    def buy(self,capital,stk_data,volume,debug=False):
        cost_per_share = float(stk_data['Close'])
        total_cost = cost_per_share*volume
        # debug info
        if(debug == True):
            print '___BUY______________________________________________'
            print 'cost_per_share = '+str(cost_per_share)
            print 'total_cost = '+str(total_cost)
            print 'capital = '+str(capital)
            print 'STOCKS_HOLDING = '+str(self.stocks_holding)
        if(total_cost > capital):             # Check if cost of purchase is higher than capital
            volume = int(capital / cost_per_share)  # If not affordable, find max feasible buy volume
            total_cost = volume * cost_per_share
            # debug info
            if(debug == True):
                print 'affordable buy cost = '+str(total_cost)
                print 'affordable buy vol  = '+str(volume)
        capital = capital - total_cost
        self.stocks_holding = self.stocks_holding + volume
        # debug info
        if(debug == True):
            print 'NEW capital = '+str(capital)
            print 'NEW STOCKS_HOLDING = '+str(self.stocks_holding)
            print '____________________________________________________'
        return capital

    def sell(self,capital,stk_data,volume,debug=False):
        cost_per_share = float(stk_data['Close'])
        if(volume > self.stocks_holding):   # checks if stocks are held to sell
            volume = self.stocks_holding
        total_cost = cost_per_share * volume
        # debug info
        if(debug == True):
            print '___SELL______________________________________________'
            print 'cost_per_share = '+str(cost_per_share)
            print 'total_cost = '+str(total_cost)
            print 'capital = '+str(capital)
            print 'STOCKS_HOLDING = '+str(self.stocks_holding)
        capital = capital + total_cost
        self.stocks_holding = self.stocks_holding - volume
        # debug info
        if(debug == True):
            print 'NEW capital = '+str(capital)
            print 'NEW STOCKS_HOLDING = '+str(self.stocks_holding)
            print '____________________________________________________'
        return capital

    def liquid_value(self,stk_data):
        cost_per_share = float(stk_data['Close'])
        value = cost_per_share * self.stocks_holding
        return value
