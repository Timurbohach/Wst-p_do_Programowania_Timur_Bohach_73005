zdanie = input('Wpisz jakieś zdanie: ')
print(zdanie)

alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'm']
lb_w = [0] * len(alfabet)


for znak in zdanie.lower():
    print(f'Sprawdza znak: {znak}')
    for i in range(len(alfabet)):
        print('Czy jest to litera:', alfabet[i])
        if znak == alfabet[i]:
            lb_w[i] += 1
            break

print("Liczba wystąpień liter:", lb_w)

lista_slow = zdanie.split()
print("Lista słów:", lista_slow)

print("\nSłowa z dużą pierwszą i ostatnią literą:")

for slowo in lista_slow:
    if len(slowo) == 1:
        nowe = slowo.upper()
    else:
        nowe = slowo[0].upper() + slowo[1:-1] + slowo[-1].upper()

    print(nowe)

