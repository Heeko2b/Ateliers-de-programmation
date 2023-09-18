def discriminant(a : int, b : int, c : int) -> int :
    return b*b - 4*a*c

un =int(input ("Entrez un premier chiffre :"))
deux =int(input ("Entrez un deuxième chiffre :"))
trois =int(input ("Entrez un troisième chiffre :"))
resultat=discriminant(un, deux, trois)
print("Le delta de",un,"carré - 4(",deux,")(",trois,") est ",resultat,)