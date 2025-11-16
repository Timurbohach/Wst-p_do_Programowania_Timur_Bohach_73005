tekst = input("Podaj ciąg znaków: ")

czysty = tekst.replace(" ", "").lower()

if czysty == czysty[::-1]:
    print("To jest palindrom.")
else:
    print("To nie jest palindrom.")
