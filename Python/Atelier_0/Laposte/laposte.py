montant = 0
#dictionnaires des tarifs
VERTE = {20: 1.16, 100: 2.32, 250: 4, 500: 6, 1000: 7.50, 3000: 10.50}
PRIO = {20: 1.43, 100: 2.86, 250: 5.26, 500: 7.89, 3000: 11.44}
ECO = {20: 1.14, 100: 2.28, 250: 3.92}

#demande des informations
type = input("Quel type de lettre voulez vous envoyer? (verte, prioritaire ou ecopli)")

if type != 'verte' and type != 'prioritaire' and type != 'ecopli':
    print("Je n'ai pas compris votre réponse")
    pasbon = True
    while pasbon == True :
        type = input("Quel type de lettre voulez vous envoyer? (verte, prioritaire ou ecopli)")
        if type == 'verte' or type == 'prioritaire' or type == 'ecopli':
            pasbon = False
    
poids = input("Quel est le poids de votre courrier (en grammes)?")
poids = int(poids)

#calcul du montant
if type == 'verte' :
    while poids >= 3000 :
        poids = input("Votre courrier est trop lourd, veuillez entrer un autre poids :")
        poids = int(poids)
    for cle in VERTE :
        if poids < cle :
            montant = VERTE[cle]
            break
        else :
            montant = VERTE[cle]

elif type == 'prioritaire' :
    while poids >= 3000 :
        poids = input("Votre courrier est trop lourd, veuillez entrer un autre poids :")
        poids = int(poids)
    for cle in PRIO :
        if poids < cle :
            montant = PRIO[cle]
            break
        else :
            montant = PRIO[cle]

elif type == 'ecopli' :
    while poids >= 250 :
        poids = input("Votre courrier est trop lourd, veuillez entrer un autre poids :")
        poids = int(poids)
    for cle in ECO :
        if poids < cle :
            montant = ECO[cle]
            break
        else :
            montant = ECO[cle]

#affichage du montant
print ("Le montant de votre envoi est de ",montant," euros \n")