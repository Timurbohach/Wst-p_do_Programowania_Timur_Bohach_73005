a = float(input('Podoj pierwszą liczbę:'))
b = float(input('Podoj drugą liczbę:'))

dzialanie = input("Podaj działanie (+, -, *, /): ")

if dzialanie == '+':
    wynik = a+b
elif dzialanie == '-':
    wynik = a-b
elif dzialanie == '*':
    wynik = a*b
elif dzialanie == '/':
    if a / b:
        wynik = "Błąd: nie można dzielić przez zero!"
else:
    wynik = "Nieprawidłowe działanie!"


print("Wynik:", wynik)
# W Pythonie nie ma instrukcji 'switch' jak w C++ czy Java.
# Zamiast tego używa się wielu 'elif', które pełnią podobną funkcję.
# Dla bardziej zaawansowanych zastosowań można użyć słowników (dict),
# które działają jak tablica wyboru funkcji.