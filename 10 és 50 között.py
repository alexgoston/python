import random

print("Gondoltam két számra. A következő kettőre:")

szám = random.randint(10, 50)
szám2 = random.randint(0, 10)
lista1 = [szám,szám2]
for i in lista1:
    print(i)

print("Az első számot elosztottam a másodikkal. Az eredmény:", szám/szám2)
print("Az első számhoz hozzáadtam a másodikat. Az eredmény:", szám+szám2)
print("Az első számból kivontam a másodikat. Az eredmény:", szám-szám2)
print("Az első számot megszoroztam a másodikkal. Az eredmény:", szám*szám2)
print("Az első számot hatványra emeltem, a hatványkitevő a második szám. Az eredmény:", szám**szám2)