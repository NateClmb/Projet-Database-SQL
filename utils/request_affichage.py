
"""
Paquetage des fonctions d'affichage des tables de la base de données
"""


####################################################################
###################    Premiere fonction    ########################
####################################################################

def afficher_table_choix(conn, nom_table):
    """
    But de la requête :
    Afficher toutes les informations d'une table choisie par l'utilisateur
        
    :param conn: Connexion à la base de données
    :param nom_table: Nom de la table à afficher
    """
    cur = conn.cursor()
    
    # Vérification de la validité de la table donnée
    if nom_table not in ['Modeles', 'Clients', 'Commandes', 'Telephones', 'Pieces', 'Reparations']:
        print("\n ERREUR : La table entrée n'existe pas")
        return
    
    # Exécution de la requête SQL
    cur.execute(f"""
                SELECT *
                FROM {nom_table}
                """)
    
    rows = cur.fetchall()

    for row in rows:
        print(row)   
        
    print("\nAffichage effectuée sans erreur") 


####################################################################
###################    Deuxieme fonction    ########################
####################################################################

def afficher_toutes_les_tables(conn):
    """
    But de la requête :
    Avoir les informations de toutes les tables les unes à la suite des autres
        
    :param conn: Connexion à la base de données
    """
    
    tables = ['Modeles', 'Clients', 'Commandes', 'Telephones', 'Pieces', 'Reparations']
    cur = conn.cursor()

    # Pour toutes les tables définies
    for table in tables:
        print(f"\nAffichage de la table {table} :")
        # Exécuter la requête SQL
        cur.execute(f"""
                    SELECT *
                    FROM {table}
                    """)
        
        rows = cur.fetchall()

        for row in rows:
            print(row)
            
        print()
        
    print("\nRequête terminée sans erreur")

    
    