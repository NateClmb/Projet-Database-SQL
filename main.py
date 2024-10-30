#!/usr/bin/python3

from utils import db
from utils import request_affichage
from utils import request_inserer
from utils import request_select
from utils import request_supprimer
from utils import request_vue

    
####################################################################
###################       Partie main        #######################
####################################################################

def main():

    print("\nBonjour et bienvenue dans ce projet de création/interaction avec une base de données")
        
    # Nom de la BD à créer
    db_file = "data/DB_Projet.db"

    # Créer une connexion a la BD
    conn = db.creer_connexion(db_file)
    conn.set_trace_callback(print)
    
    # Remplir la BD
    print("\n1. On crée la base de données et on l'initialise avec des premières valeurs.\n")
    db.mise_a_jour_bd(conn, "data/Creation_DB.sql")
    db.mise_a_jour_bd(conn, "data/Donnees_OK.sql")

    # Boucle du programme d'appel aux requêtes
    while True:
        
        print(""" 
            Menu principal d'appel aux requêtes :

                - Requête 1 : Affichage d'une table choisie par l'utilisateur
                - Requête 2 : Affichage de toutes les tables
                - Requête 3 : Suppression d'une ligne de données de la table choisie par l'utilisateur
                - Requête 4 : Insertion de données dans une table choisie par l'utilisateur
                - Requête 5 : Informations sur un client et le téléphone qu'il a acheté ainsi que le nombre de réparations du téléphone
                - Requête 6 : Informations sur les clients en fonctions du nombre de réparations de leur(s) téléphone(s)
                - Requête 7 : Affichage des informations des téléphones non réparés
                - Requête 8 : Création de la vue calculant l'âge et le nombre de commandes d'un client
                - Quitter q 
            """)
        
        reponse_user = input("Veuillez taper le numéro de la requête voulue pour l'exécuter ou q pour quitter : ")
        
        
        # 1ere requête
        if reponse_user == '1':
            print("\nRequête 1 | Affichage d'une table choisie par l'utilisateur")
            nom_table = input("\nDonner le nom de la table à afficher : ")
            request_affichage.afficher_table_choix(conn,nom_table)
        
        # 2eme requête
        elif reponse_user == '2':
            print("\nRequête 2 | Liste de toutes les tables")
            request_affichage.afficher_toutes_les_tables(conn)
            
        # 3eme requête
        elif reponse_user == '3':
            print("\nRequête 3 | Suppression d'une ligne de la table choisie par l'utilisateur")
            print("\nAttention à l'ordre de suppression à respecter pour les contraintes d'intégrité : \nReparations -> Pieces -> Telephones -> Commandes -> Clients -> Modeles")
            nom_table = input("\nDonner le nom de la table dans laquelle supprimer une donnée : ")
            request_supprimer.supprimer_donnees(conn, nom_table)
        
        # 4eme requête
        elif reponse_user == '4':
            print("\nRequête 4 | Insertion de données dans une table choisie par l'utilisateur")
            nom_table = input("\nDonner le nom de la table dans laquelle insérer des données : ")
            request_inserer.inserer_donnees(conn,nom_table)
        
        # 5eme requête
        elif reponse_user == '5':
            print("\nRequête 5 | Informations sur un client et le téléphone qu'il a acheté ainsi que son nombre de réparations")
            nom_recherche = input("\nDonner le nom du client : ")
            prenom_recherche = input("Donner le prénom du client : ")
            request_select.select_nb_reparations(conn, nom_recherche, prenom_recherche)
        
        # 6eme requête
        elif reponse_user == '6':
            print("\nRequête 6 | Informations sur les clients en tenant compte du nombre de reparations de leur telephone")
            ope_bin = input("\nDonner un opérateur binaire SQL (ex. = ou <>): ")
            request_select.select_infos_client_nb_reparation_variant(conn, ope_bin)

        # 7eme requête  
        elif reponse_user == '7':
            print("\nRequête 7 | Affichage des informations des téléphones non réparés")
            request_select.select_telephones_non_repares(conn)
            
        # 8eme requête
        elif reponse_user == '8':
            print("\nRequête 8 | Création de la vue calculant l'âge et le nombre de commandes d'un client")
            request_vue.creation_vue(conn) 
            
        elif reponse_user == 'q':
            print("\nMerci d'avoir utilisé cette base de données, à bientôt !\n")
            break

        else:
             print("\nVotre réponse n'est pas comprise dans le choix proposé, réessayez")   
    # Fin du programme        
    
if __name__ == "__main__":
    main()
    