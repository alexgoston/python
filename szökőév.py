evszam = int(input("Helló! Adj meg egy évszámot!"))
if (evszam%4!=0):
    print("Nem szökőév.")
elif (evszam%400==0):
    print("Szökőév.")
elif (evszam%100==0):
    print("Nem szökőév.")
else:
    print("Szökőév.")