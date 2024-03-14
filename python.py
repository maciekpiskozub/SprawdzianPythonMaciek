with open('napisy.txt', 'r') as plik:
    napisy = plik.readlines()

# do pudpunktu a)
napisy_parzyste = 0

# do podpunktu b)
zera_1 = 0
jedynki_1 = 0
zera_i_jedynki = 0

# do podpunktu c)
zera_2 = 0
jedynki_2 = 0

# do podpunktu d)
napisy_konczace_sie_na_1 = 0

# do podpunktu e)
palindromki = 0



# a)
for napis in napisy:
    if len(napis) %2 == 0:
        napisy_parzyste += 1

# b)
for napis in napisy:
    if '1' in napis:
        jedynki_1 += 1

    if '0' in napis:
        zera_1 += 1

    if zera_1 == jedynki_1:
        zera_i_jedynki += 1

# c)
for napis in napisy:
    if '1' not in napis:
        zera_2 += 1
    elif '0' not in napis:
        jedynki_2 += 1

# d) (cos sie zrypalo nie wiem co)
for napis in napisy:
    if napis[-1] == '1':
        napisy_konczace_sie_na_1 += 1

# e)
for napis in napisy:
    for i in range(len(napis)):
        if(napis[i] == napis[i - 1]):
            palindromki += 1

# f) przerasta moje umiejetnosci + niestarczylo mi czasu ;\\\\\\\\\\






print("a) Ilosc napisow o parzystej dlugosci:", napisy_parzyste)
print("b) Liczba napisow z taka sama liczba zer i jedynek to:", zera_i_jedynki)
print("c) Liczba napisow zawierajacych same jedynki to: ", jedynki_2, " ,a ilość napisów zawierającyh same zera to: ", zera_2)
print("d) Ilosc napisow okonczacych sie na 1 to :", napisy_konczace_sie_na_1)
print("e) Ilosc palindromow wynosi: ", palindromki)



# Zapisywanie wynikow w pliku wynik.txt
with open('wynik.txt', 'w') as wynik:
    wynik.write(f"a): {napisy_parzyste}\n")
    wynik.write(f"b): {zera_i_jedynki}\n")
    wynik.write(f"c(jedynki, zera)): {jedynki_2} {zera_2}\n")
    wynik.write(f"d): {napisy_konczace_sie_na_1}\n")
    wynik.write(f"e): {palindromki}\n")










