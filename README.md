###JPWP### 
MMORPG game implementing advanced aspects of multi inheritance
and classes

#todo!

4. Zapisywanie i Wczytywanie Stanu Gry (Bazy Danych / Pliki)
Prawdziwe aplikacje nie tracą danych po wyłączeniu konsoli.

Co dodać: Dwie metody, które na żądanie gracza "zamrożą" stan jego bohatera i zapiszą go na dysku.

Jak to zmieni grę: Używając wbudowanej biblioteki json, będziesz mógł zapisać parametry bohatera (HP, level, klasa, ekwipunek) do pliku tekstowego save.json. Przy kolejnym uruchomieniu gry, program najpierw zapyta: "Chcesz stworzyć nowego bohatera, czy wczytać zapis?".

Czego to uczy: Operacji Wejścia/Wyjścia (I/O), serializacji obiektów (zamiany obiektu Pythona na tekst) i pracy z formatem JSON, który jest używany do komunikacji w niemal każdym współczesnym systemie IT.
