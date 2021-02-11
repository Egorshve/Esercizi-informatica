dizionario_CAP={}
dizionario_città={}
numero_città=int(input("Quante città ci sono? "))
contatore=0
while contatore!=numero_città:
    città=input("Dimmi il nome della città: ")
    CAP=input("Dimmi il corrispondente CAP: ")
    dizionario_CAP[CAP]=città
    dizionario_città[città]=CAP
    contatore+=1

domanda=input("Dimmi il nome della città per visualizzare il suo CAP oppure il CAP per visualizzare il nome della città: ")
if domanda in dizionario_CAP:
    print(dizionario_CAP[domanda])
if domanda in dizionario_città:
    print(dizionario_città[domanda])
else:
    print("Il seguente CAP o nome di città non è presente nell'elenco")

