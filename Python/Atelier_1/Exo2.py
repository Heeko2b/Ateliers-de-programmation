def est_bissextile(x : int) -> bool :
    return (x%4==0 and not x%100==0) or x%400==0

boucle = 0
while boucle < 6 :
    année =int(input ("Entrez une année :"))
    bis=est_bissextile(année)
    if bis :
        print("C'est une année bissextile")
    else :
        print("Ce n'est pas une année bissextile")
    boucle += 1