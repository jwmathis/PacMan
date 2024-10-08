from custom_environment import PacMan
from dqn_model import DQN, DQNAgent
import numpy as np
from dqn_model import plot_learning_curve

if __name__ == '__main__':
    env = PacMan()
    
    agent = DQNAgent(gamma=0.99, epsilon=1.0, batch_size=64, num_actions=5, 
                     eps_end=0.01, input_dims=(6, 50, 80), lr=0.003)
    scores, eps_history = [], []
    n_games = 500
    
    for i in range(n_games):
        score = 0
        done = False
        observation = env.reset()
        while not done:
            action = agent.choose_action(observation)
            observation_, reward, done, truncated, info = env.step(action)
            print("Shape: ", observation_.shape)
            score += reward
            agent.store_transition(observation, action, reward, observation_, done)
            agent.learn()
            observation = observation_
            env.render()
        scores.append(score)
        eps_history.append(agent.epsilon)
        
        avg_score = np.mean(scores[-100:])
        
        print('epsiode ', i, 'score %.2f' % score, 
                'average score %.2f' % avg_score,
                'epsilon %.2f' % agent.epsilon)
        
    x = [i+1 for i in range(n_games)]
    filename = 'pacman_plot.png'
    plot_learning_curve(x, scores, eps_history, filename)
    