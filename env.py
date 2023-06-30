import gymnasium as gym
from env import transition

from stable_baselines3 import DQN

#env = gym.make("CartPole-v1", render_mode="human")
env = transition.PokemonRLBattler()

model = DQN("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10000, log_interval=4)
model.save("dqn_cartpole")
print("hi")
del model # remove to demonstrate saving and loading

model = DQN.load("dqn_cartpole")

obs, info = env.reset()
for _ in range (10000):
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, terminated, truncated, info = env.step(action)
    if terminated or truncated:
        obs, info = env.reset()