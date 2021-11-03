hónap = ["január", "február", "március", "április", "május"]
for i in hónap:
    print(i, end=" ")
print("\nA tömb mérete: ", len(hónap))
for j in range(len(hónap)):
    print("%d. hónap: %s" % (j+1, hónap[j]))