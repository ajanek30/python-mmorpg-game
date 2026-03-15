import random
import time
import os

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
        self._hp = max(0,self._hp - amount)
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

class Item(ABC):
    def __init__(self,name,description):
        self.name = name
        self.description = description
    @abstractmethod
    def use(self, target):
        pass
    def __str__(self):
        return f"{self.name} ({self.description})"
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
        xp = round(int(0.5 * maxHp))

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
        print(item, "added to inventory!")
    def dropItem(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            print(item, " removed from inventory!")

#itemy

class Weapon(Item):
    def __init__(self,name,description,damageBonus):
        super().__init__(name,description)
        self.damageBonus = damageBonus
    def use(self,target):
        target.equipWeapon(self)
class Potion(Item):
    def __init__(self,name,description,healAmount):
        super().__init__(name,description)
        self.healAmount = healAmount
    def use(self,target):
        print(f"🧪 {target.name} wypija {self.name}...")
        target.receiveHealing(self.healAmount)

#bohater

class Hero(Entity,HealingMixin,InventoryMixin):
    def __init__(self,name,level,hp,maxHp,missChance,xp = 0,xpToLevelUp = 100,equippedWeapon=None):
        super().__init__(name,level,hp,maxHp,missChance)
        self.initInventory()
        self.equippedWeapon = equippedWeapon
        self._xp = xp
        self._xpToLevelUp = xpToLevelUp

    @property
    def xp(self):
        return self._xp
    @property
    def xpToLevelUp(self):
        return self._xpToLevelUp

    def equipWeapon(self, newWeapon):
        if self.equippedWeapon is not None:
            print(f"🔄 {self.name} chowa {self.equippedWeapon.name} do plecaka.")
            self.addItem(self.equippedWeapon)
        self.equippedWeapon = newWeapon
        if newWeapon in self.inventory:
            self.inventory.remove(newWeapon)
    def levelUp(self):
        #todo

        self.level += 1
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
            weaponBonus = self.equippedWeapon.damageBonus if self.equippedWeapon else 0
            if self.stamina >= 20:
                self.stamina -= 20
                damage = self.level * 1.5 + self.stamina * 0.3 + weaponBonus
                target.takeDamage(damage)
            else:
                damage = self.level * 1.5 + weaponBonus
                target.takeDamage(damage)

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
            weaponBonus = self.equippedWeapon.damageBonus if self.equippedWeapon else 0
            bonusDamage = self.generateKnightBonus()
            if(bonusDamage > 15):
                damage = self.level * 1.5 + bonusDamage + weaponBonus
                target.takeDamage(damage)
            else:
                damage = self.level * 1.5 + weaponBonus
                target.takeDamage(damage)
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
            weaponBonus = self.equippedWeapon.damageBonus if self.equippedWeapon else 0
            if self.mana >= 35:
                self.mana -= 35
                damage = self.level * 1.5 + self.mana * 1.5 + weaponBonus
                target.takeDamage(damage)
            else:
                damage = self.level * 1.5 + weaponBonus
                target.takeDamage(damage)
#wrog

class Enemy(Entity,InventoryMixin,HealingMixin):
    def __init__(self,name,level,hp,maxHp,missChance):
        super().__init__(name,level,hp,maxHp,missChance)
        self._xp = round(self.maxHp * random.random())
        self.initInventory()
    @property
    def xp(self):
        return self._xp
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

enemy1 = EntityFactory.createEnemy("worm", "fiutek", 8)
enemy2 = EntityFactory.createEnemy("witch", "frajer", 8)
player = EntityFactory.createHero("warrior", "warrior", 1)
miecz = Weapon("Stalowy Miecz", "Zwykły miecz z pobliskiej kuźni", damageBonus=10)
rozdzka = Weapon("Magiczna różdżka","różdżka wykuta przez niebiosa", damageBonus=20)
mikstura = Potion("Mała Mikstura Życia", "Leczy 30 HP", healAmount=30)

def gameHandle(player):

    player.addItem(miecz)
    player.addItem(mikstura)

    Goblin.createBoss(player.name,player.level)

    fightHandle(player,enemy1)
    print(f"Następny przeciwnik!\n ##################################")
    fightHandle(player,enemy2)
    #i tu kolejny przeciwnik itd

def fightHandle(player,enemy):

#jakos oni musza miec iles potek itd czy moga sie leczyc w nieskonczonosc???
    while player and enemy:
        aktualnaBron = player.equippedWeapon if player.equippedWeapon else "Puste pięści"
        print(f"\n[Twoja tura] {player.name} HP: {player.hp:.1f}/{player.maxHp} Level: {player.level}({player.xp}/{player.xpToLevelUp})"
              f" | {enemy.name} HP: {enemy.hp:.1f}/{enemy.maxHp} Level: {enemy.level}({enemy.xp})")
        print("Co chcesz zrobić?\n")
        print(f"[1] Atak ⚔️ | twoja broń : {aktualnaBron}")
        print("[2] Wybierz przedmiot/ekwipunek 🎒")
        print("[3] Ucieczka🏃‍♂️")

        mainChoice = input("Wybierz akcję (1/2/3/4): ")
        print("-" * 20)

        if mainChoice == "1":
            player.makeMove()
            player.attack(enemy)

        elif mainChoice == "2":
            if not player.inventory:
                print("utrata tury!")
                pass
            else:
                print("zawartosc plecaka")
                for idx,item in enumerate(player.inventory,start = 1):
                    print(f"[{idx}] {item}")
                print("[0] Anuluj (powrót)")
                try:
                    choice = int(input("Podaj numer przedmiotu"))
                    if choice == 0:
                        print("anulowano,tracisz ture!")
                        pass
                    elif 1 <= choice <= len(player.inventory):
                        selectemItem = player.inventory[choice-1]
                        selectemItem.use(player)

                        if(isinstance(selectemItem,Potion)):
                            player.dropItem(selectemItem)
                            print("mikstura zostala usunieta")
                    else:
                        print("Nie ma takiego przedmiotu!")
                except ValueError:
                    print("musisz wpisac cyfre")

        elif mainChoice == "3":
            print(f" 🏃‍♂️ {player.name} ucieka w popłochu z pola walki!")
            break
        else:
            print("nieznana opcja")
        if not enemy:
            print(f"{enemy} zostal pokonany")

            break;

        time.sleep(1)

        #zmiana tury


        if not player:
            print(f"{player} zostal pokonany")
            break
        enemy.makeMove()
        enemy.attack(player)

        time.sleep(1)


gameHandle(player)
