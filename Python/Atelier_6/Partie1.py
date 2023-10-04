def listeMultiples(binf:int, bsup:int, nb:int)->list:
    """Retourne une liste d'entiers multiples de nb et compris entre binf et bsup

    Args:
        binf (int): limite basse
        bsup (int): limite haute
        nb (int): multiple

    Returns:
        list: liste de multiples de nb compris entre binf et bsup
    """
    return [i for i in range(binf, bsup+1) if i%nb == 0]

binf = 5
bsup = 10
nb = 2
print("listeMultiples =",listeMultiples(binf, bsup, nb))

def ajouter(lst:list, nb:int)->list:
    """Ajoute nb à tous les éléments de lst

    Args:
        lst (list): liste d'entiers
        nb (int): nombre a additionner a chaque élément de lst

    Returns:
        list: résultat de l'addition
    """
    return [i+nb for i in lst]

lst = [1,2,3,4,5]
nb = 2
print("ajouter =",ajouter(lst, nb))

def ajouterSiSup(lst:list, val:int, nb:int)->list:
    """Ajoute nb aux éléments de lst qui sont supérieurs a val

    Args:
        lst (list): _description_
        val (int): _description_
        nb (int): _description_

    Returns:
        list: _description_
    """
    return[i+nb for i in lst if i >= val]

lst = [1,2,3,4,5]
nb = 4
val = 3
print("ajouterSiSup =",ajouterSiSup(lst, val, nb))