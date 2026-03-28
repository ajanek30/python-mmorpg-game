
# W Królestwie Obiektowości każdy nowicjusz zaczyna jako zwykły Bohater.
# Niestety, na opancerzone gobliny z północy to nie wystarczy!
# Mistrz Broni zlecił Ci wyszkolenie elity – klasy Warrior.
# Wojownik pamięta podstawy walki, ale uczy się też zadawać dodatkowe,
# brutalne obrażenia.
#
#
# Stworz klase pochodną Warrior
# dziedzicząc atrybuty konstruktora klasy Hero
# Dodaj atrybut warriorDamageBonus
# Stworz obiekt wojownika(i uzupełnij jego 3 pola konstruktora)

class Hero:
    def __init__(self, hp, damage):
        self.hp = hp
        self.damage = damage
        print(f'Bohater posiada: {self.hp} HP oraz zadaje: {self.damage} DMG.')


class ________(________):
    def __init__():


        print(f'Dodatkowo wojownik ma bonus: {________}')


woj1 = ________(100, 50, 30)


print(f"Całkowite obrażenia wojownika: {woj1.damage + woj1.warriorDamageBonus}")

# Jeśli w konsoli zobaczysz komunikaty o HP, bonusie, a na końcu sumę 80 obrażeń,
# to znaczy, że poprawnie wyszkoliłeś swojego wojownika!