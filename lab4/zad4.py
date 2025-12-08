def oblicz_bmi(waga, wzrost):
    bmi = waga / (wzrost ** 2)
    print("Twoje BMI:", bmi)
    if bmi < 18.5:
        print("Niedowaga")
    elif bmi < 25:
        print("Waga prawidłowa")
    elif bmi < 30:
        print("Nadwaga")
    else:
        print("Otyłość")

waga = float(input("Podaj wagę (kg): "))
wzrost = float(input("Podaj wzrost (m): "))

oblicz_bmi(waga, wzrost)
