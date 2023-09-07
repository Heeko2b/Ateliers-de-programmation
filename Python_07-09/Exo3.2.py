def racine_unique(a : int, b : int) -> int :
    x = -b/(2*a)
    return x

un =int(input ("Entrez un premier nombre :"))
deux =int(input ("Entrez un deuxième nombre :"))
resultat=racine_unique(un, deux)
print("x =",resultat,)