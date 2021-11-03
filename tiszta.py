a = "Hello"
b = "World"
c = a + b
print(a, b)

primek = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
p4 = primek[4]
print(p4)

gyumolcs = "banán"
hossz = len(gyumolcs)
print(hossz)

i = 0
while i < len(gyumolcs):
    karakter = gyumolcs[i]
    print(karakter)
    i += 1

for c in gyumolcs:
    print(c)

elotag = "törp"
utotagok_listaja = ["erős", "költő", "morgó", "öltő", "papa", "picúr", "szakáll"]

for utotag in utotagok_listaja:
    print(elotag + utotag)

nev = "Alice"
kor = 10
s2 = "A nevem {1}, és {0} éves vagyok.".format(kor, nev)
print(s2)

