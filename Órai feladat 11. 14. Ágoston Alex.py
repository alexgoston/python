#példák a videókból
#1
diák = ["Kiss", "Péter", "10.A", 17, True, False]
print(diák[3])
diák = {
    "vezetéknév": "Kiss",
    "keresztnév": "Péter",
    "osztály": "10.A",
    "életkor": "17",
    "kollégista": True,
    "info_fakt": False,
    "matek_jegyek": [5, 4, 4, 3, 5, 5]
}
print(diák["életkor"])

#2
raktár = {
    114589: "Dominó polc",
    264875: "Student íróasztal",
    364879: "Kényelem01 fotel",
    568974: "Family étkezőasztal 6 fős"
}
print(raktár)

#üres szótár létrehozása
raktár = {}
print(raktár)

#adatokkal teli lista létrehozása
diák = {
    "vezetéknév": "Kiss",
    "keresztnév": "Péter",
    "osztály": "10.A",
    "életkor": "17",
    "menza": True
}
print(diák["életkor"])
print(diák.get("életkor"))
diák["szakkör"] = True
print(diák)
for kulcs in diák:
    print(kulcs, diák[kulcs])
print(diák.values())
for érték in diák.values():
    print(érték)
print(diák.items())
for kulcs, érték in diák.items():
    print(kulcs, érték)



#példák a "példák" oldalról
# üres szótár létrehozása
raktar = {}
print(raktar)

# szótár létrehozása adatokkal 
diak = {
  'vezeteknev': 'Kiss',
  'keresztnev': 'Péter',
  'eletkor': 17,
  'menza': True
}

# szótár elemeinek elérése kulcs alapján
print(diak['eletkor'])
#print(diak.get('eletkor'))
# nem létező kulcsra való hivatkozás -> KeyError
# print(diak['osztaly'])
# nem létező kulcsra hivatkozunk a .get metódussal, 
# ilyenkor a megadott alapértékkel tér vissza
print(diak.get('kollegista', 'nem'))
# ellenőrzés, hogy létezik-e a kulcs
print('keresztnev' in diak)
# érték módosítása
diak['eletkor'] = 21
print(diak['eletkor'])
# még nem létező kulcs megadása értékkel
diak['osztaly'] = '10.A'
# kulcs-érték törlése
del diak['vezeteknev']
for kulcs in diak:
    print(kulcs, diak[kulcs])
for ertek in diak.values():
    print(ertek)
for kulcs, ertek in diak.items():
    print(kulcs, ertek)
    