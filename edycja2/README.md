## [\#wyzwaniepython](http://www.wykop.pl/tag/wyzwaniepython/) Zadanie 02

W ankiecie wygrała propozycja **nr 1.** i nad tym zadaniem będziemy pracować przez
następny tydzień:

### Łatwa
Rekurencyjne wyszukiwanie plików w danym katalogu i zrobienie histogramu w
osobnym pliku tekstowym z częstotliwością (tzn. informacją jaką część
wszystkich plików są pliki z danym rozszerzeniem) występowania plików z danym
rozszerzeniem oraz sumą ich rozmiarów.

#### Wymagania:
 - odpowiednie formatowanie: kolumny wyrównanie do prawej strony, pierwsza
   o szerokości 5 znaków, druga 15, trzecia 60 (w trzeciej 10 spacji przed
   pierwszym znakiem `#`)
 - katalog jak i nazwa pliku wyjściowego muszą być przyjmowane jako
   argumenty programu (ułatwi to testowanie):
       `./prog nazwa_katalogu nazwa_pliku_wyjsciowego`
 - rozmiar podajemy w bajtach, po rozszerzeniu
 - histogram ma składać się ze znaków `#` i ma mieć szerokość 50 znaków,
   czyli jeśli w katalogu występują wyłącznie pliki z rozszerzeniem .txt,
   obok tego rozszerzenie, po sumie rozmiarów tych plików, ma się znaleźć
   50 znaków '#'.

#### Przykład
Załóżmy, że w podanym katalogu znajduje się 12 plików:
```
6 z rozszerzeniem  .txt o rozmiarze    5932B
3 z rozszerzeniem .jpeg o rozmiarze   10000B
2 z rozszerzeniem  .mp3 o rozmiarze  203151B
1 z rozszerzeniem  .zip o rozmiarze   43131B
```

Rozwiązanie powinno zapisać do podanego pliku następujące dane(bez pierwszej
linii, służy ona jedynie przedstawieniu szerokości kolumn, 5-15-60):

```
#####***************%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  txt          5932B                                   #########################
 jpeg         10000B                                               #############
  txt        203151B                                                    ########
  zip         43131B                                                        ####
```

### Trudna
~~Zapisanie danych o plikach z danego katalogu do bazy danych (takie dane jak
ścieżka, rozmiar, rozszerzenie, data modyfikacji). Moglibyśmy to rozbudować o
sprawdzanie, czy pliki i podkatalogi danego katalogu zmieniły się od ostatniego
zapisu do bazy - nawet poza #wyzwaniepython ;-). Do ustalenia schemat bazy.~~

===

### Przydatne biblioteki:
* SQLAlchemy

### Czas na wykonanie
**1 tydzień, do 27.07.2016**

===

Tak jak poprzednio, prosimy o niepublikowanie wcześniej rozwiązań, ale
zachęcamy do pytania o pomoc w tagu [#wyzwaniepythonpomoc](http://www.wykop.pl/tag/wyzwaniepythonpomoc/)
(jeśli coś jest dla Was niejasne w treści zadania, pytajcie i o to).

### Linki:
* [Spam lista](http://mirkolisty.pvu.pl/list/qIRpnpHg3WM8YOv5)


## Powodzenia!
