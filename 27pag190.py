rubrica={}
numero_studenti=int(input("Quanti studenti ci sono?  "))
contatore=0
while contatore!=numero_studenti:
    nome=input("Dimmi il nome dello studente ")
    numero=int(input("Dimmi il nome dello studente "))
    rubrica[nome]=numero
    contatore+=1

domanda=input("Di quale studente vuoi sapere il numero? ")
if domanda in rubrica:
    print(rubrica[domanda])
else:
    print("Lo studente non è presente nella lista")
