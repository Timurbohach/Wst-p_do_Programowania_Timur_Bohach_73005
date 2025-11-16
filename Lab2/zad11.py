a = int(input("Podaj pierwszą liczbę całkowitą: "))
b = int(input("Podaj drugą liczbę całkowitą: "))


mniejsza = min(a, b)
wieksza = max(a, b)


for i in range(mniejsza, wieksza + 1):

    if i % 2 != 0:
        continue

    print(i)