lista_pazienti=[]
while True:
    paziente=input("Scrivi il nome del paziente: ")
    lista_pazienti.append(paziente)
    continuo=int(input("Schiaccia 1 se vuoi continuare, 2 se vuoi terminare di inserire i nomi dei pazienti "))
    if continuo==1:
        print()
        print()
    else:
        break
print("Il primo paziente della coda è ",lista_pazienti[0])