import csv

with open('playlist.csv') as zenék:
    csv_olvasó = csv.reader(zenék, delimiter=',')
    line_count = 0
    for oszlop in zenék:
        if line_count == 0:
            print("Előadó; Zene címe; Műfaj; Hossz")
            line_count += 1
        else:
            print(f'\tElőadó: {oszlop[0]} Zene címe: {oszlop[1]} Műfaj: {oszlop[2]} Hossz: {oszlop[3]}')
            line_count += 1
    print(f'{line_count} sor feldolgozva.')