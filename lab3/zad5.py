
lista_zakupow ={'chleb': 7, 'maslo':8, 'ciastka':10, 'pepsi':6,'ser':10, 'somarek':10}


print(lista_zakupow)
print(lista_zakupow['chleb'])
print(lista_zakupow.keys())
print(lista_zakupow.values())
print(lista_zakupow.items())


suma=0
for i in lista_zakupow.values():
    suma += i
print(suma)

for k, v in lista_zakupow.items():
    print(k, v)