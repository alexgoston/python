auto = input('Egy autónév rendel! ')
vegsebesseg = int(input('Egy autó végsebesség rendel! '))
orszag = input('Hol készül a(z) ' + auto + '? ')

#str
mondat1 = orszag + ' vidékein készül a(z) ' + auto + ', ami ' + str(vegsebesseg) + ' km/h végsebességre képes.'
print(mondat1)

#str nélkül
mondat2 = '{} vidékein készül a(z) {}, ami {} km/h végsebességre képes.' .format(orszag, auto, vegsebesseg)
print(mondat2)

#rendezve számokkal
mondat3a = '{0} vidékein készül a(z) {1}, ami {2} km/h végsebességre képes.' .format(orszag, auto, vegsebesseg)
mondat3b = '{1} vidékein készül a(z) {2}, ami {0} km/h végsebességre képes.' .format(vegsebesseg, orszag, auto)
print(mondat3a)
print(mondat3b)

#rendezve betűkkel
mondat4 = '{o} vidékein készül a(z) {a}, ami {v} km/h végsebességre képes.' .format(o=orszag, a=auto, v=vegsebesseg)
print(mondat4)

#f-strinh
mondat5 = f'{orszag} vidékein készül a(z) {auto}, ami {vegsebesseg} km/h végsebességre képes. '
print(mondat5)





auto2 = input('Még egy autó ')