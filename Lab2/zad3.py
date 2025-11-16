n = int(input("Podaj liczbę elementów ciągu (n): "))
a = float(input("Podaj pierwszy wyraz ciągu (a): "))
r = float(input("Podaj różnicę ciągu (r): "))

for i in range(n):
    elem = a + i * r
    print(elem)
