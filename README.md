###JPWP### 
MMORPG game implementing advanced aspects of multi inheritance
and classes

#todo!
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
