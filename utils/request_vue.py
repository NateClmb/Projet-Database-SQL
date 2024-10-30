"""
Paquetage des fonctions permettant de créer une vue
"""

####################################################################
###################     Fonction annexe     ########################
####################################################################

def supprimer_vue(conn):
    """
    But de la requête :
    Supprimer la vue pour pouvoir en recréer une nouvelle si besoin
        
    :param conn: Connexion à la base de données
    """
    
    
    cur = conn.cursor()
       
    # Execution de la requête SQL 
    cur.execute("""
                DROP VIEW IF EXISTS Clients_View
                """)
    
    rows = cur.fetchall()

    for row in rows:
        print(row)
        
####################################################################
###################    Première fonction    ########################
####################################################################

def creation_vue(conn):
    """
    But de la requête :
    Créer une vue affichant les informations de base du client ainsi que son âge calculé et le nombre total de commandes qu'il a passé
        
    :param conn: Connexion à la base de données
    """
    
    cur = conn.cursor()
    # On supprime au préalable la vue si elle existe pour éviter d'avoir des erreurs (appel à une fonction annexe)
    supprimer_vue(conn)
    
    # Exécution de la requête SQL
    cur.execute("""
                CREATE VIEW Clients_View AS
                SELECT
                    numero_client,
                    nom_client,
                    prenom_client,
                    date_naiss_client,
                    (strftime('%Y', 'now') - strftime('%Y', date_naiss_client)) -
                    (strftime('%m-%d', 'now') < strftime('%m-%d', date_naiss_client)) AS age_client,
                    adresse_client,
                    COUNT(numero_commande) AS nb_commande_client
                FROM Clients C
                LEFT JOIN Commandes Cmd USING (numero_client)
                GROUP BY numero_client, nom_client, prenom_client, date_naiss_client, adresse_client
                """)
    
    rows = cur.fetchall()

    for row in rows:
        print(row)
        
    print("\nVue terminée sans erreur")