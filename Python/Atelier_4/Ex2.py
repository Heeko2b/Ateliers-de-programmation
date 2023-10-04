import random
def mix_list(list_to_mix:list)->list:
    """Mélange une liste (sans l'altérer)

    Args:
        list_to_mix (list): liste d'origine

    Returns:
        list: liste mélangée
    """
    melange=list_to_mix.copy() #Crée melange qui est une copie de la liste d'entrée
    for i in range(len(melange)):
        j=random.randint(0, len(melange)-1) #Génère un chiffre compris entre la valeur de l'indice 0 et celle de l'indice max de la liste
        melange[i], melange[j]= melange[j], melange[i] #Echange les valeurs aux indices i et j
    return melange

liste=[15,40,132,56,49,20,46,12,9]
print("Liste originelle:",liste)
print("Liste mélangée:",mix_list(liste))