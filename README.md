###JPWP### 
MMORPG game implementing advanced aspects of multi inheritance
and classes

#todo!
1. Interaktywne menu walki (Zamiast automatu)
Aktualnie walka rozgrywa się sama w ułamku sekundy, a my tylko czytamy logi.

Co dodać: Funkcję input(), która w każdej turze pyta gracza, co chce zrobić.

Jak to zmieni grę: Zamiast samego entity1.attack(), gracz dostanie menu:
Wybierz akcję: [1] Zwykły atak | [2] Atak Specjalny (kosztuje Manę/Staminę) | [3] Wypij miksturę | [4] Ucieczka

Czego to uczy: Zarządzania pętlą gry (tzw. Game Loop), walidacji danych wprowadzanych przez użytkownika (co jeśli wpisze literę zamiast cyfry?) oraz obsługi błędów (try-except).

2. Prawdziwe Przedmioty (Wzorzec Kompozycji)
Teraz Twój ekwipunek przechowuje tylko tekst ("mieczyk"). To dobre na start, ale string nie może zadać obrażeń.

Co dodać: Zupełnie nowe klasy dla przedmiotów. Główną klasę Item i dziedziczące po niej np. Weapon i Potion.

Jak to zmieni grę: Zamiast pisać addItem("mieczyk"), zrobisz addItem(Weapon("Excalibur", damageBonus=15)). Kiedy wojownik założy ten miecz, jego funkcja attack() dynamicznie doliczy +15 do obrażeń. Kiedy użyje Potion("Leczenie", healAmount=30), wywoła się Twój HealingMixin.

Czego to uczy: Tzw. Kompozycji w programowaniu obiektowym – czyli sytuacji, w której jeden złożony obiekt (Bohater) posiada wewnątrz siebie inne obiekty (Bronie).

3. System Doświadczenia (XP) i Awansowania
Zabicie wroga kończy grę. A co, gdybyśmy chcieli zabić ich pięciu z rzędu?

Co dodać: Atrybut _xp i _xpToNextLevel w klasie Hero. Po śmierci potwora (w lifeChecker), wróg przekazuje swoje punkty XP bohaterowi.

Jak to zmieni grę: Jeśli wojownik zbierze 100 XP, wywoła się metoda levelUp(), która podniesie jego .level o 1, w pełni zregeneruje jego HP i powiększy .maxHp.

Czego to uczy: Tworzenia powiązań między zdarzeniami (śmierć obiektu A wywołuje zmianę w obiekcie B) i skalowania trudności (matematyka w kodzie).

4. Zapisywanie i Wczytywanie Stanu Gry (Bazy Danych / Pliki)
Prawdziwe aplikacje nie tracą danych po wyłączeniu konsoli.

Co dodać: Dwie metody, które na żądanie gracza "zamrożą" stan jego bohatera i zapiszą go na dysku.

Jak to zmieni grę: Używając wbudowanej biblioteki json, będziesz mógł zapisać parametry bohatera (HP, level, klasa, ekwipunek) do pliku tekstowego save.json. Przy kolejnym uruchomieniu gry, program najpierw zapyta: "Chcesz stworzyć nowego bohatera, czy wczytać zapis?".

Czego to uczy: Operacji Wejścia/Wyjścia (I/O), serializacji obiektów (zamiany obiektu Pythona na tekst) i pracy z formatem JSON, który jest używany do komunikacji w niemal każdym współczesnym systemie IT.
