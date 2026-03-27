#Podstawowe tworzenie klas z dziedziczeniem w pythonie
class A:
    def process(self): print("Klasa A")

class B(A):
    def process(self): print("Klasa B")

class C(A):
    def process(self): print("Klasa C")

class D(B, C):
    pass

print(D.__mro__) #__mro__ pozwala sprawdzić hierarchię dziedziczenia klas
obiekt = D()
obiekt.process()

