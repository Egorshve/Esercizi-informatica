mappa={}
while True:
    conto=input("Scrivi il numero del conto:  ")
    saldo=input("Scrivi il numero del saldo:  ")
    mappa[conto]=saldo
    risposta=int(input("Se vuoi continuare schiaccia 1 "))
    if risposta==1:
        print()
    else:
        break

conto=input("Di quale conto vuoi sapere il saldo: ")
if conto in mappa:
    print("Il saldo del conto",conto,"è",mappa[conto])
else:
    print("Questo conto non è presente nella mappa")