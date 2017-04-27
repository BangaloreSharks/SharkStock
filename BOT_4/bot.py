#https://yanpanlau.github.io/2016/10/11/Torcs-Keras.html
from keras.models import Sequential, Model
from keras.layers import Dense, Activation, Flatten, Input, merge
from keras.optimizers import Adam
from keras.models import load_model

import matplotlib.pyplot as plt
from rl.agents import DDPGAgent
from rl.memory import SequentialMemory
from rl.random import OrnsteinUhlenbeckProcess

import environment as stk
env = stk.Stock()
nb_actions = 3

# Next, we build a very simple model.
actor = Sequential()
actor.add(Flatten(input_shape=(1,) + (4,)))
actor.add(Dense(16,kernel_initializer='random_uniform'))
actor.add(Activation('relu'))
# actor.add(Dense(16,kernel_initializer='random_uniform'))
# actor.add(Activation('relu'))
# actor.add(Dense(16,kernel_initializer='random_uniform'))
actor.add(Activation('relu'))
actor.add(Dense(nb_actions,kernel_initializer='random_uniform'))
actor.add(Activation('linear'))
actor.save('BOT_4_actor.h5')

print(actor.summary())

action_input = Input(shape=(nb_actions,), name='action_input')
observation_input = Input(shape=(1,) + (4,), name='observation_input')
flattened_observation = Flatten()(observation_input)
x = merge([action_input, flattened_observation], mode='concat')
x = Dense(32,kernel_initializer='random_uniform')(x)
x = Activation('relu')(x)
# x = Dense(32,kernel_initializer='random_uniform')(x)
# x = Activation('relu')(x)
# x = Dense(32,kernel_initializer='random_uniform')(x)
# x = Activation('relu')(x)
x = Dense(1,kernel_initializer='random_uniform')(x)
x = Activation('linear')(x)
critic = Model(input=[action_input, observation_input], output=x)
critic.save('BOT_4_critic.h5')
print(critic.summary())

# Finally, we configure and compile our agent. You can use every built-in Keras optimizer and
# even the metrics!
memory = SequentialMemory(limit=100000, window_length=1)
random_process = OrnsteinUhlenbeckProcess(size=nb_actions, theta=.01, mu=0., sigma=.9)
agent = DDPGAgent(nb_actions=nb_actions, actor=actor, critic=critic, critic_action_input=action_input,
                  memory=memory, nb_steps_warmup_critic=100, nb_steps_warmup_actor=100,
                  random_process=random_process, gamma=.99, target_model_update=1e-3)
agent.compile(Adam(lr=.001, clipnorm=1.), metrics=['mae'])

# Okay, now it's time to learn something! We visualize the training here for show, but this
# slows down training quite a lot. You can always safely abort the training prematurely using
# Ctrl + C.
agent.fit(env, nb_steps=50000, visualize=False, verbose=1, nb_max_start_steps=0)

# After training is done, we save the final weights.
agent.save_weights('ddpg_{}_weights.h5f'.format("test"), overwrite=True)


observation = env.reset() # Obtain an initial observation of the environment
while True:
    print observation
    action = agent.select_action([observation])
    print action
    action = action.argmax()
    observation, reward, done, info = env.step(action)
    graph_stk,graph_holding,graph_liquidasset,graph_staticasset = env.graphing()
    if done:
        fig, axarr = plt.subplots(3, 1)
        fig.suptitle("DDPG Agent", fontsize=10)
        axarr[0].plot(graph_holding)
        axarr[0].set_title('Stocks held')
        axarr[1].plot(graph_stk)
        axarr[1].set_title('Stocks value')
        axarr[2].plot(graph_liquidasset,color='red')
        axarr[2].plot(graph_staticasset,color='blue')
        axarr[2].set_title('Comparision of stagnant and RL-bot asset value')
        fig.tight_layout()
        fig.subplots_adjust(top=0.88)
        plt.savefig("training/BOT_4/train.png")
        plt.close()
        break
