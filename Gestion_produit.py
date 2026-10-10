dic_livre={
   1:{'Title':'python','price':12,'amount':10}, 
   2:{'Title':'java','price':30,'amount':15}
  }

def ajouter_produit():
    print("\n➕ Ajouter un produit")
    new_id = max(dic_livre, default=0) + 1
    titre = input("Nom : ").strip()
    #categorie = choisir_categorie()
    prix = int(input("Prix (ex. 19.99) : "))
    quantite =float(input("Quantité : "))

    prod = {
        "Title": titre,
        "price": prix,
        "amount": quantite,
    }
    
    dic_livre[new_id]=prod
   # print(f"✅ Produit ajouté avec ID #{prod['id']}.")
#ajouter_produit()

def afficher_list():
    for pid, info in dic_livre.items():
        print(pid, "=>", info["Title"], info["price"],info["amount"])

def rechercher():
    id=int(input("dooner un id"))
    for i,info in dic_livre.items():
        if i== id:
            print(info)


def afficher_menu():
    print("\n=== MENU ===")
  
    print("""
    1: Ajouter un produit
    2: Lister les produits
    3: Rechercher (nom/catégorie)
    0: Quitter
    """)
 

def main():
    print("Application de gestion ")

    while True:
        afficher_menu()

        try:
            choix = int(input("Votre choix : "))
        except ValueError:
            print("⚠️ Veuillez entrer un nombre.")
            continue

        if choix == 1:
            ajouter_produit()
        elif choix == 2:
            afficher_list()
        elif choix == 3:
            rechercher()
        elif choix == 0:
            print("Au revoir !")
            break
        else:
            print("⚠️ Choix invalide.")

if __name__ == "__main__":
    main()

