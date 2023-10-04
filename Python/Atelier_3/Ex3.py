import random
def places_lettre(ch:str, mot:str)->list:
    """Cherche si le caractère ch est présent dans la chaine de caractère mot, renvoie le ou les indices si oui, une chaine vide si non

    Args:
        ch (str): caractère recherché
        mot (str): mot dans lequel on recherche le caractère

    Returns:
        list: liste contenant les indices du caractère dans le mot
    """
    lst=[]
    for i in range(len(mot)):
        if mot[i]==ch:
            lst.append(i)
    return lst

def outputStr(mot:str, lpos:list)->str:
    """Génère un string avec les lettres de mot aux indices de lpos et des _ sinon

    Args:
        mot (str): mot recherché
        lpos (list): indices des lettres trouvées

    Returns:
        str: string avec les lettres de mot aux indices de lpos et des _ sinon
    """
    s=""
    for i in range(len(mot)):
        if i in lpos:
            s+=mot[i]
        else:
            s+="_"
    return s

"""mot=input("Entrez un mot: ")
char=input("Entrez un caractère: ")
print(places_lettre(char,mot))
#print(outputStr("bon",[0,1,2]))
print(outputStr(mot,places_lettre(char,mot)))"""

def runGame()->None:
    """Jeu du pendu"""

    #Initialisation de la partie
    #Liste de mots
    lst=["paris","londres","madrid","berlin","new-york"]
    #Choix aléatoire d'un mot
    mot=lst[random.randint(0,len(lst)-1)]
    resultat=outputStr(mot,[])
    #Nombre de tentatives
    tentatives = 10
    essai=0
    
    #Déroulement de la partie
    while resultat != mot and essai <= tentatives:
        if tentatives-essai == 1:
            print(tentatives-essai,"tentative restante")
        else:
            print(tentatives-essai,"tentatives restantes")
        char=input("Entrez un caractère: ")
        char=char.lower()
        
        #Recherche des indices du caractère dans le mot
        indices = places_lettre(char, mot)
        #Mise à jour du résultat
        for i in indices:
            resultat = resultat[:i] + char + resultat[i+1:]

        #Ecriture du résultat
        print(resultat.capitalize())
        essai+=1
    
    #Fin de partie
    if resultat != mot:
        print("Perdu, vous avez dépassé le nombre de tentatives")
    else:
        print("Bravo, vous avez trouvé le mot",mot.capitalize())
    
runGame()