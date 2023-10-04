import random

def choose_element_list(liste:list)->list:
    """Génère une liste de n entiers aléatoires compris entre int_binf et int_bsup

    Args:
        ch (str): _description_
        mot (str): _description_

    Returns:
        list: _description_
    """
    return liste[random.randint(0, len(liste)-1)]

liste=[87,23,589,29,10,589,20]
print("Liste originelle:",liste)
print("Tirage au sort:",choose_element_list(liste))