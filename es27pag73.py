giorno=1
veicoli=0
segnale=1

while True:
    print("Giorno:  ",giorno)
    veicoli+=int(input("Inserire numero veicoli transitati:  "))
    segnale=int(input("Se vuoi continuare schiaccia 1,altrimenti 0:   "))
    giorno+=1
    if segnale==0:
        giorno-=1
        break
    

print()    
print("In",giorno,"giorni sono transitati",veicoli)