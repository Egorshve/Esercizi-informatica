prenotazioni={}
prenotazioni_confermate=[]
while True:
    partecipante=input("Scrivi il nome del partecipante:  ")
    orario=int(input("Scrivi l'orario della prenotazione(solo orari di punta):  "))
    prenotazioni[partecipante]=orario
    continuo=int(input("Vuoi continuare a inserire prenotazioni? 1=SI 2=NO  "))
    if continuo==1:
        print()
        print()
    if continuo==2:
        break

print()
print("Elenco delle prenotazioni")
for x in prenotazioni:
    print(x)
    print(prenotazioni[x]) 
print()
print()
input()
print("Adesso visualizzerai ogni preontazione e potrai decidere se mandare la conferma")
while True:
    for x in prenotazioni:
        print(x)
        print(prenotazioni[x])    
        conferma=int(input("Vuoi mandare la conferma? 1=SI 2=NO "))
        if conferma==1:
            prenotazioni_confermate.append(x)
        if conferma==2:
            print()
        print("Elenco delle prenotazioni confermate")
        print(prenotazioni_confermate)
        print()
        if conferma==1:
            print("Prossimo partecipante: ")
    print()    
    print(prenotazioni_confermate)
    conferma2=int(input("Vuoi ripercorrere l'elenco dei partecianti? 1=SI 2=NO"))
    if conferma2==1:
        print()
    if conferma2==2:
        break

