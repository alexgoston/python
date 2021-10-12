import random

tömegek = []
for _ in range(20):
    tömegek.append(random.randint(1000,10000))

print(tömegek)

volt_nehéz = False
nehezek_száma = 0
össztömeg = 0
nehezek_össztömege = 0
for tömeg in tömegek:
    össztömeg = össztömeg + tömeg
    if tömeg > 9300:
        volt_nehéz = True
        nehezek_száma += 1
        nehezek_össztömege += tömeg 

if volt_nehéz:
    print('Volt 9300 kg-nál nehezebb jármű.')

print(nehezek_száma, '9300 kg-nál nehezebb jármű volt.')