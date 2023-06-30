# Building the necessary information needed for battling will be a pain to do later so this seperate doc will be used to import all the pokemon via name or dex id 
import pokebase as pb

class pokemon:
    def __init__(self, ID):
        self.obj = pb.pokemon(ID)
        self.id = ID
        self.name = self.obj.name
        self.lvl = 50
        self.typeA = self.obj.types[0].type.name
        self.typeB = self.obj.types[1].type.name

        self.hp= self.obj.stats[0].base_stat
        self.attack = self.obj.stats[1].base_stat
        self.defense = self.obj.stats[2].base_stat
        self.spAttack = self.obj.stats[3].base_stat
        self.spDefense = self.obj.stats[4].base_stat
        self.speed = self.obj.stats[5].base_stat
        
        self.remainingHp = self.hp
        self.move1 = Move(1)
        self.move2 = Move(2)
        self.move3 = Move(3)
        self.move4 = Move(4)

class Move:
    def __init__(self, ID):
        self.obj = pb.move(ID)
        self.name = self.obj.names[7].name
        self.power = self.obj.power
        self.pp = self.obj.pp
        self.damageType = self.obj.damage_class.name
        self.type = self.obj.type.name
        