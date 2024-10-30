"""
Paquetage annexe permettant la vérification des différents format entrés par l'utilisateur, il n'y a pas est_nombre car on utilise except ValueError pour mieux gérer les cas 
"""

####################################################################
###################     Fonction annexe 1    #######################
####################################################################
    
def est_nom_prenom(chaine):
    """
    Vérifie si le format du prénom est valide.

    Le prénom doit commencer par une lettre et peut contenir des lettres,
    des tirets et des espaces, mais ne peut pas contenir de chiffres ou uniquement des tirets
    ou des espaces.

    Entrée :
        chaine (str): Le prénom ou nom à vérifier.

    Sortie :
        bool: True si le format est valide, False sinon.
    """
    # Si le prénom est vide, il est invalide
    if not chaine:
        return False
    
    # Vérifier si le prénom commence par une lettre
    if not chaine[0].isalpha():
        return False

    # Si le prénom contient uniquement des tirets ou des espaces, il est invalide
    if chaine.strip('- ') == '':
        return False 

    # Si aucune des conditions ci-dessus n'est satisfaite, le prénom est valide
    return True


####################################################################
###################     Fonction annexe 3    #######################
####################################################################


def est_date(date):
    """
    Vérifie si le format de la date est valide (YYYY-MM-DD).

    Args:
        date (str): La date à vérifier.

    Returns:
        bool: True si le format est valide, False sinon.
    """
    try:
        # Vérification de la longueur de la chaîne
        if len(date) != 10:
            print("\nERREUR : Le format de la date n'est pas le bon (YYYY-MM-DD)")
            return False
        
        # Séparation de l'année, du mois et du jour
        annee, mois, jour = map(int, date.split('-'))
        
        # Vérification des limites des valeurs
        if not (1 <= mois <= 12):
            print("\nERREUR : Le nombre de mois invalide")
            return False
        
        # Vérification des jours pour chaque mois
        if mois in [1, 3, 5, 7, 8, 10, 12]:
            if not (1 <= jour <= 31):
                print("\nERREUR : Nombre de jours invalide")
                return False
        elif mois in [4, 6, 9, 11]:
            if not (1 <= jour <= 30):
                print("\nERREUR : Nombre de jours invalide")
                return False
        else:  # Février
            if annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0):
                if not (1 <= jour <= 29):
                    print("\nERREUR : Nombre de jours invalide")
                    return False
            else:
                if not (1 <= jour <= 28):
                    print("\nERREUR : Nombre de jours invalide")
                    return False
        
        # Si toutes les conditions sont satisfaites, la date est valide
        return True
    
    except ValueError:
        # En cas de ValueError lors de la conversion en entier, la date est invalide
        return False
