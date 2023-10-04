import random
def extract_elements_list(list_in_which_to_choose:list, int_nbr_of_element_to_extract:int)->list:
    """Retourne une liste d'éléments venant de list_in_which_to_choose choisis aléatoirement

    Args:
        list_in_which_to_choose (list): _description_
        int_nbr_of_element_to_extract (int): _description_

    Returns:
        list: _description_
    """
    sbeul=list_in_which_to_choose.copy()
    nbr=0
    while nbr <= int_nbr_of_element_to_extract:
       for i in range(len(sbeul)):
            j=random.randint(0, len(sbeul)-1) #Génère un chiffre compris entre la valeur de l'indice 0 et celle de l'indice max de la liste
            sbeul[i], sbeul[j]= sbeul[j], sbeul[i]
       nbr+=1
    return sbeul

liste=[129,41,490,239,23,92,56]
liste2=[[1],[2,3],[5],[6,5]]
print("Liste originelle:",liste)
print("Tirage au sort:",extract_elements_list(liste,5))
print("Tirage au sort 2:",extract_elements_list(liste2,5))