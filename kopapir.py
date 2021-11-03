import random

while True:
    játékos_választása = input("Kő, papír, vagy olló?")
    lehetőségek = ["kő", "papír", "olló"]
    gép_választása = random.choice(lehetőségek)
    print(f"\nA te választásod a(z) {játékos_választása}, az ellenfélé a(z) {gép_választása}.\n")

    if játékos_választása == gép_választása:
        print(f"Mindkét fél a(z) {játékos_választása} eszközt választotta. Döntetlen!")
    elif játékos_választása == "kő":
        if gép_választása == "olló":
            print("A kő eltöri az ollót. Nyertél! :)")
        else:
            print("A papír becsomagolja a követ. Vesztettél! :(")
    elif játékos_választása == "papír":
        if gép_választása == "kő":
            print("A papír becsomagolja a követ. Nyertél! :)")
        else:
            print("Az olló elvágja a papírt. Vesztettél! :(")
    elif játékos_választása == "olló":
        if gép_választása == "papír":
            print("Az olló elvágja a papírt. Nyertél! :)")
        else:
            print("A kő eltöri az ollót. Vesztettél! ):")

    play_again = input("Új játék? (i/n): ")
    if play_again.lower() != "i":
        break