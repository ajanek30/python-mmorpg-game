class Base:
    def __init__(self): print("Inicjalizacja Base")

class Left(Base):
    def __init__(self):
        print("Inicjalizacja Left")
        super().__init__()

class Right(Base):
    def __init__(self):
        print("Inicjalizacja Right")
        super().__init__()

class Child(Left, Right):
    def __init__(self):
        print("Inicjalizacja Child")
        super().__init__()

print(Child.__mro__)
obiekt = Child()

#Wynik kodu:
#(<class '__main__.Child'>, <class '__main__.Left'>,
#<class '__main__.Right'>, <class '__main__.Base'> ...)
#Inicjalizacja Child
#Inicjalizacja Left
#Inicjalizacja Right
#Inicjalizacja Base

