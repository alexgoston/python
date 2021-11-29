#bevezetés
print("Üdv!")
print("A program elejére kiírtam bizonyos megjegyzéseket, hogy tisztán átlátható legyen a program.")
print("A halmazokkal végeztem műveleteket, kiírtam a példaszámot, a feladatot, aztán érthető magyarázattal körülírtam,")
print("mintha mindennapi eseményekről beszélnénk. Ezért is van, hogy egyes példáknál listákról van szó, mert azok nem")
print("listák, hanem halmazok, csak hogy a példa reális legyen, például egy bevásárlólistaként van említve a halmaz.")

#1) hozzon létre egy halmazt és törölje
print(" ")
print("1. példa")
print("Létrehoztuk egy halmazt, de törölnünk kell. Így nem maradnak elemei.")
print("A halmazban az elemek azok az ételek, amelyeket szívesen falatoznánk reggelire, de ránézünk az órára,")
print("és látjuk, hogy skippelnünk kell a reggelit, hogy el ne késsünk, így töröljük az elemeket.")
halmaz1 = {"kakaós csiga", "tejbegríz", "müzli"}
print("Létrehoztuk a halmazt. A következő elemeket tartalmazza:")
print(halmaz1)
halmaz1.clear()
print("De törölnünk kell az elemeket, vagyis üres halmazunk marad. Ezért üres halmazt ír ki, ha kiíratjuk [set()]:")
print(halmaz1)

#2) másolja át a halmaz értékkészletét egy másik halmazba
print(" ")
print("2. példa")
print("Másoljuk át egy halmaz értékkészletét (elemeit) egy másikba.")
print("Másoljuk át az előző példa halmazát egy másik halmazba, ehhez új halmazt hozunk létre. Tartalma az előző halmaz.")
print("Elküldjük a havernak, mit reggeliznénk szívesen, de  töröltük az elemeket a halmazból, így nem küldünk semmit.")
print("Ezért a halmaz üres marad, majd bepótolhatjuk út közben a pékségben, ha hamarabb ér a busz a központba.")
halmaz2 = halmaz1.copy()
print("Létrehoztuk a halmazt, tartalma az előző halmazzal azonos. Ha kiíratjuk, azt látjuk, hogy [set()] (üres halmaz),")
print("mert az előző halmaz üres volt, így nincs tartalma.")
print(halmaz2)

#3) hozzon létre két halmazt és képezze a két halmaz különbségét (difference()metódus)
print(" ")
print("3. példa")
print("Létrehozuk két halmazt, majd a különbségüket képezzük, utána kiíratjuk.")
print("Az első halmazban azoknak az embereknek a státusza van felsorolva, akik egy támogatásra pályáztak.")
print("A másodikban olyan státuszok vannak felsorolva, amelyek mellett nyerhetünk támogatást. Így a halmazok különbségéből azt")
print("kapjuk meg, kik nem jelentkezhetnek.")
halmaz3 = {"nappali tagozatos képzésben részesül", "esti tagozatos képzésben részesül", "középiskolai tanuló", "általános iskolás", "nem részesül képzésben", "munkanélküli", "munkavállaló"}
halmaz4 = {"nyugdíjas", "egyetemista", "nappali tagozatos képzésben részesül", "esti tagozatos képzésben részesül", "munkavállaló"}
print("A következők jelentkeztek:")
print(halmaz3)
print("A következők kapnak támogatást:")
print(halmaz4)
print("így a pályázók, akik nem kapnak támogatást:")
print(halmaz3.difference(halmaz4))

#4) hozzon létre két halmazt és távolítsa el azokat az elemeket, amelyek szerepelnek a másodikban is [difference_update()]
print(" ")
print("4. példa")
print("Létrehozunk két halmazt, majd az elsőből eltávolítjuk azokat az elemeket, amelyek a másodikban is találhatóak.")
print("Töriből sok ember bukásra áll, de a tanár úgy döntött, azokat tovább engedi, akik matekból nem állnak bukásra.")
print("Az elsó halmaz tartalmazza azokat a tanulókat, akik töriből bukásra állnak. A második azokat, akik matematikából.")
halmaz5 = {"B. Ákos", "S. Renátó", "Z. Vivien"}
print("Történelemből bukásra állnak:")
print(halmaz5)
halmaz6 = {"A. Ákos", "S. Renátó", "S. Kata", "Z. Vivien"}
print("Matematikából bukásra állnak:")
print(halmaz6)
halmaz5.difference_update(halmaz6)
print("Át lesznek engedve történelemből:")
print(halmaz5)

#5) hozzon létre két halmazt és használja intersection () metódust. Írja le mit kapott végeredményként!
print(" ")
print("5. példa")
print("Hozzunk létre két halmazt, majd alkalmazzuk az intersection() metódust. Írjuk ki az eredményt.")
print("Két halmaz metszetét fogjuk kapni.")
print("Létrehozunk két halmazt, majd képzünk egy harmadikat, amelyben azok az elemek találhatóak meg, amelyek közösek az előző kettőben.")
print("Megkérdeztük két barátunkat, mely tanórákon szeretik a társaságot, ahol 3-man egy padba lehet ülni. A két halmazunk")
print("tartalma azok az órák, amelyeken szeretik, ha van mellettük valaki. A harmadik halmaz pedig azokból a tanórákból fog képződni,")
print("amelyeken mindketten össze akarnak ülni, így a harmadik halmaz lényegében azoknak a tanóráknak a felsorolása, ahol egymás")
print("mellett fogunk ülni.")
halmaz7 = {"Matematika", "Irodalom", "Természettudomány", "Informatika"}
print("Létrehoztuk a halmazt. Csongor ezeken az órákon akar beszélgetni:")
print(halmaz7)
halmaz8 = {"Kémia", "Fizika", "Természettudomány", "Informatika", "Idegen nyelv"}
print("Most pedig létrehoztuk azt a halmazt, ahol Szabolcs beszélgetne szívesen:")
print(halmaz8)
halmaz9 = halmaz7.intersection(halmaz8)
print("Létrehoztuk a halmazt, megkaptuk a tanórákat, ahol egymás mellett fogunk ülni:")
print(halmaz9)

#6) hozzon létre két halmazt és képezzen egy olyan halmazt, amely azokat az elemeket tartalmazza, amelyek nem szerepelnek mindkettőben. intersection_update()
print(" ")
print("6. példa")
print("Létrehozunk két halmazt, majd képezünk egy harmadikat, amiben azok az elemek vannak, amelyek benne vannak az elsőben, de a")
print("másodikban nincsenek.")
print("Van két szakkör. Rajz és matematika. A tanárnő olyan rajzszakkörös tanulókat keres, akik nem matekosak. Így az első halmaz")
print("értelemszerűen a rajzosoké, a második a matekosoké. A harmadik halmaz azoké, akik csak rajzosok, így viszi őket tanárnő.")
halmaz10 = {"A. Csabi", "D. Sándor", "F. Maja", "H. Máté", "H. Rozi", "Sz. Lili"}
print("Rajzszakkörös tanulók:")
print(halmaz10)
halmaz11 = {"A. Csabi", "B. Lajos", "H. Máté", "Sz. Lili", "T. Béla"}
print("Matekszakkörös tanulók:")
print(halmaz11)
halmaz10.intersection_update(halmaz11)
print("Így a tanulók, akiket tanárnő foglalkozásra visz:")
print(halmaz10)

#7) hozzon létre két halmazt és használja az isdisjoint() metódust. Írja le mikor kaphatunk True és False kimeneti értéket.
print(" ")
print("7. példa")
print("Létrehozunk két halmazt, majd megézzük, van-e közös eleme az isdisjoint() metódussal.")
print("Sanyi és Béla írtak egy listát, hogy milyen sportokat szeretnek, és ha közös kedvencre bukkannak, arra a meccsre mennek el. Ha")
print("nincs ilyen, otthon maradnak. A kérdés az, hogy otthon maradnak-e? Ha igen, akkor True választ kapunk, ha nem, akkor False.")
halmaz12 = {"foci", "kosár", "tenisz", "baseball"}
print("Sanyi sportjai:")
print(halmaz12)
halmaz13 = {"jégkorong", "box", "mma", "golf", "tenisz"}
print("Béla sportjai:")
print(halmaz13)
print("Akkor otthon maradnak?")
print(halmaz12.isdisjoint(halmaz13))

#8) mire használható issubset() metódus? Írjon rá példát!
print(" ")
print("8. példa")
print("Létrehozunk két halamzt, majd megnézzük, hogy az elsőnek az összes eleme  benne van-e a másodikban.")
print("Tesóval vagyunk otthon, aki ránkhagyta a listát, amelyet anya készített, hogy legyen minden megcsinálva, mire hazaér. Az első")
print("halmaz azon tennivalók listája, amelyek már készen vannak, a második az, amit otthon hagyott anya. Ha minden kész, amit felírt,")
print("akkor a program kiírja, hogy True, ha nincs kész minden, akkor azt írja ki, hogy False.")
halmaz14 = {"mosogatás", "teregetés", "porszívózás", "ruhamosás", "ágynemű hajtogatás", "főzés"}
print("A teendők:")
print(halmaz14)
halmaz15 = {"mosogatás", "ruhamosás", "porszívózás", "ágynemű hajtogatás"}
print("Ami készen van:")
print(halmaz15)
print("Tehát készen van-e minden?")
print(halmaz14.issubset(halmaz15))
print("(Csak kiegészítés.) A tennivalók, amik tesóra maradtak:")
print(halmaz14 - halmaz15)

#9) mire használható issuperset() metódus? Írjon rá példát!
print(" ")
print("9. példa")
print("Létrehozunk két halmazt, majd megnézzük, hogy a második halmaz minden elemét tartalmazza-e az első.")
print("Feladatokat csináltunk otthon, többet, mint amit a tanár feladott. Az első halmaz azon feladatok listája, amelyet megcsináltunk,")
print("a második halmaz azon feladatok listája, amelyet a tanár feladott.Az eredmény True, ha mindent megcsináltunk, amit a tanár adott,")
print("ellenkező esetben értelemszerűen False az eredmény.")
halmaz16 = {"64.", "65.", "68.", "72.", "73.", "74.", "82."}
print("Feladatok, melyeket megoldottunk:")
print(halmaz16)
halmaz17 = {"65.", "72.", "73.", "82."}
print("Feladatok, melyeket a tanár adott fel:")
print(halmaz17)
print("Készen van-e minden feladat?")
print(halmaz16.issuperset(halmaz17))

#10) mire használható symmetric_difference() metódus? Írjon rá példát!
print(" ")
print("10. példa")
print("Létrehozunk két halmazt, majd kiírjuk azokat az elemeket, amelyek a két halmaz metszetén kívül találhatóak (nem közös elemek).")
print("Megjegyzés: ^ karakterrel is elvégezhetjük ezt a műveletet, de ebben a példában mi most symmetric_difference() metódussal írjuk ki.")
print("Van két listánk, esküvői teendők. Azok a tennivalók, amik mind a két listán szerepelnek, már készen vannak. Így kiírjuk azokat,")
print("melyek még várnak ránk.")
halmaz18 = {"csokrok megvásárlása", "erkély díszítése", "gazolás", "szállítmányok ellenőrzése", "torta rendelése", "ebéd rendelése"}
print("Első tennivaló-lista:")
print(halmaz18)
halmaz19 = {"csokrok megvásárlása", "ebéd rendelése", "nasik megvásárlása", "autó bérlése", "egyeztetni a pappal"}
print("Második tennivaló-lista:")
print(halmaz19)
print("És a tennivalók, melyek még várnak ránk:")
print(halmaz18.symmetric_difference(halmaz19))

#11) keressen még további három metódus az interneten, próbálja ki írja le milyen műveletet hajtanak végre egy halmazon!
print(" ")
print("+3 példa")
print(" ")
print("11. példa")
print("Létrehozunk egy halmazt, majd a pop metódussal egy véletlenszerű elemet távolítunk el belőle.")
print("Van egy zsákba pár cetli, amin nevek vannak. Akit kihúzunk, azt kell meglepjük, persze nem tudjuk előre, kit húzunk ki.")
halmaz20 = {"Máté", "Eszter", "Csaba", "Jenő", "Dorka", "Ákos"}
print("A nevek:")
print(halmaz20)
halmaz20.pop()
print("Valakit kihúztál, így a lista a követkető:")
print(halmaz20)
print("*kiegészítettem egy while szerkezettel, hogy addig kérdezze azt, hogy kit húztunk ki, míg el nem találjuk, de ez csak bónusz*")
halmaz20.add("valami")
kiaz = "valami"
kiaz = input("Szerinted kit húztál ki?")
while kiaz in halmaz20:
    kiaz = input("Sajnos téves! :( Próbáld újra!")
print("Igen,", kiaz, "volt, akit kihúztál.")
print(" ")
print("12. példa")
print("Létrehozunk egy halmazt, majd bekérjük, hogy a felhasználó mely elemet szeretné eltávolítani.")
print("Van egy listánk, amely tartalmaz bizonyos ételeket. Eltávolíthatjuk azokat, melyeket nem fogyasztunk szívesen, majd kiírjuk")
print("a végleges listát. Ha semmit nem szeretünk, a lista üres marad, a program eredményül kiírja, hogy set(), de ebben az esetben")
print("hozzáadhatunk párat magunktól.")
halmaz21 = {"rántott hús", "töltött hús", "palacsinta", "bejgli", "kalács"}
print(halmaz21)
kérdés = input("Szeretnél eltávolítani ételeket? (igen/nem)")
while kérdés != "nem":
    étel = input("Mit szeretnél eltávolítani?")
    halmaz21.remove(étel)
    print("Az étel eltávolítása megtörtént.")
    üres = (len(halmaz21) == 0)
    if üres:
        print("Az összes étel eltávolításra került.")
        kérdés = input("Kilépéshez írd be, hogy *nem* (csillag karakterek nélkül).")
    else:
        kérdés = input("Szeretnél még valamit eltávolítani? (igen/nem)")
üres = (len(halmaz21) == 0)
if üres:
    kérdés2 = input("Úgy tűnik, semmit nem szerettél a megadott ételek közül. Szeretnél mást megadni? (igen/nem)")
    while kérdés2 != "nem":
        étel2 = input("Mit adjunk hozzá?")
        halmaz21.add(étel2)
        kérdés2 = input("Szeretnél még valamit hozzáadni? (igen/nem)")
print("Itt a lista a szeretett ételekkel:")
print(halmaz21)
print("Ha azt látod, hogy set(), akkor nem szerettél egy megadott ételt sem, valamint nem is adtál hozzá mást.")