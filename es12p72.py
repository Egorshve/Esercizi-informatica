articolo=input("Scrivere il nome dell'articolo:   ")
t=int(input("Vuoi aggiungere una descrizione? 1.sì 2.no   "))
if t==1:
    descrizione=input()
if t==2:
    descrizione=()
print("Quanti articoli di",articolo,"vuoi acquistare?")
quantità=float(input())
prezzo=float(input("Quanto costa l'articolo?  "))
iva=float(int(input("A quanto corrisponde l'IVA?(percentuale)   "))/100)
prezzototale=float((prezzo*iva)*quantità)
round(prezzototale,2)
print()
print()
print(articolo)
print(descrizione)
print(prezzototale,"euro")


    
    
