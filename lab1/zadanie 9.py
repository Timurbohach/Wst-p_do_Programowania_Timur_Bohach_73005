a = int(input('ile masz lat'))
if a < 4:
    print('wstęp jest bezpłatny')

elif a > 4 and a < 18:
    print('bilet kosztuje 10zł')

elif a >= 18:
    b = input('czy jestesz studentem')
    if b =='tak':
        print('masz 25% zniżką')
    elif b == 'nie':
        print('bilet kosztuje 20zł')


