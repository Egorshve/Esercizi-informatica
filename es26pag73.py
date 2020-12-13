dipendenti=int(input("NUMERO DIPENDENTI"))
aggiunta=0
stipendiototale=0
traccia=1
while aggiunta!= -1:
    print("INSERIRE STIPENDIO NUMERO",traccia)
    aggiunta=int(input())
    traccia+=1
    stipendiototale+=aggiunta
media=stipendiototale/dipendenti
print("La media degli stipendi è",media)