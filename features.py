panier = []

def menu() :
    print("""
    1. Ajouter un article dans le panier
    2. Supprimer un article du panier
    3. Afficher tous les articles
    4. Vider le panier
    5. Quitter """)
    #sa = input("Quel est votre choix? ")

def ajout():
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

def supprimer1():
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
            
def affiche() :
    print(panier)
    for c in panier : 
        print(f" {c['name']} = {c['price']}") 
                
def supprimertout():
    panier.clear()
    print("tous les élément ont été supprimé")