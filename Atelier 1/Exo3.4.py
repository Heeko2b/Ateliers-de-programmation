from math import sqrt
def discriminant(a : int, b : int, c : int) -> int :
    return b*b - 4*a*c

def racine_double(a : int,b : int,delta : int,num : int) -> float :
    if delta < 0 :
        result = 0
    elif num == 1 :
        result = (-b + sqrt(delta))/(2*a)
    elif num == 2 :
        result = (-b - sqrt(delta))/(2*a)
    else :
        result = 0
    return result

un =int(input ("Entrez un premier chiffre :"))
deux =int(input ("Entrez un deuxième chiffre :"))
trois =int(input ("Entrez un troisième chiffre :"))
numéro =int(input ("Entrez un numéro de racine :"))
resultat=discriminant(un, deux, trois)
r2 = racine_double(un, deux, resultat, numéro)
print("La racine double est ",r2,)