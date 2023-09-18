def mots_Nlettres(lst_mot:list, n:list):
    """Génère une liste de mots contenant n lettres

    Args:
        lst_mot (list): _description_
        n (list): _description_

    Returns:
        _type_: _description_
    """
    lst = []
    for mot in lst_mot:
        if len(mot) == n:
            lst.append(mot)
    return lst

def commence_par(mot, prefixe):
    """Check si le mot commence par le prefixe

    Args:
        mot (_type_): _description_
        prefixe (_type_): _description_

    Returns:
        _type_: _description_
    """
    mot=mot.lower()
    prefixe=prefixe.lower()
    if mot.startswith(prefixe):
        return True
    else:
        return False

def finit_par(mot, suffixe):
    """Check si le mot finit par le suffixe

    Args:
        mot (_type_): _description_
        suffixe (_type_): _description_

    Returns:
        _type_: _description_
    """
    mot=mot.lower()
    suffixe=suffixe.lower()
    if mot.endswith(suffixe):
        return True
    else:
        return False
    
def finissent_par(lst_mots:list, suffixe:str):
    """Génère une liste de mots finissant par le suffixe

    Args:
        lst_mots (list): _description_
        suffixe (str): _description_

    Returns:
        _type_: _description_
    """
    lst = []
    for mot in lst_mots:
        if mot.endswith(suffixe):
            lst.append(mot)
    return lst

def commencent_par(lst_mots:list, prefixe:str):
    """Génère une liste de mots commençant par le prefixe

    Args:
        lst_mots (list): _description_
        prefixe (str): _description_

    Returns:
        _type_: _description_
    """
    lst = []
    for mot in lst_mots:
        if mot.startswith(prefixe):
            lst.append(mot)
    return lst

def liste_mots(lst_mots:list, prefixe:str, suffixe:str, n:int):
    """Génère une liste de mots commençant par le prefixe, finissant par le suffixe et contenant n lettres

    Args:
        lst_mots (list): _description_
        prefixe (str): _description_
        suffixe (str): _description_
        n (int): _description_

    Returns:
        _type_: _description_
    """
    lst = []
    for mot in lst_mots:
        if mot.startswith(prefixe) and mot.endswith(suffixe) and len(mot) == n:
            lst.append(mot)
    return lst

def dictionnaire(fichier:str):
    """Génère un dictionnaire à partir d'un fichier

    Args:
        fichier (str): _description_

    Returns:
        _type_: _description_
    """
    with open(fichier, "r") as f:
        lst = f.readlines()
    for i in range(len(lst)):
        lst[i] = lst[i].strip()
    return lst

lst_mots=["jouer","bonjour", "punir", "jour", "aurevoir", "revoir", "pouvoir", "cour", "abajour",
"finir", "aimer"]
print("mots en 4 lettres:",mots_Nlettres(lst_mots, 4,),"\n")
print("mots en 5 lettres:",mots_Nlettres(lst_mots, 5,),"\n")
print("mots en 6 lettres:",mots_Nlettres(lst_mots, 6,),"\n")
print("mots en 7 lettres:",mots_Nlettres(lst_mots, 7,),"\n")

print("commence par 'jour':",commence_par("Journal", "jour"),"\n")
print("finit par 'a':",finit_par("baba", "a"),"\n")
lst=["patate", "tomate", "pomme", "poire", "frate", "batte"]
print("mots finissant par 'te':",finissent_par(lst, "te"),"\n")
print("mots commençant par 'po':",commencent_par(lst, "po"),"\n")
print("mots commençant par 'pa' et finissant par 'te' et ayant 6 lettres :",liste_mots(lst, "pa", "te", 6),"\n")
print(dictionnaire("C:\wamp64\www\Jacques\L3\Ateliers de programmation\Atelier 3\littre.txt"))