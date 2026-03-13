import time

import numpy as np
from abc import ABC, abstractmethod

#KLASA ABSTRAKCYJNA

class Entity(ABC):
    def __init__(self, name,level,hp,maxHp,missChance):
        self.name = name
        self.level = level
        self._hp = hp
        self._maxHp = maxHp
        self._missChance = missChance
    @property
    def hp(self):
        return self._hp
    @property
    def maxHp(self):
        return self._maxHp
    @property
    def missChance(self):
        return self._missChance
    @hp.setter
    def hp(self,value):
        self._hp = value
    @maxHp.setter
    def maxHp(self,value):
        self._maxHp = value
    @missChance.setter
    def missChance(self,value):
        self._missChance = value

    # ABSTRAKCYJNE METODY
    @abstractmethod
    def makeMove(self):
        pass

    # MODYFIKATORY DOSTEPU
    @property
    def isAlive(self):
        return self._hp > 0


    def attack(self,target):
        if self.isMissed(bonus=1):
            self.missAttack()
            return
        else:
            damage = self.level * 1.5
            target.takeDamage(damage) #poprawic to wszedzie

    def takeDamage(self,amount):
        self._hp -= amount
        print(f" ⚔️ {self.name} otrzymuje {amount} obrażeń! (Pozostało HP: {max(0, self._hp):.1f})")
        self.lifeChecker()

    def lifeChecker(self):
        if not self.isAlive:
            print(f" 💀 {self.name} umiera!")
            self._hp = 0

    def isMissed(self,bonus = 0):
        currentChance = self._missChance + bonus
        return np.random.randint(0,101) < currentChance

    def missAttack(self):
        print(f" 💨 {self.name} pudłuje!")
            #pass #to implement - todo #missing whatever it means
            #change turn
#METODY SPECJALNE
    def __str__(self):
        return f"[{self.__class__.__name__} Lvl {self.level}] {self.name} | HP: {self._hp}/{self.maxHp}"
    def __repr__(self):
        return f"Entity(name='{self.name}', level={self.level}, hp={self._hp})"
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

#FABRYKI

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

        #METODY STATYCZNE

    @staticmethod
    def createEnemy(enemyType,name,level):
        enemyType = enemyType.lower()
        maxHp = level * 20
        hp = np.random.randint(int(0.2 * maxHp), maxHp + 1)
        missChance = 20
        enemies = \
            {
                "goblin":Goblin,
                "witch":Witch,
                "worm":Worm,
                "dragon":Dragon
            }
        if enemyType in enemies:
            return enemies[enemyType](name,level,hp,maxHp,missChance)
        else:
            return Enemy(name,level,hp,maxHp,missChance)

#MIXINY

class HealingMixin:
    def receiveHealing(self,amount):
        oldHp = self._hp
        self._hp = min(oldHp + amount, self.maxHp) # zeby nie przekroczyc maxa
        healed = self._hp - oldHp
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
    def showInventory(self):
        for item in self.inventory:
            print(item)
#bohater

class Hero(Entity,HealingMixin,InventoryMixin):
    def __init__(self,name,level,hp,maxHp,missChance):
        super().__init__(name,level,hp,maxHp,missChance)
        self.initInventory()
    def __str__(self):
        return super().__str__()
    def makeMove(self):
        pass

#bohaterowie dziedziczni

class Warrior(Hero):
    def __init__(self,name,level):
        super().__init__(name,level,150,150,20)
        self.stamina = 100
    def makeMove(self):
        print(super().__str__(), ": is moving")
    def attack(self,target):
        if self.isMissed(bonus = 5):
            self.missAttack()
        else:
            if self.stamina >= 20:
                self.stamina -= 20
                damage = self.level * 1.5 + self.stamina * 0.3
                target.takeDamage(damage)
            else:
                super().attack(target)

class Knight(Hero):
    def __init__(self,name,level):
        super().__init__(name,level,120,120,30)
    def generateKnightBonus(self):
        return np.random.randint(10,30)

    def makeMove(self):
        print(super().__str__(), ": is moving")
    def attack(self,target):
        if self.isMissed(bonus = 1):
            self.missAttack()
        else:
            bonusDamage = self.generateKnightBonus()
            if(bonusDamage > 15):
                damage = self.level * 1.5 + bonusDamage
                target.takeDamage(damage)
            else:
                super().attack(target)
class Mage(Hero):
    def __init__(self,name,level):
        super().__init__(name,level,90,90,15)
        self.mana = 150
    def makeMove(self):
        print(super().__str__(), ": is moving")

    def attack(self,target):
        if self.isMissed(bonus = 1):
            self.missAttack()
        else:
            if self.mana >= 35:
                self.mana -= 35
                damage = self.level * 1.5 + self.mana * 1.5
                target.takeDamage(damage)
            else:
                super().attack(target)
#wrog

class Enemy(Entity,InventoryMixin,HealingMixin):
    def __init__(self,name,level,hp,maxHp,missChance):
        super().__init__(name,level,hp,maxHp,missChance)
        self.initInventory()
    #METODA KLASOWA
    @classmethod
    def createBoss(cls, name, level):
        maxHp = level * 50
        hp = maxHp
        missChance = 25
        print(f"Generowanie elitarnej jednostki typu {cls.__name__}...")
        return cls(f"Elite {name}", level, hp, maxHp,missChance)
    def __str__(self):
        return super().__str__()
    def makeMove(self):
        pass

#wrogowie dziedziczni

class Goblin(Enemy):
    def __init__(self,name,level,hp,maxHp,missChance):
        super().__init__(name,level,hp,maxHp,missChance)
    def makeMove(self):
        print(super().__str__(), ": is moving")
    def attack(self,target):
        if self.isMissed(bonus = 1):
            self.missAttack()
        else:
            super().attack(target)

class Witch(Enemy):
    def __init__(self,name,level,hp,maxHp,missChance):
        super().__init__(name,level,hp,maxHp,missChance)
    def makeMove(self):
        print(super().__str__(), ": is moving")
    def attack(self,target):
        if self.isMissed(bonus = 1):
            self.missAttack()
        else:
            super().attack(target)

class Worm(Enemy):
    def __init__(self,name,level,hp,maxHp,missChance):
        super().__init__(name,level,hp,maxHp,missChance)
    def makeMove(self):
        print(super().__str__(), ": is moving")
    def attack(self,target):
        if self.isMissed(bonus=1):
            self.missAttack()
        else:
            super().attack(target)

class Dragon(Enemy):
    def __init__(self,name,level,hp,maxHp,missChance):
        super().__init__(name,level,hp,maxHp,missChance)
    def makeMove(self):
        print(super().__str__(), ": is moving")
    def attack(self,target):
        if self.isMissed(bonus=1):
            self.missAttack()
        else:
            super().attack(target)


############################################################################

#POLIMORFIZM

#musi byc obsluga gry z podzialem na tury

enemy = EntityFactory.createEnemy("worm","fiutek",2)
hero = EntityFactory.createHero("warrior","warrior",1)


def fightHandle(entity1,entity2):

    while entity1 and entity2:
        entity1.makeMove()
        entity1.attack(entity2)

        if not entity2:
            break

        entity2.makeMove()
        entity2.attack(entity1)
        time.sleep(1)

        if not entity1:
            break



fightHandle(enemy,hero)
