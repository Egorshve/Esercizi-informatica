print("equazione (ax + b = 0)")
a=int(input("A quanto corrisponde il parametro (a)    "))
b=int(input("A quanto corrisponde il parametro (b)    "))

if a==0 and b==0:
    print("Questa equazione è indeterminata")
if a==0 and b!=0:
    print("Questa equazione è impossibile")
if a!=0 and b==0:
    print("La soluzione è x=0")
if a!=0 and b!=0:
    print("La soluzione è x=-b/a")

