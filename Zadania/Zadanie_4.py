# W Królestwie Obiektowości nastały trudne czasy. Podstępne gobliny z klanu Cyberki
# próbują wkraść się do Królewskiego Skarbca i zadłużyć królestwo, wpisując tam ujemne wartości!
# Jako Nadworny Mag Architektury, zostałeś poproszony o rzucenie zaklęcia Enkapsulacji.
# Musisz ukryć prawdziwe złoto przed światem zewnętrznym i stworzyć magiczne wrota,
# które wpuszczą tylko wartości dodatnie.

#Spróbuj dostać się do prywatnego atrybutu
#za pomocą gettera i settera
#Na początku w konstruktorze skorzystaj z settera
#ktory sprawdza czy wartosc mu przekazana jest wieksza od 0
#jesli nie -> ma byc 0

#Dodatkowo dostań się do wartości skarbca, za pomocą enkapsulacji

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