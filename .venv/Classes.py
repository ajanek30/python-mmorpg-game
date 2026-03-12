from abc import ABC, abstractmethod

#klasa abstrakcyjna
class Entity(ABC):
    def __init__(self, name,level,hp,maxHp):
        self.name = name
        self.level = level
        self.hp = hp
        self.maxHp = maxHp
    @abstractmethod
    def makeMove(self):
        pass
    @property
    def isAlive(self):
        return self.hp > 0
#mixiny,pomocniczne
class HealingMixin:
    def receiveHealing(self,amount):
        oldHp = self.hp
        self.hp = min(oldHp + amount, self.maxHp) # zeby nie przekroczyc maxa
        healed = self.hp - oldHp
class InventoryMixin:
    def __init__(self,):
        inventory = []
    def addItem(self,item):
        self.inventory.append(item)
#bohater
class Hero(Entity,HealingMixin,InventoryMixin):
    def __init__(self,name,level,hp,maxHp):
        Entity.__init__(self,name,level,hp,maxHp)
    def makeMoving(self):
        pass
class Warrior(Hero,InventoryMixin,HealingMixin):
    def __init__(self,name,level,hp,maxHp):
        Hero.__init__(self,name,level,hp,maxHp)
    def makeMove(self):
        print(self.name, " warrior is moving")
#wrog
class Enemy(Entity,InventoryMixin,HealingMixin):
    def __init__(self,name,level,hp,maxHp):
        Entity.__init__(self,name,level,hp,maxHp)
    def makeMove(self):
        pass
class Goblin(Enemy,HealingMixin):
    def __init__(self,name,level,hp,maxHp):
        Enemy.__init__(self,name,level,hp,maxHp)
    def makeMove(self):
        print(self.name, " goblin is moving")