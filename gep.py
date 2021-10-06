tipus = input('Mi a gép típusa?')
allapot = input('Működik, renden van? (igen/nem)')
ar = int(input('Mennyibe kerül?'))
if tipus == 'C64':
    if allapot == 'igen':
        if ar <= 25000:
            print('Működő C64 gépet vehetünk 25000 forint alatt.')
        else:
            print ('A gép túl drága.')
    else:
        print('A gép nem működik.')
elif tipus == 'ZX Spectrum':
    if allapot == 'igen':
        if ar <= 25000:
            print('Működő ZX Spectrum gépet vehetünk 25000 forint alatt.')
        else:
            print ('A gép túl drága.')
    else:
        print('A gép nem működik.')
else:
    print('Nincs megfelelő típusú gép.')



#2. megoldás
tipus = input('Mi a gép típusa?')
működik = True if input('Működik? (i/n) ') == 'i' else False
ár = int(input('Mennyibe kerül? '))
if (tipus == 'ZX Spectrum' or tipus == 'C64') and működik and ár <= 25000:
    print('Deal!')
else:
    print('Gagyi nyócbitesek.. Kinek kellenek? Azt én meg hogyan R6-ozzak? Jézusom...')