import numpy as np

#Creation de matrice 4x4 avec des valeurs aléatoires entre 0 et 10
M = np.random.randint(0,10,(4,4))
print("M =\n",M)
"""I_4 = np.identity(4)
print("I_4 =\n",I_4)"""

def matrice_trace(matrice:list)->int:
    """Prend une matrice en entrée et retourne la trace de la matrice

    Args:
        matrice (list): _description_
    """
    trace = 0
    for i in range(len(matrice)):
        trace += matrice[i][i]
    return trace

print("Trace de M =",matrice_trace(M))

def est_symetrique(matrice:list)->bool:
    """Prend une matrice en entrée et retourne True si elle est symétrique et False sinon

    Args:
        matrice (list): _description_
    """
    result = True
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if matrice[i][j] != matrice[j][i]:
                result=False
    return result

sym= np.array([[1,2,3],[2,1,4],[3,4,1]])
print("sym =\n",sym)
print("sym est symétrique :",est_symetrique(sym))

def produit_diagonale(matrice:list)->int:
    """Prend une matrice en entrée et retourne la trace de la matrice

    Args:
        matrice (list): _description_
    """
    multi = 1
    for i in range(len(matrice)):
        multi *= matrice[i][i]
    return multi

matrice_produit = np.array([[4,2,3],[2,2,4],[3,4,3]])
print("matrice_produit =\n",matrice_produit)
print("Produit de la diagonale de matrice_produit =",produit_diagonale(matrice_produit))

#Calculez la trace de la matrice A en utilisant votre fonction matrice_trace
print("\n")
A = np.array([[4,5,6],[2,1,4],[3,4,1]])
print("A =\n",A)
print("Trace de A =",matrice_trace(A))
print("A.T =\n",A.T)
print("A + A.T =\n",A + A.T)
print("(A + A.T)/2 =\n",(A + A.T)/2)
print("(A + A.T)/2 est symetrique :", est_symetrique((A + A.T)/2))

#Inversez la matrice A et multipliez-la par A. Vérifiez que vous obtenez une matrice proche de la matrice identité I
A_inv = np.linalg.inv(A)
print("A_inv =\n",A_inv)
print("A_inv * A =\n",A_inv * A)
print("A_inv * A est proche de I_3 :",np.allclose(A_inv * A, np.identity(3)))