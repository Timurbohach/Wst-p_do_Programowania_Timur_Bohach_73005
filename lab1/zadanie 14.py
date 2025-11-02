plik = input('podaj nazwę pliku:')

if plik.endswith('.xls') or plik.endswith('.xlsx'):
    print('Ten plik jest arkusza Exele')
else:
    print('To ne jest plik Exele')

# Metoda endswith() służy do sprawdzania, czy napis (string)
# kończy się określonym ciągiem znaków.
# Zwraca wartość True (prawda) lub False (fałsz).
# Przykład:
# "plik.xlsx".endswith(".xlsx") → True