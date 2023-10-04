import re

def full_name(str:str) -> str:
    """_summary_

    Args:
        str (str): _description_

    Returns:
        str: _description_
    """
    if str.strip() !="": #Si la chaine est vide, on return un " ", sinon on continue
        split=str.split() #On crée une liste qui split les mots de la chaine et les attribue chacun a un indice
        split[0]=split[0].upper() #On met le nom de famille en majuscule
        for i in range(1, len(split)):
            split[i]=split[i].capitalize() #On met la première lettre de chaque prénom en majuscule
        return " ".join(split) #Renvoie la chaine de caractère avec les mots de la liste séparés par un espace
    else:
        return " "

def is_mail(str:str) -> (int, int):
    """_summary_

    Args:
        str (str): _description_
        int (_type_): _description_

    Returns:
        _type_: _description_
    """
    #On test si il y a un arobase dans le mail
    arobase=str.count("@")
    if arobase != 1:
        return (0, 2)
    splited=str.split("@")
    #On cherche si le corp du mail commence ou termine par un point, si oui on renvoie (0, 1)
    result= re.search("^(?!.*\.\.)(?!^\.|.*\.$)[a-zA-Z0-9\-_]*$", splited[0])
    #^(?!.*\.\.) = ne contient pas deux points d'affilés
    #(?!^\.|.*\.$) = ne commence pas par un point ou ne termine pas par un point
    #[a-zA-Z0-9\-_]*$ = contient des lettres, des chiffres, des tirets et des underscores
    if not result:
        return (0, 1)
    domaine= re.search("^(?!.*\.\.)(?!^\.)[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*$", splited[1])
    #^(?!.*\.\.) = ne contient pas deux points d'affilés
    #(?!^\.) = ne commence pas par un point
    #[a-zA-Z0-9-]+ = contient des lettres, des chiffres et des tirets, une ou plusieurs fois
    #(\.[a-zA-Z0-9-]+)*$ = idem, mais doit commencer par un "."
    if not domaine:
        return (0, 3)
    #On cherche si il y a un point avant le suffixe du mail, si oui on renvoie (0, 4)
    point= re.search("\.[a-zA-Z]{0,3}$", splited[1])
    if not point:
        return (0, 4)
    else:
        return (1, 0)
    
    
print(full_name("smengi anthony"))
print(is_mail("bisgambiglia@univ-corse.fr"))