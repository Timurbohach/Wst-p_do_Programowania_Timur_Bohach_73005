n = int(input('Podaj liczbę (n):'))

elem = 1

for i in range(1, n + 1):
    elem *= i
print("Silnia =", elem)
