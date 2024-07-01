from features import  *

while True :
    menu()
    sa = input("Quel est votre choix? ")
    while not (sa.isdigit() and int(sa) in range(1,6)) : 
        print("erreur, entrez un nombre entre 1 et 5")
        menu()
    if sa == "1" :
        ajout()
    elif sa == "2" :
        supprimer1()
    elif sa == "3" :
        affiche()
    elif sa =="4" :
        supprimertout()
    else :
        print("Fin du programme")
        exit() 
    
        