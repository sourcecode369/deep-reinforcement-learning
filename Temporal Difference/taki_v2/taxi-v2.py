import gym
import sys
import numpy as np
import warnings
warnings.filterwarnings("ignore")
from collections import defaultdict, deque
import random
import math

env = gym.make('Taxi-v2')

def epsilon_greedy(Q,state,nA,epsilon):
    if random.random()>epsilon:
        return np.argmax(Q[state])
    else:
        return np.random.choice(env.action_space.n)
        
def update_q(env,Q,nA,alpha,gamma,state,action,reward,next_state=None):
    current = Q[state][action]
    Qsa_next = np.max(Q[next_state]) if next_state is not None else 0
    target = (reward + (gamma*Qsa_next))
    new_value = current + alpha * (target - current)
    return new_value

def q_learning(env,num_episodes,alpha,gamma,plot_every=100):
    nA = env.action_space.n
    Q = defaultdict(lambda: np.zeros(nA))
    
    tmp_score = deque(maxlen=plot_every)
    avg_score = deque(maxlen=num_episodes)
    best_avg_reward = -math.inf
    epsilon = 0.005
    
    for i_episode in range(1,num_episodes+1):
        state = env.reset()
        score = 0
        while True:
            action = epsilon_greedy(Q,state,nA,epsilon)
            next_state, reward, done, info = env.step(action)
            score += reward
            Q[state][action] = update_q(env,Q,nA,alpha,gamma,state,action,reward,next_state)
            state = next_state
            if done:
                tmp_score.append(score)
                break
#             if(i_episode%100)==0:
#                 avg_score.append(np.mean(tmp_score))
        if (i_episode >= 100):

            avg_reward = np.mean(tmp_score)

            avg_score.append(avg_reward)

            if avg_reward > best_avg_reward:
                best_avg_reward = avg_reward

        print("\rEpisode {}/{} || Best average reward {}".format(i_episode, num_episodes, best_avg_reward), end="")
        sys.stdout.flush()
        
        if best_avg_reward >= 9.7:
            print('\nEnvironment solved in {} episodes.'.format(i_episode), end="")
            break
        if i_episode == num_episodes: print('\n')
    return Q, avg_score, best_avg_reward

def play_taxiv2(env,Q,num_episodes):
    rewards = []
    for i_episode in range(num_episodes):
        state = env.reset()
        total_rewards = 0
        while True:
            env.render()
            action = np.argmax(Q[state])
            next_state, reward, done, info = env.step(action)
            total_rewards += reward
            if done:
                rewards.append(total_rewards)
                print("Score: ",total_rewards)
                break
            state= next_state
    env.close()
    print("Score over time: ",sum(rewards)/num_episodes)
    
Q, avg_reward, best_reward = q_learning(env,10000,0.2,1)
play_taxiv2(env,Q,1000)   
