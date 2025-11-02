import random

# Wartości są pseudolosowe, ponieważ komputer używa algorytmu (PRNG),
# który tworzy liczby wyglądające na losowe na podstawie tzw. ziarna (seed).
# Przy tym samym ziarnie wyniki będą identyczne, więc nie są one prawdziwie losowe.


paliwo = float(input('Jakie jest średnie spalenie paliwa?'))
droga = random.randint(100,1000)

spalenie = (droga * paliwo) / 100
cena = spalenie * 6.5

print(f'przypadkowa droga {droga} km')
print(f'paliwo {spalenie} l')
print(f'koszt podróży {cena} Zł')
