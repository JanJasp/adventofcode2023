def find_first_and_last_numbers(input_liste):
    zahl = [item for item in input_liste if type(item) in (int, float)]
    letters = [item for item in input_liste if isinstance(item, str) and item.isalpha()]
    
    return zahl[:1] + zahl[-1:]


gegebene_liste = []
first_number, last_number = find_first_and_last_numbers(gegebene_liste)
ergebnis = first_number + last_number


print("Ergebnis:", ergebnis)
