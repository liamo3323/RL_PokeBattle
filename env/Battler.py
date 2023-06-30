import random
import pokebase as pb
from pokemonBuilder import Pokemon


class Battler():
    def speedCheck(object:builder.Pokemon, target:builder.Pokemon):
        if (object.speed > target.speed):
            return False # player is faster
        else:
            return True # enemy is faster

    def hpBar(pokemon:builder.Pokemon):
        percentageHp = 0.0
        hpBar = "║"
        maxHp = pokemon.hp
        remainingHp = pokemon.remainingHp
        percentageHp = remainingHp/maxHp
        percentageHp = int(percentageHp*10)
        for _ in range(percentageHp):
            hpBar+="▓▓▓▓"
        for _ in range(10-percentageHp):
            hpBar+="    "
        hpBar+="║"
        return hpBar

    def damageCalculation(player:builder.Pokemon, target:builder.Pokemon, move:builder.Move):
        pokemonLevel = player.lvl
        power = move.power
        stab = 1
        if (move.type == player.typeA) or (move.type == player.typeB):
            stab = 1.2 

        baseDamage = ((((((2 * pokemonLevel) / 5 ) + 2 ) * power * player.attack / target.defense ) / 50 ) + 2 ) * stab 

        #print(baseDamage)
        return baseDamage

    def consoleDisplayInfo(player:builder.Pokemon, enemy:builder.Pokemon, display:bool):
        if display is True:
            move1 = player.move1.name
            move2 = player.move2.name
            move3 = player.move3.name
            move4 = player.move4.name
            print(f"\n\n{(hpBar(enemy))[::-1]} {round(enemy.remainingHp)}/{enemy.hp} {enemy.name} \n\n{player.name} {round(player.remainingHp)}/{player.hp} {hpBar(player)} \n\n    [{move1}]    [{move2}]\n    [{move3}]    [{move4}]")

    def enemyAction(player:builder.Pokemon, enemy:builder.Pokemon):
        action = random.randint(0,4)
        if action == 1:
            print(f"the enemy {enemy.name} used {player.move1.name}")
            player.remainingHp -= damageCalculation(enemy,player, enemy.move1)
        else:
            print(f"the enemy is distracted...") 

    def playerAction(player:builder.Pokemon, enemy:builder.Pokemon, action:int):
            if (action) == 1:
                print(f"{player.name} used {player.move1.name}") 
                enemy.remainingHp -= damageCalculation(player, enemy, player.move1)
            if (action) == 2:
                print(f"{player.name} used {player.move2.name}") 
                enemy.remainingHp -= damageCalculation(player, enemy, player.move2)
            if (action) == 3:
                print(f"{player.name} used {player.move3.name}") 
                enemy.remainingHp -= damageCalculation(player, enemy, player.move3)
            if (action) == 4:
                print(f"{player.name} used {player.move4.name}") 
                enemy.remainingHp -= damageCalculation(player, enemy, player.move4)        

    def battleLoop(player:builder.Pokemon, enemy:builder.Pokemon, display:bool=True):  

        while(player.remainingHp > 0) and (enemy.remainingHp > 0):
            consoleDisplayInfo(player,enemy,display)
            faster = speedCheck(player, enemy)
            action = input("What would you like to do?")
            action = int(action)
            if faster:
                playerAction(player,enemy, action)
                enemyAction(player, enemy)
            else:
                enemyAction(player, enemy)
                playerAction(player,enemy, action)
        print(f"{enemy.name} has been defeated")

    def main():
        p1 = builder.Pokemon(1)
        p2 = builder.Pokemon(2)
        print(f"a wild ivysaur has appeared!\n")
        battleLoop(p1,p2)

    if __name__ == "__main__":
        main()