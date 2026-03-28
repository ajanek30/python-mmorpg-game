#stworz klase pochodną Warrior
#dziedzicząc atrybuty konstruktora klasy Hero
#dodaj atrybut warriorDamageBonus
#stworz obiekt wojownika(i uzupełnij jego 3 pola konstruktora)
#sprawdz czy całkowite zostały powiększone
class Hero:
    def __init__(self,hp,damage):
        self.hp = hp
        self.damage = damage
        print(f'bohater posiada: {self.hp} oraz zadaje: {damage}')
class ...:
    def __init__(...)
        ...
        print(f'Dodatkowo warrior ma bonus: {}')
woj1 = ...(100,50,30)
print(f"Całkowite obrażenia wojownika: {woj1.damage + woj1.warriorDamageBonus}")

################################

#spróbuj dostać się do prywatnego atrybutu
#za pomocą gettera i settera

#najpierw w konstruktorze skorzystaj z settera
#ktory sprawdza czy wartosc mu przekazana jest wieksza od 0
#jesli nie -> ma byc 0

#dodatkowo dostań się do wartości skarbca, za pomocą enkapsulacji

class Skarbiec:
    def __init__(self,stanPoczatkowy):
        self.(...nazwa_settera...) = stanPoczatkowy

    ...
    #tu 2 metody
    #pamietaj o uzyciu "_" w nazwie ukrytego atrybutu
    ...

sk = Skarbiec(1000)
print(sk.stanSkarbca)
sk.stanSkarbca = -100
print(sk.stanSkarbca)

# jesli chcesz podjac wyzwanie sam sprobuj rozwiazac
# -> ps. na dole sa podpowiedzi dla opornych

from abc import ABC, abstractmethod
import random


# 1. Stwórz HealingMixin do leczenia

# 2. Stwórz Klase Abstrakcyjna Entity

# 3. Stwórz Klasy pochodne Warrior oraz Monster - załóż że możemy leczyć tylko Warriora

# 4. Funkcja walki
def symulacja_walki(p1, p2):
    print(f"--- WALKA ROZPOCZĘTA: {type(p1).__name__} vs {type(p2).__name__} ---")

    ...
    petla

    # Szansa na uleczenie wojownika (jeśli ma Mixin)
    if isinstance(p1, HealingMixin) and p1.hp < 30:
        p1....(15)

    # atakowanie
    p2....(p1)
    print(f"STATUS: P1({p1.hp} HP) | P2({p2.hp} HP)\n")


zwyciezca = p1 if p1.hp > 0 else p2
print(f"🏆 KONIEC! Zwyciężył: {type(zwyciezca).__name__}")

# --- START ---
wojownik = Warrior(random.randint(80, 120), random.randint(15, 25))
potwor = Monster(random.randint(70, 110), random.randint(10, 30))

...
rozpocznij
gre
tutaj!

# w Mixinie stworz metode lecz, która przyjmie wartość, o którą
# atrybut hp zostanie powiększony

# Entity(abstrakcyjna) - definiuje hp i damage
# pamietaj o setterach i getterach oraz metodzie abstrakcyjnej atak(cel)
# sprawdz czy wartosc hp jest > 0

# klasy pochodne powinny implementowac metode abstrakcyjną atak(cel)
# a takze cel powinien otrzymać damage

# stworz petle while, która działa póki hp jednego i drugiego
# obiektu > 0
# ulecz za pomocą obiekt.lecz(15)
# atakuj za pomocą obiekt.atak(drugiObiekt)


#############################