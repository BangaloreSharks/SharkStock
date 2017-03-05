import tensorflow as tf
import tensorflow.contrib.slim as slim
import numpy as np
import pickle
import env
import matplotlib.pyplot as plt

#importing Data from pickle
data = pickle.load(open('WIKI_MSFT','rb'))

#setting env
capital = 1000.0
fb_stock = env.Stock()
yesterdays_assets = capital
assets = capital

#Result tracking
asset_history = []

#COMPLETE THIS
def execAction(action_id,stk_data):
    global yesterdays_assets,assets,capital
    volume = 1 #MAX POSSIBLE
    if(action_id==0):   #Buy
        yesterdays_assets = assets
        capital = fb_stock.buy(capital,stk_data,volume)
        assets = capital+fb_stock.liquid_value(stk_data)
        asset_history.append(assets)
        #print '{} Buy'.format(assets)
    elif(action_id==1): #Sell
        yesterdays_assets = assets
        capital = fb_stock.sell(capital,stk_data,volume)
        assets = capital+fb_stock.liquid_value(stk_data)
        asset_history.append(assets)
        #print '{} Sell'.format(assets)
    else:               #hold
        assets = capital+fb_stock.liquid_value(stk_data)
        #print '{} Hold'.format(assets)
        asset_history.append(assets)
#COMPLETE THIS
def getReward():
    return assets-yesterdays_assets

#   NETWORK ARCHITECTURE
#   (input layer)                         (output layer)
#
#   stock_open
#   stock_close                             buy
#   stock_high      (fully_connected)       sell
#   stock_low                               hold
#   capital
#   stock_held
#



class agent():
    def __init__(self,lr):
        #FFN fully connected no hidden layer
        self.state_in = tf.placeholder(shape=[1,6],dtype=tf.float32)
        output = slim.fully_connected(self.state_in,3,biases_initializer=None,activation_fn=tf.nn.sigmoid,weights_initializer=tf.ones_initializer())
        self.output = tf.reshape(output,[-1])
        self.chosen_action = tf.argmax(self.output,0)

        #training
        self.reward_holder = tf.placeholder(shape=[1],dtype=tf.float32)
        self.action_holder = tf.placeholder(shape=[1],dtype=tf.int32)
        self.responsible_weight = tf.slice(self.output,self.action_holder,[1])
        self.loss = -(tf.log(self.responsible_weight)*self.reward_holder)
        optimizer = tf.train.GradientDescentOptimizer(learning_rate=lr)
        self.update = optimizer.minimize(self.loss)


tf.reset_default_graph()
myAgent = agent(lr=0.001)
weights = tf.trainable_variables()[0]

epochs = 100
e = 0.1 # probability of random action

init = tf.initialize_all_variables()

with tf.Session() as sess:
    sess.run(init)
    i=0
    for epoch in range(epochs):

        #reinitializing global variables
        capital = 1000.0
        fb_stock = env.Stock()
        yesterdays_assets = capital
        assets = capital
        asset_history = []

        print ':::::Starting epoch {} ::::::::::::::::::::::'.format(epoch)
        for index,row in data.iterrows():
            #print '{}'.format(index)
            state = np.zeros([1,6])
            state[0,0] = row['Open']
            state[0,1] = row['Close']
            state[0,2] = row['High']
            state[0,3] = row['Low']
            state[0,4] = capital
            state[0,5] = fb_stock.stocks_holding

            #Choose either a random action or one from our network.
            if np.random.rand(1) < e:
                action = np.random.randint(3)
            else:
                action = sess.run(myAgent.chosen_action,feed_dict={myAgent.state_in:state})

            execAction(action,row)
            reward = getReward()

            #Update the network.
            feed_dict={myAgent.reward_holder:[reward],myAgent.action_holder:[action],myAgent.state_in:state}
            _,ww = sess.run([myAgent.update,weights], feed_dict=feed_dict)
        print 'asset = {}'.format(assets)
        #plt.plot(asset_history)
        #plt.show()
