# ASD_Lista5

Program napisany w wersji pythona 3.10.9

wariant D - księżniczka

Wariant D „ Księżniczka”
Król ASD-Landii zamierza wydać za mąż swą urodziwą córkę, księżniczkę ASDelle. Zapytał ja,
jakiego męża chciałaby mieć. Księżniczka odpowiedziała, że jej przyszły małżonek powinien być
mądry, a także ani skąpy, ani rozrzutny. Zamyślił się król nad tym, jakim to próbom powinni być
poddani kandydaci na męża, aby mógł wybrać dla swej córki najlepszego z nich. Po długich
dumaniach stwierdził, że najlepiej posłuży do tego zamek, który kazał był wybudować ku uciesze
mieszkańców ASD-Landii. Zamek składa się z dużej liczby komnat, w których zgromadzono
bogactwa królestwa. Komnaty te, połączone korytarzami, mogą by zwiedzane przez poddanych w
celu podziwiania wystawionych w nich wspaniałości. Za zwiedzenie komnaty trzeba uiścić pewną
liczbę asdolów (asdol jest jednostką pieniężną ASD-Landii). Zwiedzanie zamku rozpoczyna się od
komnaty wejściowej. Król wręczył sakiewkę każdemu kandydatowi na męża księżniczki. W każdej
sakiewce była taka sama liczba asdolów. Poprosił każdego kandydata, aby ten wybrał tak drogę,
która pozwoli, poczynając od komnaty wejściowej, odwiedzić pewną liczbę komnat zamku oraz
zakończy zwiedzanie w komnacie, w której przebywa księżniczka, i wyda przy tym dokładnie
kwotę, jaka była w sakiewce. Rozrzutni kandydaci, którzy wydawali po drodze zbyt dużo, nie
docierali do komnaty księżniczki, skąpi natomiast zjawiali się z niepustą sakiewką i księżniczka
wyprawiała ich w dalszą drogę celem opróżnienia sakiewki. Niestety do dziś żadnemu z
kandydatów nie udało się sprostać zadaniu króla, a księżniczka ASDella wciąż z utęsknieniem
czeka na swój ideał. Zaproponuj możliwie najefektywniejszy algorytm, który:
• wczyta z pliku tekstowego opis zamku, numer komnaty, w której znajduje się księżniczka i kwotę
w sakiewce,
• wyznaczy ciąg komnat, przez które należy kolejno przejść, aby dojść z komnaty wejściowej do
komnaty, w której znajduje się księżniczka i wydać dokładnie całą zawartość sakiewki,
• zapisze znalezioną drogę w pliku tekstowym.
Zakładamy, że droga zawsze istnieje. Jeśli istnieje wiele takich dróg, to Twój algorytm powinien
wyznaczyć dowolną z nich.
Wejście: W pierwszym wierszu pliku tekstowego zapisanych jest pięć dodatnich liczb całkowitych
n, m, w, k, s, 1 <= n <= 100 , 1 <= m <= 64950 , 1 <= w, k <= n, 1 <= s <= 1000, pooddzielanych
pojedynczymi odstępami. Liczba n jest równa liczbie komnat, a m liczbie korytarzy. Komnaty są
ponumerowane od 1 do n. Liczba w jest numerem komnaty wejściowej, a k numerem komnaty, w
której znajduje się księżniczka. Liczba s określa liczbę asdolów w sakiewce. W drugim wierszu
zapisanych jest n dodatnich liczb całkowitych o1, o2, . . . , on, 1 <= oi <= 1000, pooddzielanych
pojedynczymi odstępami. Liczba oi jest równa opłacie za (każdorazowy) wstęp do komnaty nr i. W
kolejnych m wierszach zapisane są po dwie dodatnie liczby całkowite x, y, x <= y, 1 <= x, y <= n,
oddzielone pojedynczym odstępem. Każda taka para x, y określa, że komnaty o numerach x i y są
połączone korytarzem.
Wyjście: Twój program powinien w pierwszym (i jedynym) wierszu pliku tekstowego zapisać ciąg
dodatnich liczb całkowitych, pooddzielanych pojedynczymi odstępami, określający numery
kolejnych komnat, przez które należy przejść, aby dojść z komnaty wejściowej do komnaty, w
której znajduje się księżniczka, i wyda dokładnie całą zawartość sakiewki.

Przykład:
Plik wejściowy:
5 6 3 4 9
1 2 3 4 5
2 4
5 4
1 5
1 2
2 3
3 1
Plik wyjściowy:
3 2 4
