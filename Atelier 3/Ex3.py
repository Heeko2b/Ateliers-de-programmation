def places_lettre(ch:str, mot:str)->list:
    """Cherche si le caractère ch est présente dans la chaine de caractère mot, renvoie le ou les indices si oui, une chaine vide si non

    Args:
        ch (str): _description_
        mot (str): _description_

    Returns:
        list: _description_
    """
    lst=[]
    for i in range(len(mot)):
        if mot[i]==ch:
            lst.append(i)
    return lst

def outputStr(mot:str, lpos:list)->str:
    """Génère un string avec les lettres de mot aux indices de lpos et des _ sinon

    Args:
        mot (str): _description_
        lpos (list): _description_

    Returns:
        str: _description_
    """
    s=""
    for i in range(len(mot)):
        if i in lpos:
            s+=mot[i]
        else:
            s+="_"
    return s

mot=input("Entrez un mot: ")
char=input("Entrez un caractère: ")
print(places_lettre(char,mot))
print(outputStr("bon",[0,1,2]))
#print(outputStr(mot,places_lettre(char,mot)))