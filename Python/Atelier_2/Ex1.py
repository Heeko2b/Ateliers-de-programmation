def somme(L : list) -> int:
    """_summary_

    Args:
        L (list): _description_

    Returns:
        int: _description_
    """
    addition = 0
    for i in range(len(L)) :
        addition += L[i]
        '''print("i =",L[i],)
        print("a =",addition,"\n")'''
    return addition

def test_exercice1 ():
    print("TEST SOMME")
    #test liste vide
    print("Test liste vide : ", somme([]))
    #test somme 11111
    lst2test1=[1,10,100,1000,10000]
    print("Test somme 111 : ", somme(lst2test1),"\n")

def moyenne(L : list) -> int:
    """_summary_

    Args:
        L (list): _description_

    Returns:
        int: _description_
    """
    if len(L)==0:
        resultat=0
    else:
        resultat=somme(L)/len(L)
    return resultat

def test_moyenne():
    print("TEST moyenne")
    #test liste vide
    print("Test liste vide : ", moyenne([]))
    #test somme 11111
    lst2test2=[1,10,100,1000,10000]
    print("Test somme 111 : ", moyenne(lst2test2),"\n")

def nb_sup(L:list,e:int)->int:
    """_summary_

    Args:
        L (list): _description_
        e (int): _description_

    Returns:
        int: _description_
    """
    sup = 0
    for i in range(len(L)) :
        if L[i] > e:
            sup+=1
    return sup

def somme_for(L) :
    addition = 0
    for i in L :
        addition += i
        '''print("i =",i,)
        print("a =",addition,"\n")'''
    return addition

def moyenne_for(L) :
    if len(L) == 0:
        resultat=0
    else:
        resultat=somme(L)/len(L)
    return resultat

def nb_sup_for(L,e) :
    sup = 0
    for i in L :
        if i > e:
            sup+=1
    return sup

def somme_while(L) :
    addition = 0
    i = 0
    while i < len(L) :
        addition += L[i]
        '''print("i =",L[i],)
        print("a =",addition,"\n")'''
        i+=1
    return addition

def moyenne_while(L) :
    if len(L) == 0:
        resultat=0
    else:
        resultat=somme(L)/len(L)
    return resultat

def nb_sup_while(L,e) :
    sup = 0
    for i in L :
        if i > e:
            sup+=1
    return sup

def moy_sup(L:list,e:int)->int:
    """_summary_

    Args:
        L (list): _description_
        e (int): _description_

    Returns:
        int: _description_
    """
    Lsup = []
    for i in range(len(L)) :
        if L[i] > e:
            Lsup.append(L[i])
    return moyenne(Lsup)

def moy_supv2(L:list,e:int)->int:
    som=0
    for i in L:
        if i > e:
            som += i
    return moyenne(som)

def val_max(L : list) -> int:
    """_summary_

    Args:
        L (list): _description_

    Returns:
        int: _description_
    """
    i=0
    valeur_max = 0
    while i < len(L):
        if valeur_max < L[i]:
            valeur_max = L[i]
        i+=1
    return valeur_max

def ind_max(L : list) -> int:
    """_summary_

    Args:
        L (list): _description_

    Returns:
        int: _description_
    """
    max = 0
    while max < len(L):
        max+=1
    return L[max-1]

#test_exercice1()
#test_moyenne()
liste = [1,2,3,4,52,6,7,8,9]
print(nb_sup(liste,3))
print(moy_sup(liste,3))
print(val_max(liste))
print(ind_max(liste))
#somme (L = [1,2,3,4,5])
