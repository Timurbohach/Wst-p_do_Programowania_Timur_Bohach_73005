import random


a = random.randint(3, 7)
b = random.randint(3, 7)

X = set(random.randint(0, 10) for i in range(a))
Y = set(random.randint(0, 10) for j in range(b))

print("Zbiór X:", X)
print("Zbiór Y:", Y)


print(" Czy X zawiera liczbę 5?", 5 in X)

print(" Czy X jest podzbiorem Y?", X.issubset(Y))

print(" Czy Y jest podzbiorem X?", Y.issubset(X))

print(" Suma X ∪ Y:", X.union(Y))

print(" Różnica X - Y:", X.difference(Y))

print(" Różnica Y - X:", Y.difference(X))

print(" Iloczyn X ∩ Y:", X.intersection(Y))


max_X = max(X) if X else None
max_Y = max(Y) if Y else None
print(" Najwyższy element w X:", max_X)
print(" Najwyższy element w Y:", max_Y)

if X:
    elem = next(iter(X))
    X.remove(elem)
    Y.add(elem)
    print(f" Przeniesiono element {elem} ze zbioru X do Y")

print("X po operacji i):", X)
print("Y po operacji i):", Y)


Y.update(X)
print(" Po skopiowaniu X do Y:")
print("X:", X)
print("Y:", Y)

X.clear()
Y.clear()

print(" Po wyczyszczeniu:")
print("X:", X)
print("Y:", Y)
