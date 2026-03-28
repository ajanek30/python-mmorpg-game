# Wędrując przez Labirynt Abstrakcji, natrafiasz na lśniącą podstawkę.
# Spoczywa na niej legendarny "Dzbanuszek Modulacji AM".
# Tuż obok wisi w powietrzu ciężka, niematerialna "5 z SiSU".
# Twoim zadaniem będzie zabranie obu przedmiotów.

# Aby móc zabrać dzbanuszek, musisz nauczyć się podnosić materialne przedmioty
# W tym celu uzupełnij klasę Lootable(Mixin), która definiuje metodą pick_up
# Pamiętaj: Mixin nie powinien definiować własnego stanu (__init__),
# ma jedynie dostarczać nową umiejętność!

#5 z SiSu jest niematerialna, musisz podnieść ją bez udziału LootableMixin()



class LootableMixin:
    ...
    def pickUpBy(...):
        print(f"{player_name} podnosi przedmiot!")


class AncientRelic(...):
    name = "Dzbanuszek Modulacji AM"

class SisuGrade:
    name = "5 z SiSU"

relic = ...
grade = SisuGrade()

relic ...

print(f"Gratulacje! Zdobyłeś: {relic.name}")


grade.pickUpBy(...) #Kod powinien wyrzucić błąd
#Nie oszukujmy się nawet w grach nie wszystko jest możliwe 
