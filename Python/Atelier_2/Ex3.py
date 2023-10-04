def separer(lst:list) -> list :
    negatif = []
    neutre = []
    positif = []
    for i in range(len(lst)) :
        if lst[i] < 0 :
            negatif.append(lst[i])
        elif lst[i] == 0 :
            neutre.append(lst[i])
        else :
            positif.append(lst[i])
    LSEP= negatif + neutre + positif
    return LSEP

liste = [0,1,2,3,-4,5,6,-7,-8,9,0,10]
print(separer(liste))