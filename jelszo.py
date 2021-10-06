#
#
 
#JELSZO = input('Mi a jelszava?') 
#print(JELSZO)
JELSZO = 'Jelszó'
jelszo = None
while jelszo != JELSZO:
    jelszo = input('Mi a jelszava?')
    if jelszo != JELSZO:
        print('Helytelen jelszó. Ellenőrizze, majd adja meg újra jelszavát!')
        pass
print('Helyes jelszó. Üdvözöljük!')