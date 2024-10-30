"""
Paquetage de la fonction permettant d'insérer des données dans une table de la base de données
"""

import sqlite3
from utils import request_affichage
from utils import verif_format

####################################################################
###################    Premiere fonction    ########################
####################################################################

def inserer_donnees(conn, nom_table):
    """
    But de la requête :
    Insérer de nouvelles données dans une table choisie par l'utilisateur 
    !!! Attention !!! Les valeurs sont restreintes pour respecter les contraintes d'intégrité
            
    :param conn: Connexion à la base de données
    :param nom_table: Nom de la table dans laquelle insérer des données
    """
    cur = conn.cursor()
    
    nb_err = 0
    try:
        # En fonction de la table donnée par l'utilisateur on va vérifier si l'élément à ajouter et déjà présent ou non dans la table
        # Cela nous permet d'éviter d'insérer des valeurs déjà présentes dans la table et donc d'éviter des erreurs même si cela allonge le code de la fonction
        if nom_table == 'Modeles':
            # Aucune vérification de type pour les modèles
            nom_modele = input("Entrer le nom du modèle : ")
            marque_modele = input("Entrer la marque associée au modèle : ")
            cur.execute("SELECT COUNT(*) FROM Modeles WHERE nom_modele = ?", [nom_modele])
            
        elif nom_table == 'Clients':
            try :
                numero_client = str(int(input("Entrer le numéro (id) du client à ajouter (doit être différent des id de la table et compris entre 1 et 99) : ")))
            except ValueError:
                print("\nERREUR : Le numéro de client doit être un entier positif")
                return
            nom_client = input("Entrer le nom du client : ")
            if verif_format.est_nom_prenom(nom_client):
                prenom_client = input("Entrer le prénom du client : ")
                if verif_format.est_nom_prenom(prenom_client):
                    date_naiss_client = input("Entrer la date de naissance du client (YYYY-MM-DD) : ")
                    if verif_format.est_date(date_naiss_client):
                        adresse_client = input("Entrer l'adresse du client : ")
                        cur.execute("SELECT COUNT(*) FROM Clients WHERE numero_client = ?", [numero_client])
                    else:
                        return
                else:
                    return
            else:
                return
            
            
        elif nom_table == 'Commandes':
            try :
                numero_commande = str(int(input("Entrer le numéro de la commande (doit être unique compris entre 100 et 999) : ")))
                numero_client = str(int(input("Entrer le numéro (id) du client à ajouter (doit être compris dans la table Clients) : ")))
            except ValueError:
                print("\nERREUR : Les numéros de commande et de client doivent être des entiers positifs")
                return
            date_commande = input("Entrer la date de la commande (YYYY-MM-DD) : ")
            if verif_format.est_date(date_commande):
                cur.execute("SELECT COUNT(*) FROM Commandes WHERE numero_commande = ?", [numero_commande])
            else:
                return
            
        elif nom_table == 'Telephones':
            try:
                numero_telephone = str(int(input("Entrer le numéro (id) du téléphone (doit être unique) : ")))
                stockage_telephone = str(int(input("Entrer la capacité de stockage du téléphone : ")))
                numero_commande = int(input("Entrer le numéro de commande associé au téléphone (doit être compris dans la table Commandes) : "))
            except ValueError:
                print("\nERREUR : Le numéro de téléphone, de stockage et de commande doivent être des entiers positifs")
                return
            etat_telephone = input("Entrer l'état du téléphone (excellent, bon, moyen) : ")
            if etat_telephone in ['excellent', 'bon', 'moyen']:
                nom_modele = input("Entrer le modèle du téléphone (doit être compris dans Modeles) : ")
                cur.execute("SELECT COUNT(*) FROM Telephones WHERE numero_telephone = ?", [numero_telephone])
            else:
                print("\nERREUR : L'état entré pour le téléphone est invalide")
                return
            
        elif nom_table == 'Pieces':
            try:
                numero_piece = str(int(input("Entrer le numéro de la pièce (> 1000 et différent de ceux déjà présents) : ")))
            except ValueError:
                print("\nERREUR : Le numéro de pièce doit être un entier positif")
            piece_type_piece = input("Entrer le nom de la pièce (batterie, carte mere, ecran, appareil photo) : ")
            if piece_type_piece in ['batterie', 'carte mere', 'ecran', 'appareil photo']:
                cur.execute("SELECT COUNT(*) FROM Pieces WHERE numero_piece = ?", [numero_piece])
            else:
                print("\nERREUR : Le type de pièce entré est invalide")
                return
            
        elif nom_table == 'Reparations':
            try:
                numero_telephone = str(int(input("Entrer le numéro de téléphone (doit être compris dans la table Telephones) : ")))
                numero_piece = str(int(input("Entrer le numéro de la pièce à réparer (doit être compris dans la table Pieces) : ")))
            except ValueError:
                print("\nERREUR : Les numéros de téléphone et de pièce doivent être des entiers positifs")
                return
            cur.execute("SELECT COUNT(*) FROM Reparations WHERE numero_telephone = ? AND numero_piece = ?", [numero_telephone, numero_piece])
            
        else:
            print("Nom de table invalide !")
            nb_err = 1
    
        if nb_err == 0:
            # Vérifier si l'élément existe déjà dans la table
            count = cur.fetchone()[0]
            # Si l'élément est déjà présent, message d'erreur
            if count > 0:
                print("L'élément à insérer existe déjà dans la table.")
            else:
                # Sinon, exécuter la requête SQL
                if nom_table == 'Modeles':
                    cur.execute("INSERT INTO Modeles VALUES (?, ?)", [nom_modele, marque_modele])
                elif nom_table == 'Clients':
                    cur.execute("INSERT INTO Clients VALUES (?, ?, ?, ?, ?)", [numero_client, nom_client, prenom_client, date_naiss_client, adresse_client])
                elif nom_table == 'Commandes':
                    cur.execute("INSERT INTO Commandes VALUES (?, ?, ?)", [numero_commande, date_commande, numero_client])
                elif nom_table == 'Telephones':
                    cur.execute("INSERT INTO Telephones VALUES (?, ?, ?, ?, ?)", [numero_telephone, stockage_telephone, etat_telephone, nom_modele, numero_commande])
                elif nom_table == 'Pieces':
                    cur.execute("INSERT iNTO Pieces VALUES (?, ?)", [numero_piece, piece_type_piece])
                else:
                    cur.execute("INSERT INTO Reparations VALUES (?, ?)", [numero_telephone, numero_piece])
                
                rows = cur.fetchall()

                for row in rows:
                    print(row)
                
                print("\nInsertion effectuée sans erreur")
                
                # Afficher la table pour vérifier l'insertion
                rep = input("\nVoulez-vous afficher la table pour vérifier que l'insertion s'est bien déroulée ? (o/n) : ")
                if rep == 'o':
                    request_affichage.afficher_table_choix(conn, nom_table) 
        
            
    except sqlite3.Error as e:
        print("Erreur lors de l'insertion des données :", e)
        return     
                            
    conn.commit()  # Valider les changements une fois que toutes les insertions sont terminées
