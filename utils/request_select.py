"""
Paquetage des fonctions de sélection de différentes données dans les tables
"""

from utils import verif_format

####################################################################
###################    Premiere fonction    ########################
####################################################################

def select_nb_reparations(conn, nom_recherche, prenom_recherche):
    """
    But de la requête :
    Cette recherche renvoie le numero du telephone, son modele, le numero de commande, le nom du client et le nombre de réparations du téléphone
    
    :param conn: Connexion à la base de données
    :param nom_recherche: Nom du client
    :param prenom_recherche: Prénom du client
    """
    
    # Vérification de type (isinstance est une fonction python permettant de vérifier le type d'une variable, ici les paramètres de la fonction)
    if not isinstance(nom_recherche, str) or not isinstance(prenom_recherche, str):
        print("\nERREUR : Les noms et prénoms doivent être des chaînes de caractères !")
        return
    
    # Vérification de longueur (len est une fonction python permettant de connaitre la longueur d'une chaîne)
    if len(nom_recherche) <= 0 or len(prenom_recherche) <= 0:
        print("\nERREUR : Les noms et prénoms ne peuvent pas être des chaînes vides !")
        return
    
    # Vérification du format du nom (verifier_format_nom_prenom est une fonction permettant de vérifier la validité du nom et du prénom du client)
    if not verif_format.est_nom_prenom(nom_recherche):
        print("\nERREUR : Le format attendu pour le nom n'est pas bon !")
        return
    
    # Vérification du format du prénom
    if not verif_format.est_nom_prenom(prenom_recherche):
        print("\nERREUR : Le format attendu pour le prénom n'est pas bon !")
        return
    
    # Grâce à ces vérifications on se protège contre d'éventuels erreurs de saisies de l'utilisateur
    
    cur = conn.cursor()
    # Exécution de la requête SQL
    cur.execute("""
                SELECT T.numero_telephone AS NumeroTelephone, T.nom_modele AS Modele, Cmd.numero_commande AS NumeroCommande, C.nom_client AS Nom, COUNT(P.numero_piece) AS NbReparations 
                FROM Telephones T
                JOIN Commandes Cmd USING (numero_commande)
                JOIN Clients C USING (numero_client)
                LEFT JOIN Reparations R ON T.numero_telephone = R.numero_telephone
                LEFT JOIN Pieces P ON R.numero_piece = P.numero_piece
                WHERE C.nom_client = :nom AND C.prenom_client = :prenom
                GROUP BY T.numero_telephone, T.nom_modele, Cmd.numero_commande, C.nom_client;
                """, {'nom': nom_recherche, 'prenom': prenom_recherche})



    rows = cur.fetchall()

    for row in rows:
        print(row)
        
    print("\nRequête terminée sans erreur")


####################################################################
###################    Deuxieme fonction    ########################
####################################################################

def select_infos_client_nb_reparation_variant(conn, ope_bin):
    """
    But de la requête :
    Sélectionner les informations des clients qui ont acheté un téléphone qui n'a pas été réparé
    
    :param conn: Connexion à la base de données
    :param ope_bin: Opérateur binaire servant à la comparaison du nombre de réparations
    :param nb_rep: Nombre de réparations 
    """
    # Vérification de la validité de l'opérateur binaire
    if ope_bin not in ['<>', '=', '!=', '>', '<', '<=', '>=']:
        print("\nERREUR : L'opérateur binaire doit être une chaîne de caractères valide parmi ['<>', '=', '!=', '>', '<', '<=', '>='].")
        return
    
    try:
        nb_rep = str(int(input("Donner un nombre de réparation : ")))
    except ValueError:
        print("\nERREUR : Le nombre de réparations doit être un entier.")
        return

    
    cur = conn.cursor()
    # Exécution de la requête SQL
    cur.execute(f"""
                WITH NbReparationParTelephone AS(
                    SELECT T.numero_telephone, COUNT(R.numero_piece) AS NbReparations
                    FROM Telephones T
                    LEFT JOIN Reparations R USING (numero_telephone)
                    GROUP BY T.numero_telephone
                )
                SELECT C.numero_client AS ID, C.nom_client AS Nom, C.prenom_client AS Prenom, C.date_naiss_client AS DateNaissance, C.adresse_client AS Adresse
                FROM Clients C
                JOIN Commandes USING (numero_client)
                JOIN Telephones USING (numero_commande)
                JOIN NbReparationParTelephone USING (numero_telephone)
                WHERE NbReparations {ope_bin} :nb_rep
                """,  {'nb_rep': nb_rep})

    rows = cur.fetchall()

    for row in rows:
        print(row)
        
    print("\nRequête terminée sans erreur")
    

####################################################################
###################    Troisieme fonction    #######################
####################################################################

def select_telephones_non_repares(conn):
    """
    But de la requête :
    Selectionner le numero, état et nom de modèle des téléphones non réparés
        
    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    # Exécution de la requête SQL
    cur.execute("""
                SELECT T.numero_telephone, T.etat_telephone, T.nom_modele
                FROM Telephones T
                EXCEPT 
                SELECT T.numero_telephone, T.etat_telephone, T.nom_modele
                FROM Telephones T
                JOIN Reparations USING (numero_telephone)
                """)


    rows = cur.fetchall()

    for row in rows:
        print(row)
        
    print("Requête terminée sans erreur")
    