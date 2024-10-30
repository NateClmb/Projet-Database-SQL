"""
Paquetage de la fonction permettant de supprimer des données dans une table de la base de données
"""

import sqlite3
from utils import request_affichage
from utils import verif_format

####################################################################
###################    Premiere fonction    ########################
####################################################################

def supprimer_donnees(conn, nom_table):
    """
    But de la requête :
    Supprimer des données dans une table   
    !!! Attention aux contraintes d'intégrité !!! 
    Ordre de suppression à respecter : Reparations -> Pieces -> Telephones -> Commandes -> Clients -> Modeles
    
    :param conn: Connexion à la base de données
    :param nom_table: Nom de la table dans laquelle supprimer des données
    """
    cur = conn.cursor()
    
    nb_err = 0

    try:
        # En fonction du nom de la table donnée par l'utilisateur on vérifie si l'élément qu'il veut supprimer est présent ou non
        # Cela nous permet d'éviter d'effectuer des suppressions d'éléments non présents et donc d'éviter des erreurs même si cela allonge le code de la fonction
        if nom_table == 'Modeles':
            modele = input("Entrer le nom exact du modèle à supprimer : ")
            cur.execute("SELECT COUNT(*) FROM Modeles WHERE nom_modele = ?", [modele])
            
        elif nom_table == 'Clients':
            try:
                client = str(int(input("Entrer le numéro (id) du client à retirer : ")))
            except ValueError:
                print("\nERREUR : le numéro de client doit être un entier positif")
                return
            cur.execute("SELECT COUNT(*) FROM Clients WHERE numero_client = ?", [client])

            
        elif nom_table == 'Commandes':
            try:
                commande = str(int(input("Entrer le numéro de la commande à supprimer : ")))
            except ValueError:
                print("\nERREUR : Le numéro de commande doit être un entier positif")
                return
            cur.execute("SELECT COUNT(*) FROM Commandes WHERE numero_commande = ?", [commande])

            
        elif nom_table == 'Telephones':
            telephone = input("Entrer le numéro (id) du téléphone à supprimer : ")
            try:
                telephone = str(int(telephone))
            except ValueError:
                print("\nERREUR : Le numéro de téléphone doit être un entier positif")
                return
            cur.execute("SELECT COUNT(*) FROM Telephones WHERE numero_telephone = ?", [telephone])
            
        elif nom_table == 'Pieces':
            piece = input("Entrer le numéro de la pièce à supprimer : ")
            try:
                piece = str(int(piece))
            except ValueError:
                print("\nERREUR : Le numéro de pièce doit être un entier positif")
                return
            cur.execute("SELECT COUNT(*) FROM Pieces WHERE numero_piece = ?", [piece])
            
        elif nom_table == 'Reparations':
            telephone = input("Entrer le numéro de téléphone à supprimer : ")
            piece = input("Entrer le numéro de la pièce à supprimer : ")
            try:
                telephone = str(int(telephone))
                piece = str(int(piece))
            except ValueError:
                print("\nERREUR : Le numéro de téléphone et le numéro de pièce doivent être des entiers positifs")
                return
            cur.execute("SELECT COUNT(*) FROM Reparations WHERE numero_telephone = ? AND numero_piece = ?", [telephone, piece])
            
        
        else:
            print("Nom de table invalide !")
            nb_err = 1
    
        # Si le nom de la table est correct
        if nb_err == 0:
            # Vérifier si l'élément existe dans la table
            count = cur.fetchone()[0]
            # S'il n'y est pas, message d'erreur
            if count == 0:
                print("\nL'élément à supprimer n'existe pas dans la table.")
            elif nb_err == 0:
                # Sinon, exécuter la requête SQL en fonction de la table donnée
                if nom_table == 'Modeles':
                    cur.execute("DELETE FROM Modeles WHERE nom_modele = ?", [modele])
                elif nom_table == 'Clients':
                    cur.execute("DELETE FROM Clients WHERE numero_client = ?", [client])
                elif nom_table == 'Commandes':
                    cur.execute("DELETE FROM Commandes WHERE numero_commande = ?", [commande])
                elif nom_table == 'Telephones':
                    cur.execute("DELETE FROM Telephones WHERE numero_telephone = ?", [telephone])
                elif nom_table == 'Pieces':
                    cur.execute("DELETE FROM Pieces WHERE numero_piece = ?", [piece])
                elif nom_table == 'Reparations':
                    cur.execute("DELETE FROM Reparations WHERE numero_telephone = ? AND numero_piece = ?", [telephone, piece])
                
                
                rows = cur.fetchall()
                print()
                for row in rows:
                    print(row)
                
                print("\nSuppression effectuée sans erreur")
                
                # Afficher la table pour vérifier la suppression
                rep = input("\nVoulez-vous afficher la table pour vérifier que la suppression s'est bien déroulée ? (o/n) : ")
                if rep == 'o':
                    request_affichage.afficher_table_choix(conn, nom_table) 
        
            
    except sqlite3.Error as e:
        print("Erreur lors de la suppression des données :", e)
        return
        
    conn.commit()  # Valider les changements une fois que toutes les suppressions sont terminées
    
    