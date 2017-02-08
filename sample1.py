import gym
from gym import envs


# print(envs.registry.all())
# env = gym.make('PongNoFrameskip-v3')
# print(env.action_space)
# #> Discrete(2)
# print(env.observation_space)
# #> Box(4,)
# print(env.observation_space.high)
# #> array([ 2.4       ,         inf,  0.20943951,         inf])
# print(env.observation_space.low)
# #> array([-2.4       ,        -inf, -0.20943951,        -inf])


import gym
env = gym.make('FrozenLake-v0')
for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break