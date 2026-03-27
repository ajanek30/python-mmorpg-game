# Wędrując przez Labirynt Abstrakcji, natrafiasz na lśniącą podstawkę.
# Spoczywa na niej legendarny "Dzbanuszek Modulacji AM".
# Tuż obok wisi w powietrzu ciężka, niematerialna "5 z SiSU".
# Aby móc go zabrać, musisz stworzyć uniwersalną "Domieszkę" (Mixin),
# która pozwoli każdemu przedmiotowi stać się "podnoszalnym".
# Pamiętaj: Mixin nie powinien definiować własnego stanu (__init__),
# ma jedynie dostarczać nową umiejętność!

class LootableMixin:
    def pick_up(...):
        print(f"{player_name} podnosi przedmiot!")


class AncientRelic(...):
    name = "Dzbanuszek Modulacji AM"

class SisuGrade:
    name = "5 z SiSU"

relic = ...
grade = SisuGrade()

relic ...

print(f"Gratulacje! Zdobyłeś: {relic.name}")


grade.pick_up(...) #Kod powinien wyrzucić błąd
#Nie oszukujmy się nawet w grach nie wszystko jest możliwe 
