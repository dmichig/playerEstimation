import csv

with open('players_20.csv', encoding='utf8') as data:
    players = csv.reader(data, delimiter=',')

    line_number = 0
    for a in players:
        if line_number == 0:
            column_names = a
            line_number += 1
    for b in column_names:
        print(b)
        if b == 'overall' || wszystkie pozostale potrzebne kategorie (dla bramkarzy te z gk)(dla reszty normalne z karty)(dla wszystkich overall plus cena):
            print(b)