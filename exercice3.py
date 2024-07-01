#liste et dictionnaire
panier =[]
while True :
    
    print("""
    1. Ajouter un article dans le panier
    2. Supprimer un article du panier
    3. Afficher tous les articles
    4. Vider le panier
    5. Quitter """)
    sa = input("Quel est votre choix? ")
    
    while not (sa.isdigit() and int(sa) in range(1,6)) : 
        print("erreur, entrez un nombre entre 1 et 5")
        print(f"""
            1. Ajouter un article dans le panier
            2. Supprimer un article du panier
            3. Afficher tous les articles
            4. Vider le panier
            5. Quitter  """)
        sa = input("Quel est votre choix?" )
#si l'utilisateur choisi 1  
    if sa == "1":
        a = input("entrez un article: ")
        b = input("entrez le prix de l'article: ")
        while not (a.isalpha() and b.isdigit()) :
            print("erreur")
            a = input("entrez un article: ")
            b = input("entrez le prix de l'article: ")
        c = {
            'name' : a,
            'price' : b
            }
        panier.append(c)
        print("article ajouté au panier")
            
# Si  l'utilisateur choisi 2
    elif sa == "2":
        d =input("quelle est le nom de l'artcle à supprimer: ")
        while not (d.isalpha()):
            print("erreur")
            d =input("quelle est le nom de l'artcle à supprimer: ")
        for c in panier :
            if c['name']== d :
                panier.remove(c)
                print(" article supprimé.")
                
            else :
                print("Aucun article avec ce nom dans le panier.")
                
        
#si l'utilisateur choisi 3        
    elif sa == "3":
        print(panier)
        for c in panier : 
                print(f" {c['name']} = {c['price']}") 
            
#si l'utilisateur choisi 4
    elif sa == "4":
        panier.clear()
        print("tous les élément ont été supprimé")
#si l'utilisateur choisi 5
    else :        
# Affichage d'un message de fin et on arrete le programme 
        print("Fin du programme")
        #break 
        exit() 