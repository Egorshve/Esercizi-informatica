trump=0
biden=0
voti=0
trump=int(input("VOTI TRUMP"))
biden=int(input("VOTI BIDEN"))
lista=["trump","biden"]
lista.sort()
print("Ordine alfabetico dei partecipanti")
print(lista)
if biden > trump:
    lista.insert(0,"biden")
    lista.insert(1,"trump")
if trump > biden:
    lista.insert(0,"trump")
    lista.insert(1,"biden")
lista.pop()
lista.pop()
print("La lista dei candidati in ordine decrescente per punteggio")
print(lista)