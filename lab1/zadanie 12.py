x = float(input("Podaj wartość x: "))
funkcja = input("Wybierz funkcję (a, b, c): ")

if funkcja == 'a':
    if x > 0:
        wynik = 2 * x
    elif x == 0:
        wynik = 0
    else:
        wynik = -3 * x


elif funkcja == "b":
    if x >= 1:
        wynik = x ** 2
    else:
        wynik = x


elif funkcja == "c":
    if x > 2:
        wynik = 2 + x
    elif x == 2:
        wynik = 8
    else:
        wynik = x - 4

else:
    print('Nieprawidłowy wybór funkcji')

print('Wynik:', wynik)


