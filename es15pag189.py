numero_nazioni=int(input("Quante nazioni vuoi inserire?  "))
capitali=[]
nazioni=[]
contatore=0
while True:
    nazione=input("Inserisci il nome della nazione: ")
    nazioni.append(nazione)
    capitale=input("Inserisci il nome della capitale: ")
    capitali.append(capitale)
    contatore+=1
    if contatore==numero_nazioni:
        break
print()
print()
nazione=input("Inserisci il nome della nazione della quale vuoi conoscere la capitale:  ")
if nazione in nazioni:
    indice=nazioni.index(nazione)
    print("La capitale di questa nazione è",capitali[indice])
else:
    print("La nazione non è presente")


    