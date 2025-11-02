x = float(input('Podaj pierwszą  liczbę (x):'))
y = float(input('Podaj drugą  liczbę (y):'))
z = float(input('Podaj trzecią  liczbę (z):'))

if x > y:
    x, y = y, x
elif x > z:
    x, z = z, x
elif y > z:
    y, z = z, y
else:
    print('napisz numer')

print(x, y, z)