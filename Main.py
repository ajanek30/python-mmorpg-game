import random
import numpy as np
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

class EntityFactory:
    @staticmethod
    def createHero(heroType,name,level):
        heroType = heroType.lower()
        heros =\
            {
                "warrior":Warrior,
                "mage":Mage,
                "knight":Knight
            }
        if heroType in heros:
            return heros[heroType](name,level)
        else:
            raise ValueError(f"Nieznany typ bohatera: {heroType}")
    @staticmethod
    def createEnemy(enemyType,name,level):
        enemyType = enemyType.lower()
        maxHp = level * 20
        hp = np.random.randint(int(0.2 * maxHp), maxHp + 1)
        enemies = \
            {
                "goblin":Goblin,
                "witch":Witch,
                "worm":Worm,
                "dragon":Dragon
            }
        if enemyType in enemies:
            return enemies[enemyType](name,level,hp,maxHp)
        else:
            return Enemy(name,level,hp,maxHp)
#mixiny,pomocniczne

#hp powinno zalezc od level - todo!

class HealingMixin:
    def receiveHealing(self,amount):
        oldHp = self.hp
        self.hp = min(oldHp + amount, self.maxHp) # zeby nie przekroczyc maxa
        healed = self.hp - oldHp
        print("Healed",healed)
class InventoryMixin:
    def initInventory(self):
        self.inventory = []
    def addItem(self,item):
        self.inventory.append(item)
        print(item, " added to inventory")
    def dropItem(self,item):
        self.inventory.remove(item)
        print(item, " removed from inventory")

#bohater
class Hero(Entity,HealingMixin,InventoryMixin):
    def __init__(self,name,level,hp,maxHp):
        super().__init__(name,level,hp,maxHp)
        self.initInventory()
    def makeMoving(self):
        pass

#bohaterowie dziedziczni
class Warrior(Hero):
    def __init__(self,name,level):
        super().__init__(name,level,150,150)
        self.stamina = 100
    def makeMove(self):
        print(self.name, " warrior is moving")
class Knight(Hero):
    def __init__(self,name,level):
        super().__init__(name,level,120,120)
    def makeMove(self):
        print(self.name, " warrior is moving")
class Mage(Hero):
    def __init__(self,name,level):
        super().__init__(name,level,90,90)
        self.mana = 150
    def makeMove(self):
        print(self.name, " mage is moving")
#wrog
class Enemy(Entity,InventoryMixin,HealingMixin):
    def __init__(self,name,level,hp,maxHp):
        super().__init__(self,name,level,hp)
    def makeMove(self):
        pass
#wrogowie dziedziczni
class Goblin(Enemy):
    def __init__(self,name,level,hp,maxHp):
        super().__init__(name,level,hp,maxHp)
    def makeMove(self):
        print(self.name, " goblin is moving")
class Witch(Enemy):
    def __init__(self,name,level,hp,maxHp):
        super().__init__(name,level,hp,maxHp)
    def makeMove(self):
        print(self.name, " witch is moving")
class Worm(Enemy):
    def __init__(self,name,level,hp,maxHp):
        super().__init__(name,level,hp,maxHp)
    def makeMove(self):
        print(self.name," worm is moving")
class Dragon(Enemy):
    def __init__(self,name,level,hp,maxHp):
        super().__init__(name,level,hp,maxHp)
    def makeMove(self):
        print(self.name," dragon is moving")


enemy = EntityFactory.createEnemy("worm","fiutek",15)
print(enemy.maxHp)