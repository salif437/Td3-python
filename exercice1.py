t = input("Entrez une note: ")
while not (t.isdigit() and int(t)) : 
    print("entrez un nombre")
    t = input("Entrez une note: ")
r = int(t)
if r>=18 :
    print("Excellent")
elif 16<=r<18:
    print("Très bien")
elif 14<=r<16 :
    print("Bien")
elif 12<=r<14 :
    print("Satisfaisant")
elif 10<=r<12 : 
    print("Passable")
else :
    print("Échec")
    