import numpy as np
        
def my_searchsorted(table : object, indice : int )-> int:
    """Fonction searchsorted de numpy version maison

    Args:
        table (object): _description_
        indice (int): _description_

    Returns:
        int: _description_
    """
    if table.size == 0:
        return -1
    len_table = len(table) #longueur de la table, pour éviter de la recalculer à chaque fois
    for i in range(len_table):
        if table[i] == indice:
            return i
    return len_table

#Exemple d’usage de la fct searchsorted
arr = np.array([6, 7, 8, 9])
x = my_searchsorted(arr, 8)
print(x)

def my_where(table : object, indice : int )-> list:
    """Version maison de la fonction where de NumPy

    Args:
        table (object): _description_
        indice (int): _description_

    Returns:
        list: _description_
    """
    result = []
    for i in range(len(table)):
        if table[i] == indice:
            result.append(i)
    return result

#Exemple pour la fonction my_where
arr = np.array([1, 2, 3, 4, 5, 4, 4])
print("where:",np.where(arr%2 == 0))
print("my_where:",my_where(arr%2, 0),"\n")

#Addition de matrice
def my_add(tableA:object, tableB: object)->object:
    """Vérifie que les matrices ont la même dimension, puis les additionne

    Args:
        tableA (object): matrice A
        tableB (object): matrice B

    Returns:
        object: matrice A + B
    """
    
    if tableA.shape != tableB.shape: #Renvoie une erreur si les tables sont de tailles différentes
        return None
    else:
        result = np.zeros(tableA.shape, dtype=int) #Crée une matrice de la même taille que tableA, remplie de zéros.
        for i in range(tableA.shape[0]):
            for j in range(tableA.shape[1]):
                result[i][j] = tableA[i][j] + tableB[i][j]
    return result

#test de my_add
A = np.array([[14, 20], [15, 2]])
B = np.array([[8, 13], [24, 30]])
print("add =",np.add(A,B))
print("my_add =",my_add(A, B))

M=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("M =",M)
M_plus_10= M + 10
print("M + 10 =",M_plus_10)
M_fois_2= M * 2
print("M x 2 =",M_fois_2)
print("Deuxième ligne de M :",M[1])
print("Troisième colonne de M :",M[:,2])