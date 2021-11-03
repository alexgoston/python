#49
hónap = ["január", "február", "március", "április", "május"]
for i in hónap:
    print(i, end=" ")
print("\nA tömb mérete: ", len(hónap))
for j in range(len(hónap)):
    print("%d. hónap: %s" % (j+1, hónap[j]))

#50
strl = "isz"
hb = ""
hb = "h" + strl + "ed"
print(hb)
print(hb[3])

#51
strl = "hiszed"
print(len(strl))
print(strl[1:4])
strl = strl[1:]
print(strl)
strl = strl[:3]+"o"+strl[4:]
print(strl)

#63
wr = open("szöveg.txt",'w')
wr.write("Ágoston Alex")
wr.close()
wr = open("szöveg.txt",'a')
wr.write("\nPython")
wr.close()
wr = open("szöveg.txt",'a')
wr.write("\n2021. 10. 20.")
wr.close()

#64
import sys
oldout = sys.stdout
print("Képernyőre ír...")
wr = open("szöveg2.txt",'a')
sys.stdout = wr
print("Fájlba ír...")
wr.close
print("Hová ír?")
sys.stdout = oldout
print("Képernyőre ír...")



#házi feladat

#1
szó1 = input("Adjon meg egy szót!")
szóhossz1 = len(szó1)
print("A megadott szó hossza", szóhossz1, "karakter.")

#2
szó2 = input("Adjon meg egy szót!")
print("A megadott szó kezdőbetűje a(z)", szó2[0], "karakter.")

szó3 = input("Adjon meg egy szót!")
print("A megadott szó utolsó betűje a(z)", szó3[-1], "karakter.")

#3
szó4 = input("Adjon meg egy 5 betűs szót!")
print("A megadott szó középső betűi a(z)", szó4[1], szó4[2], szó4[3], "karakterek.")

#4
bpirszám = int(input("Adjon meg egy budapesti irányítószámot!"))
if bpirszám[1] == 0 and bpirszám[2] == 1:
    print("A megadott irányítószám az I. kerületben található.")
elif bpirszám[1] == 0 and bpirszám[2] == 2:
    print("A megadott irányítószám az II. kerületben található.")
elif bpirszám[1] == 0 and bpirszám[2] == 3:
    print("A megadott irányítószám az III. kerületben található.")
elif bpirszám[1] == 0 and bpirszám[2] == 4:
    print("A megadott irányítószám az IV. kerületben található.")
elif bpirszám[1] == 0 and bpirszám[2] == 5:
    print("A megadott irányítószám az V. kerületben található.")
elif bpirszám[1] == 0 and bpirszám[2] == 6:
    print("A megadott irányítószám az VI. kerületben található.")
elif bpirszám[1] == 0 and bpirszám[2] == 7:
    print("A megadott irányítószám az VII. kerületben található.")
elif bpirszám[1] == 0 and bpirszám[2] == 8:
    print("A megadott irányítószám az VIII. kerületben található.")
elif bpirszám[1] == 0 and bpirszám[2] == 9:
    print("A megadott irányítószám az IX. kerületben található.")
elif bpirszám[1] == 1 and bpirszám[2] == 0:
    print("A megadott irányítószám az X. kerületben található.")
elif bpirszám[1] == 1 and bpirszám[2] == 1:
    print("A megadott irányítószám az XI. kerületben található.")
elif bpirszám[1] == 1 and bpirszám[2] == 2:
    print("A megadott irányítószám az XII. kerületben található.")
elif bpirszám[1] == 1 and bpirszám[2] == 3:
    print("A megadott irányítószám az XIII. kerületben található.")
elif bpirszám[1] == 1 and bpirszám[2] == 4:
    print("A megadott irányítószám az XIV. kerületben található.")
elif bpirszám[1] == 1 and bpirszám[2] == 5:
    print("A megadott irányítószám az XV. kerületben található.")
elif bpirszám[1] == 1 and bpirszám[2] == 6:
    print("A megadott irányítószám az XVI. kerületben található.")
elif bpirszám[1] == 1 and bpirszám[2] == 7:
    print("A megadott irányítószám az XVII. kerületben található.")
elif bpirszám[1] == 1 and bpirszám[2] == 8:
    print("A megadott irányítószám az XVIII. kerületben található.")
elif bpirszám[1] == 1 and bpirszám[2] == 9:
    print("A megadott irányítószám az XIX. kerületben található.")
elif bpirszám[1] == 2 and bpirszám[2] == 0:
    print("A megadott irányítószám az XX. kerületben található.")
elif bpirszám[1] == 2 and bpirszám[2] == 1:
    print("A megadott irányítószám az XXI. kerületben található.")
elif bpirszám[1] == 2 and bpirszám[2] == 2:
    print("A megadott irányítószám az XXII. kerületben található.")
elif bpirszám[1] == 2 and bpirszám[2] == 3:
    print("A megadott irányítószám az XXIII. kerületben található.")
