import time, random 
import matplotlib.pyplot as plt
import numpy as np
from Ex2 import mix_list
#Pour mesurer le temps d'exécution nous avons à notre disposition
#la fonction perf_counter()
def perf_mix(mix_list, buildinfunction,lst:list, int:int):
    result=([],[])
    test=0 
    moyenne1 = []
    moyenne2 = []
#Récupération du temps système et démarrage du chronomètre
    while test < int:
        print("Test numéro ",test)
        start_pc = time.perf_counter()
        for i in lst:

            #Test de mix_list
            start_pc = time.perf_counter()
            mix_list(list(range(i)))
            end_pc = time.perf_counter()
            result[0].append(end_pc-start_pc)
            print("Fonction 1 ", result[0][test])

            #Test de la fonction shuffle
            start_pc = time.perf_counter()
            buildinfunction(list(range(i)))
            end_pc = time.perf_counter()
            result[1].append(end_pc-start_pc)
            print("Fonction 2 :",result[1][test],"\n")
        moyenne1.append(sum(result[0])/len(lst))
        moyenne2.append(sum(result[1])/len(lst))
        test+=1
    while len(moyenne1) < len(lst):
        moyenne1.append(0)
        moyenne2.append(0)
    #On additionne tous les résultats de result[0] pour calculer la moyenne
    plt.plot(lst, moyenne1, label="mix_list")
    plt.plot(lst, moyenne2, label="shuffle")
    plt.show()
    return result

lst= [10, 500, 5000, 50000, 100000]
print("Temps écoulé entre les deux mesures : ",perf_mix(mix_list, random.shuffle, lst, 2))
# Exécutez ce code et vérifiez par vous-même la variabilité des mesures.

"""#Ici on décrit les abscisses
#Entre 0 et 5 en 10 points
x_axis_list = np.arange(0,5.5,0.5)
fig, ax = plt.subplots()
#Dessin des courbes, le premier paramètre
#correspond aux point d'abscisse le
#deuxième correspond aux points d'ordonnées
#le troisième paramètre, optionnel permet de
#choisir éventuellement la couleur et le marqueur
ax.plot(x_axis_list,x_axis_list,'bo-',label='Identité')
ax.plot(x_axis_list,x_axis_list**2, 'r*-', label='Carré')
ax.plot(x_axis_list,x_axis_list**3,'g*-', label='Cube')
ax.set(xlabel='Abscisse x', ylabel='Ordonnée y',
 title='Fonctions identité, cube et carré')
ax.legend(loc='upper center', shadow=True, fontsize='x-large')
#fig.savefig("test.png")
plt.show()"""