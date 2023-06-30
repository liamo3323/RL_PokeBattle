import random
import pokebase as pb
from . import pokemon_builder

class PokemonRLBattler():
    def __init__(self):
        self.player = pokemon_builder(1)
        self.enemy = pokemon_builder(2)

    def step(self, action): # single timestep method
        reward, done = 0, 0

        if faster:
            poke.playerAction(self.player, self.enemy, action)
            poke.enemyAction(self.player, self.enemy)
        else:
            poke.enemyAction(self.player, self.enemy)
            poke.playerAction(self.player,self.enemy, action)
        
        reward = check_done()
        state = enemy.remainingHp

        return reward, state, done
    
    def reset(self): # ran at the start of the environment and at the end of each episode

        print(f"A wild {self.enemy.name} appeared!")
    
    #TODO Later after barebones is done
    def render():
        return None

    def check_done(self):
        reward = 0
        if (enemy.remainingHp < 0):
            reward = 1
        if (player.remainingHp < 0):
            reward = -1
        return reward