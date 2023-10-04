import numpy as np

#Définissez une procédure matriceAdjacence(S,A) qui admet en paramètres une liste S de sommets et une liste A d’arcs (liste de tuples (i,j) avec i,jS ) et retourne la matrice d’adjacence associée (type array à 2 dimensions de numpy)

def matriceAdjacence(S, A):
    # Créer une matrice carrée remplie de zéros avec une taille égale au nombre de sommets
    n = len(S)
    matrice = np.zeros((n, n), dtype=int)

    # Remplir la matrice d'adjacence en parcourant la liste d'arcs
    for arc in A:
        #arc contient les tuples qui doivent afficher 1 sur la matrice d'adjacence, donc on attribue le tuple a i et j
        i, j = arc
        # Marquer la connexion entre les sommets i et j en mettant la valeur 1 dans la matrice
        matrice[i, j] = 1

    return matrice

# Exemple d'utilisation
sommets = np.array([0, 1, 2, 3])
arcs = np.array([(0, 1), (0, 2), (1, 2), (2, 3)])

matrice_adjacence = matriceAdjacence(sommets, arcs)
print(matrice_adjacence)

def matriceAdjacencePond(S, A):
    # Créez une matrice carrée remplie de zéros avec une taille égale au nombre de sommets
    n = len(S)
    matrice = np.zeros((n, n))  # Utilisation de dtype=float pour les poids

    # Remplissez la matrice d'adjacence en parcourant la liste d'arcs pondérés
    for arc in A:
        i, j, poids = arc
        # Utilisez le poids pour indiquer la connexion entre les sommets i et j
        matrice[i, j] = poids

    return matrice

# Exemple d'utilisation
sommets = [0, 1, 2, 3]
arcs_pondérés = [(0, 1, 2.5), (0, 2, 1.0), (1, 2, 3.0), (2, 3, 4.2)]
matrice_adjacence_pondérée = matriceAdjacencePond(sommets, arcs_pondérés)
print(matrice_adjacence_pondérée)

def lireMatriceFichier(nomfichier):
    """fonction qui renvoie une matrice carrée(typearray de numpy) contenue dans le fichier dont le nom est passé en paramètre.

    Args:
        nomfichier (_type_): _description_

    Returns:
        _type_: _description_
    """
    # Ouvrir le fichier en mode lecture
    fichier = open(nomfichier, "r")

    # Lire la première ligne du fichier
    ligne = fichier.readline()

    # Créer une liste vide pour stocker les lignes du fichier
    lignes = []

    # Parcourir le fichier ligne par ligne
    while ligne != "":
        # Ajouter la ligne à la liste des lignes
        lignes.append(ligne)
        # Lire la ligne suivante
        ligne = fichier.readline()

    # Fermer le fichier
    fichier.close()

    # Créer une matrice carrée remplie de zéros avec une taille égale au nombre de lignes
    n = len(lignes)
    matrice = np.zeros((n, n), dtype=int)

    # Remplir la matrice en parcourant la liste des lignes
    for i in range(n):
        # Séparer les valeurs de la ligne en utilisant l'espace comme séparateur
        valeurs = lignes[i].split(" ")
        # Parcourir les valeurs de la ligne
        for j in range(n):
            # Convertir la valeur en entier et l'ajouter à la matrice
            matrice[i, j] = int(valeurs[j])

    return matrice

#test de lireMatriceFichier
"""matrice = lireMatriceFichier("C:/Users/jacqu/Documents/L3/Ateliers_de_programmation/Atelier_5/graph0.txt")
print(matrice,"\n")
matrice = lireMatriceFichier("C:/Users/jacqu/Documents/L3/Ateliers_de_programmation/Atelier_5/graph1.txt")
print(matrice,"\n")
matrice = lireMatriceFichier("C:/Users/jacqu/Documents/L3/Ateliers_de_programmation/Atelier_5/graph2.txt")
print(matrice,"\n")
matrice = lireMatriceFichier("C:/Users/jacqu/Documents/L3/Ateliers_de_programmation/Atelier_5/graph3.txt")
print(matrice,"\n")
matrice = lireMatriceFichier("C:/Users/jacqu/Documents/L3/Ateliers_de_programmation/Atelier_5/graph4.txt")
print(matrice)"""