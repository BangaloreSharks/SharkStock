import pickle
import matplotlib.pyplot as plt

def get_dates(stock_data):
    date =  {}
    nb_datapoints = len(stock_data)
    date['s_year'] = str(stock_data.iloc[0].name.year)
    date['s_month'] = str(stock_data.iloc[0].name.month)
    date['l_year'] = str(stock_data.iloc[nb_datapoints-1].name.year)
    date['l_month'] = str(stock_data.iloc[nb_datapoints-1].name.month)
    if(date['l_year']>2013):
        date['l_year'] = '2013'
        date['l_month'] = '12'
    return date


def datetolist(date):
    date_list = []
    for year in range(int(date['s_year']),int(date['l_year'])+1):
        if(year == int(date['s_year'])):
            month = int(date['s_month'])
        else:
            month = 1
        for m in range(month,13):
            if(m<10):
                m = '0'+str(m)
            else:
                m = str(m)
            date_dic = {'year':str(year),
                        'month':m}
            date_list.append(date_dic)
    return date_list

def derive(ticker):
    stock_data = pickle.load(open('pickles/stock/WIKI_'+ticker))
    date = get_dates(stock_data)
    date_list = datetolist(date)
    # finding average monthly cost
    data_derv0 = []
    for i in range(0,len(date_list)):
        sum = 0
        count = 0
        month_data = stock_data[date_list[i]['year']+"-"+date_list[i]['month']]
        for index,row in month_data.iterrows():
             sum += row['Close']
             count += 1
        data_derv0.append(sum/count)
    print(len(date_list))
    print len(data_derv0)
    plot_derv1 = {}
    i = 1
    j = 0
    while i < len(data_derv0):
        plot_derv1[date_list[j]['year']+date_list[j]['month']] = data_derv0[i]-data_derv0[i-1]
        i += 1
        j += 1
    pickle.dump(plot_derv1,open('pickles/firstderiv/WIKI_'+ticker,'wb'))
