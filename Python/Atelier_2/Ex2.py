def position(liste,elt) :
    """Cherche elt dans liste et renvoie sa position si il est présent

    Args:
        liste (list): _description_
        elt (int): _description_

    Returns:
        int: _description_
    """
    for i in range(len(liste)) :
        if liste[i] == elt :
            return i
    return -1

def position_while(liste,elt) :
    """Cherche elt dans liste et renvoie sa position si il est présent

    Args:
        liste (list): _description_
        elt (int): _description_

    Returns:
        int: _description_
    """
    i = 0
    while i < len(liste) :
        if liste[i] == elt :
            return i
        i+=1
    return -1

def nb_occurences(liste,elt) :
    """Cherche elt dans liste et renvoie le nombre d'occurences de elt

    Args:
        liste (list): _description_
        elt (int): _description_

    Returns:
        int: _description_
    """
    occurences = 0
    for i in range(len(liste)) :
        if liste[i] == elt :
            occurences+=1
    return occurences

def est_triee(liste) :
    """Teste si liste est triée

    Args:
        liste (list): _description_

    Returns:
        bool: _description_
    """
    for i in range(len(liste)-1) :
        if liste[i] > liste[i+1] :
            return False
    return True

def est_triee_while(liste) :
    """Teste si liste est triée

    Args:
        liste (list): _description_

    Returns:
        bool: _description_
    """
    i = 0
    while i < len(liste)-1 :
        if liste[i] > liste[i+1] :
            return False
        i+=1
    return True

def position_tri(liste, elt) :
    """Cherche e dans liste triée et renvoie sa position si il est présent

    Args:
        liste (list): _description_
        e (int): _description_

    Returns:
        int: _description_
    """
    debut = 0
    fin = len(liste)-1
    val = 0
    mil = len(liste)//2
    trouvé = False

    while debut < fin and not trouvé :
        if elt == liste[mil]:
            trouvé = True
            val = mil
        elif elt > liste[mil] :
            debut=mil
        else:
            fin=mil
        mil = (debut+fin)//2
        