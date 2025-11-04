lb_w = int(input("Podaj liczba lub wierszy: "))
#A________________________________________________________________________
# for i in range(lb_w):
#     for j in range(lb_w):
#         print('*',  end=' ')
#     print('')

#B_______________________________________________________________________
# for i in range(lb_w):
#     for j in range(lb_w-(lb_w-(i+1))):
#         print('*',  end=' ')
#     print('')


#C_______________________________________________________________________

for i in range(lb_w):
    for j in range(lb_w-(lb_w-(i+1))):
        print('*',  end=' ')
    print('')
    for j in range(lb_w+1):
        print('*',  end=' ')