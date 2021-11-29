#halmaz létrehozása
reggeli = {"tea", "vaj", "pirítós"}
    
#üres halmaz létrehozása
#ebéd = {} -szótárt fog létrehozni
ebéd = set()

#bejárható gyűjteményből, pl. listából
ebéd = set(["halászlé", "kenyér", True])
    
#egy elem hozzáadása
reggeli.add("lekvár")

#egy nem meghatározott elem eltávolítása
reggeli.pop()

#egy bizonyos elem eltávolítása
#ha nincs ilyen elem, hibát eredményez
#reggeli.remove("sajt")
#ki lett véve a forráskódból, mint paracs, kommentként kezeli a program
#így látható a példában, hogy ez a parancs eredményezne hibát
#de nem fut le, mint parancs, így tudjuk tovább futtatni a programot probléma nélkül

#egy bizonyos elem eltávolítása
#ha nincs ilyen elem, nem eredményez hibát
reggeli.discard("sajt")
reggeli = {"víz", "tea", "vaj", "pirítós"}
ebéd = {"víz", "halászlé", "kenyér"}

#metszet
print(reggeli & ebéd)
#unió
print(reggeli | ebéd)
#különbség
print(reggeli - ebéd)
#csak az egyikben/csak a másikban
print(reggeli ^ ebéd)
