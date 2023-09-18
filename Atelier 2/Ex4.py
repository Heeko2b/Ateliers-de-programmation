from Ex1 import val_max
def histo (F:list) -> list :
    """Compte le nombre d'entiers présents dans la liste

    Args:
        F (list): _description_

    Returns:
        list: _description_
    """
    #On crée une liste vide de la taille du plus grand entier de la liste
    max=val_max(F)
    crea=0
    compte = []
    while crea < max :
        compte.append(0)
        crea+=1
    #On compte le nombre d'occurences de chaque entier
    for i in range(len(F)) :
        compte[F[i]-1]+=1
    return compte

def est_injective(F:list) -> bool :
    """Teste si il y a des doublons dans la liste, renvoie true si il n'y en a pas, et false si il y en a

    Args:
        F (list): _description_

    Returns:
        bool: _description_
    """
    test= histo(F)
    result = True
    i=0
    while i < len(test) :
        if test[i] > 1 :
            result = False
        i+=1
    return result

def est_surjective(F:list) -> bool :
    """_summary_

    Args:
        F (list): _description_

    Returns:
        bool: _description_
    """
    test= histo(F)
    result = True
    i=0
    while i < len(test) :
        if test[i] == 0 :
            result = False
        i+=1
    return result

def est_bijective(F:list) -> bool :
    """_summary_

    Args:
        F (list): _description_

    Returns:
        bool: _description_
    """
    test= histo(F)
    result = True
    i=0
    while i < len(test) :
        if test[i] == 0 or test[i] > 1:
            result = False
        i+=1
    return result


def afficheHisto(L:list):
    h=histo(L)
    MAXOCC=val_max(h)
    print("TEST HISTOGRAMME\n",L,"\n")
    #boucle pour placer les # en fonction de MAXOCC
    while MAXOCC > 0:
        i=0
        print("     ", end="")
        for i in h:
            print("  ", end="")
            if i >= MAXOCC:
                print("#", end=" ")
            else:
                print(" ", end=" ")
        print()
        MAXOCC-=1
    #boucle pour placer les chiffres en dessous
    barre=0
    e=0
    while barre <= val_max(L):
        print("| --", end="")
        barre+=1
    print("|")
    while e <= val_max(L):
        if e < 10:
            print("  ",e, end="")
        else:
            print(" ",e, end="")
        e+=1
    """for i in range(len(L)):
        print(" ",L[i], end=" ")"""
    return ""
liste = [1, 5, 5, 5, 9, 11, 11, 15, 15, 15]
injective = [0,1,2,3,4,5,6,7,8,9]
#print(histo(liste))
#print(est_injective(liste))
#print(est_injective(injective))
#print(est_surjective(liste))
#print(est_bijective(liste))
afficheHisto(liste)