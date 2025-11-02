import math

a = float(input('Podaj liczbę a:'))
b = float(input('Podaj liczbę b:'))
c = float(input('Podaj liczbę c:'))

if a == 0:
    print('to nie jest równanie kwadratowe')
else:
    des = b ** 2 - 4*a*c

    if a > 0:
        x1 = (-b - math.sqrt(des)) / (2 * a)
        x2 = (-b + math.sqrt(des)) / (2 * a)
        print(f'Dwa pierwiastki rzeczywiste x1 = {x1:.2f}, x2 = {x2:.2f}')
    elif des == 0:
        x0 = -b / (2 * a)
        print(f'Jeden pierwiastek podwójny x = {x0:.2f}')
    else:
        print('Brak pierwiastków rzeczywistych (delta < 0)')




