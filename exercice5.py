# Listes pour stocker les clients et les transactions
customers = []
transactions = []

# Fonction pour afficher le menu principal
def main_menu():
    while True:
        print("""Menu principal
        1 - Gestion des clients
        2 - Gestion des transactions
        3 - Sortir""")
        
        choice = input("Choisissez une option : ")
        
        if choice == "1":
            gestion_client()
        elif choice == "2":
            manage_transactions()
        elif choice == "3":
            break
        else:
            print("Option invalide. Veuillez réessayer.")

# Fonctions pour la gestion des clients
def gestion_client():
    while True:
        print(f"""Gestion des clients
        1 - Afficher la liste des clients
        2 - Ajouter un client
        3 - Supprimer un client
        4 - Modifier les informations d'un client
        5 - Afficher le solde d'un client
        6 - Retour au menu principal""")
        
        choice = input("Choisissez une option : ")
        
        if choice == '1':
            afficher_client()
        elif choice == '2':
            add_customer()
        elif choice == '3':
            delete_customer()
        elif choice == '4':
            modify_customer()
        elif choice == '5':
            display_balance()
        elif choice == '6':
            break
        else:
            print("Option invalide. Veuillez réessayer.")

def afficher_client():
    if not customers:
        print("Aucun client n'est enregistré.")
    else:
        for customer in customers:
            print(customer)

def add_customer():
    code = input("Code du client : ")
    if any(c['code'] == code for c in customers):
        print("Un client avec ce code existe déjà.")
        return
    
    name = input("Nom du client : ")
    phone = input("Téléphone du client : ")
    address = input("Adresse du client : ")
    email = input("Email du client : ")
    
    customer = {'code': code, 'name': name, 'phone': phone, 'address': address, 'email': email, 'balance': 0}
    customers.append(customer)
    print("Client ajouté avec succès.")

def delete_customer():
    code = input("Code du client à supprimer : ")
    for customer in customers:
        if customer['code'] == code:
            customers.remove(customer)
            print("Client supprimé avec succès.")
            return
    print("Client non trouvé.")

def modify_customer():
    code = input("Code du client à modifier : ")
    for customer in customers:
        if customer['code'] == code:
            customer['name'] = input("Nom du client : ")
            customer['phone'] = input("Téléphone du client : ")
            customer['address'] = input("Adresse du client : ")
            customer['email'] = input("Email du client : ")
            print("Informations du client mises à jour avec succès.")
            return
    print("Client non trouvé.")

def display_balance():
    code = input("Code du client : ")
    for customer in customers:
        if customer['code'] == code:
            print(f"Solde du client {customer['name']}: {customer['balance']}")
            return
    print("Client non trouvé.")

# Fonctions pour la gestion des transactions
def manage_transactions():
    while True:
        print("\nGestion des transactions")
        print("1 - Afficher toutes les transactions")
        print("2 - Afficher les transactions d'un client")
        print("3 - Ajouter une transaction entre deux clients")
        print("4 - Retour au menu principal")
        
        choice = input("Choisissez une option : ")
        
        if choice == '1':
            display_transactions()
        elif choice == '2':
            display_customer_transactions()
        elif choice == '3':
            add_transaction()
        elif choice == '4':
            break
        else:
            print("Option invalide. Veuillez réessayer.")
            
            
def display_transactions():
    if not transactions:
        print("Aucune transaction n'est enregistrée.")
    else:
        for transaction in transactions:
            print(transaction)

def display_customer_transactions():
    code = input("Code du client : ")
    customer_transactions = [t for t in transactions if t['code_emmeteur'] == code or t['code_recepteur'] == code]
    if not customer_transactions:
        print("Aucune transaction trouvée pour ce client.")
    else:
        for transaction in customer_transactions:
            print(transaction)

def add_transaction():
    ref_paiement = input("Référence de paiement : ")
    code_emmeteur = input("Code de l'émetteur : ")
    code_recepteur = input("Code du récepteur : ")
    date_transaction = input("Date de la transaction : ")
    montant = float(input("Montant : "))
    canal = input("Canal (ORANGE MONEY, WAVE, FREE MONEY, VIREMENT BANCAIRE) : ")
    
    emmeteur = next((c for c in customers if c['code'] == code_emmeteur), None)
    recepteur = next((c for c in customers if c['code'] == code_recepteur), None)
    
    if not emmeteur or not recepteur:
        print("Émetteur ou récepteur non trouvé.")
        return
    
    transaction = {
        'ref_paiement': ref_paiement,
        'code_emmeteur': code_emmeteur,
        'code_recepteur': code_recepteur,
        'date_transaction': date_transaction,
        'montant': montant,
        'canal': canal
    }
    transactions.append(transaction)
    
    emmeteur['balance'] -= montant
    recepteur['balance'] += montant
    
    print("Transaction ajoutée avec succès.")

# Exécution de l'application
#if __name__ == "__main__":
main_menu()
            