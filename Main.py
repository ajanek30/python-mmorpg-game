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

    def __str__(self):
        return f"[{self.__class__.__name__} Lvl {self.level}] {self.name} | HP: {self.hp}/{self.maxHp}"
    def __repr__(self):
        return f"Entity(name='{self.name}', level={self.level}, hp={self.hp})"
#PRZECIAZENIE OPERATOROW
    def __lt__(self, other):
        if not isinstance(other, Entity):
            return NotImplemented
        return self.level < other.level
    def __eq__(self, other):
        if not isinstance(other, Entity):
            return False
        return self.level == other.level and self.name == other.name
    def __bool__(self):
        return self.isAlive

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
        super().__init__(name,level,hp,maxHp)

    @classmethod
    def createBoss(cls, name, level):
        maxHp = level * 50
        hp = maxHp
        print(f"Generowanie elitarnej jednostki typu {cls.__name__}...")
        return cls(f"Elite {name}", level, hp, maxHp)

    def __str__(self):
        return super().__str__()
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


enemy = EntityFactory.createEnemy("worm","fiutek",5)
#zwykły = Goblin("Gienek", 1, 20, 20)
boss = Goblin.createBoss("boss",7)
print(boss.hp)
print(enemy.maxHp)