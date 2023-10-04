def somme_recursive(liste:list)->int :
    """Récursive qui additionne tous les éléments d'une liste et renvoie un int

    Args:
        liste (list): _description_

    Returns:
        int: _description_
    """
    if liste: #Teste si la liste n'est pas vide
        return liste[0] + somme_recursive(liste[1:])
    else: #Si la liste est vide
        return 0

# Test de la fonction
liste1 = [1, 2, 3, 4, 5]
resultat1 = somme_recursive(liste1)
print("La somme de la liste est :", resultat1)
liste2 = []
resultat2 = somme_recursive(liste2)
print("La somme de la liste est :", resultat2)

def factorielle_recursive(nbr:int)->int:
    """_summary_

    Args:
        nbr (int): _description_
    """
    if nbr != 0:
        return nbr * factorielle_recursive(nbr - 1)
    else:
        return 1
    
# Test de la fonction
nombre = 5
resultat = factorielle_recursive(nombre)
print("Le factoriel de", nombre, "est :", resultat)

def longueur(lst:list)->int:
    """Retourne le nombre d'éléments dans la liste

    Args:
        lst (list): _description_

    Returns:
        int: _description_
    """
    if lst:
        return 1 + longueur(lst[1:])
    else:
        return 0
#Test de la fonction longueur
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]
resultat = longueur(liste)
print("La longueur de la liste est :", resultat)

def find_min(liste:list)->int:
    """Trouve le minimum de la liste et le retourne

    Args:
        liste (list): _description_

    Returns:
        int: _description_
    """
    if not liste:
        return None
    elif len(liste) == 1:
        return liste[0]
    elif liste[0] < find_min(liste[1:]):
        return liste[0]
    else:
        return find_min(liste[1:])

def find_min_v2(liste:list)->int:
    """Pareil que find_min mais avec un seul return

    Args:
        liste (list): _description_

    Returns:
        int: _description_
    """
    if not liste:
        return None
    elif len(liste) == 1:
        min = liste[0]
    else:
        min = find_min(liste[1:])
        if liste[0] < min: #Si liste[0] est plus grand que min, la récursivité se lance
            min = liste[0] #min prend la valeur de liste[0], la récursivité se termine
    return min
    
#Test de la fonction find_min
liste = [5, 14, 3, 4, 5, 6, 7, 8, 9]
resultat = find_min_v2(liste)
print("La valeur minimale de la liste est :", resultat)

def listePairs(liste:list)->int:
    """Retourne une liste des éléments paires de la liste

    Args:
        liste (list): _description_

    Returns:
        int: _description_
    """
    pairs = []
    if not liste:
        return []
    elif liste[0] % 2 == 0:
        pairs = [liste[0]] + listePairs(liste[1:])
    else:
        pairs = listePairs(liste[1:])
        """pairs.append(liste[0])#Ajoute la valeur de liste[0] à la liste
    pairs.extend(listePairs(liste[1:])) #Ajoute la liste retournée par la récursivité à la liste pairs (extend ajoute une liste à une autre liste, append ajoute un élément à une liste)"""
    return pairs

#Test de la fonction listPairs
liste = [5, 14, 3, 4, 5, 6, 7, 8, 9]
resultat = listePairs(liste)
print("listePairs:",resultat)

def concat_liste(liste:list)->list:
    """Concatène les listes contenues dans la liste liste et retourne une liste plate constituée des éléments simples

    Args:
        liste (list): _description_

    Returns:
        list: _description_
    """
    if not liste:
        return []
    else:
        return liste[0] + concat_liste(liste[1:])

#Test de la fonction concat_liste
liste = [[1, 2], [3, 4], [5, 6], [7, 8, 9]]
resultat = concat_liste(liste)
print("concat_liste:",resultat)

def separe (liste:list)->tuple:
    """Sépare les valeurs paires des impaires dans un tuple
    
    Args:
        liste (list): Liste d'éléments a séparer

    Returns:
        tuple: Deux listes, une pair une impair
    """
    if not liste:
        return [], []
    else:
        pairs, impairs = separe(liste[1:])#On récupère les valeurs et on les attribue a pairs et impairs
        if liste[0] % 2 == 0: # Si true, alors la valeur va dans pair
            pairs = [liste[0]] + pairs
        else: # Sinon elle va dans impair
            impairs = [liste[0]] + impairs
    return (pairs, impairs)

#Test de la fonction separe
liste = [5, 14, 3, 4, 5, 6, 7, 8, 9]
resultat = separe(liste)
print("separe :",resultat)