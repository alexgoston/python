import random
szam1 = random.randint(1,10)
szam2 = random.randint(1,10)

print("Gondoltam két számra 1 és 10 között.")

#1
if (szam1%2==0):
    print("Az első szám páros.")
else:
    print("Az első szám páratlan.")
kerdes1 = input("Érdekel, hogy az első szám, amelyre gondoltam, osztható-e 3-mal? (igen/nem)")
if kerdes1 == "igen":
    if (szam1%3==0):
        print("A szám osztható 3-mal.")
    else:
        print("A szám nem osztható 3-mal.")
else:
    print("Hát akkor nem.")
kerdes2 = input("Érdekel az első szám amelyre gondoltam? (igen/nem)")
if kerdes2 == "igen":
    print(szam1)
else:
    print("Szóval nem.")

#2
if (szam2%2==0):
    print("A második szám páros.")
else:
    print("A második szám páratlan.")
kerdes1 = input("Érdekel, hogy a második szám, amelyre gondoltam, osztható-e 3-mal? (igen/nem)")
if kerdes1 == "igen":
    if (szam2%3==0):
        print("A szám osztható 3-mal.")
    else:
        print("A szám nem osztható 3-mal.")
else:
    print("Hát akkor nem.")
kerdes2 = input("Érdekel a második szám amelyre gondoltam? (igen/nem)")
if kerdes2 == "igen":
    print(szam2)
else:
    print("Szóval nem.")