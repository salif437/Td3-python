#les 10 premiers nombres paires
a = input("entrez un nombre: ")
while not (a.isdigit() and int(a)):
    print("entrez un nombre")
    a = input("entrez un nombre: ")
o = int(a)
r = o+20
for i in range(o,r) : 
    if i%2==0 :
        print(i)
    
        
    

        
        
#les 10 premiers nombres impaires  avec while   
e = input("entrez un nombre: ")
while not (e.isdigit() and int(e)):
    print("erreur")
    e = input("entrez un nombre: ")
s = int(e)
l = s+20
i =s 
while i < l :
    if i%2==1 :
        print(i)
    i +=1
        


#affiche les nombres entier entre 1 et le nombre fourni par l'utilisateur
t = input("entrez un nombre: ")
while not (t.isdigit) :
    print("erreur")
    t = input("entrez un nombre: ")
s = int(t)
a = s+1
for i in range(1,a) :
    print(i)
    