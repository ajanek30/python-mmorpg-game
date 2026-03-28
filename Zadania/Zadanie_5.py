# Dzielny wojowniku dotarłęś do granicy Królestwa Obiektowości pora abyś
# stworzył swoje własne królestwo!!
# Jesli chcesz podjac wyzwanie sam sprobuj rozwiazac

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
#rozpocznij
#gre
#tutaj!

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
