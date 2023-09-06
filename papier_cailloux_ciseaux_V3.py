import random
#creation de partie
ordinateur = input("Voulez-vous jouer contre l'ordinateur (Max 5 parties) O/N ? " )
if ordinateur != 'O' :
    if ordinateur != 'N' :
        print("Je n'ai pas compris votre réponse")
if ordinateur == 'O':
    nom1 = input("Quel est votre nom ? ")
    print("Bienvenue ",nom1, " nous allons jouer ensemble \n")
    nom2 = 'Machine'
joueur1 = 0
np = 0 #nombre de parties
if ordinateur == 'N':
    nom1 = input("Quel est votre nom ? ")
    print("Bienvenue ",nom1, " nous allons jouer ensemble")
    nom2 = input("Quel est le nom du deuxième joueur ?")
    print("Bienvenue ",nom2, " nous allons jouer ensemble \n")

partie = True
joueur2 = 0
while partie == True:
    np += 1 
    choix1 = input("{nom} faîtes votre choix parmi (pierre, papier, ciseaux ou puit): ".format(nom=nom1))
    if choix1 != 'pierre' and choix1 != 'papier' and choix1 != 'ciseaux' and choix1 != 'puit': #boucle qui détermine si la réponse est correcte
        choix1ok = False
        print("Je n'ai pas compris votre réponse")
        while choix1ok == False :
            print("Joueur ", nom1)
            choix1 = input(" faîtes votre choix parmi (pierre, papier, ou puit : ")
            choix1ok = True
            if choix1 != 'pierre' and choix1 != 'papier' and choix1 != 'ciseaux' and choix1 != 'puit':
                choix1ok = False
                print("Je n'ai pas compris votre réponse")

    if nom2 == 'Machine': 
        #Ici il faudrait plutôt vérifier que cpo == 'O' autrement
        #il y a un problème si le joueur 2 s'appelle Machine !
        choix2 = ['papier','pierre','ciseaux', 'puit'][random.randint(0, 3)]


    if nom2 != 'Machine':
        print("Joueur", nom2)
        choix2 = input("faîtes votre choix parmi (pierre, papier, ciseaux ou puit): ")
        if choix2 != 'pierre' and choix2 != 'papier' and choix2 != 'ciseaux' and choix1 != 'puit':
            choix2ok = False
            print("Je n'ai pas compris votre réponse")
            while not choix2ok :
                print("Joueur ", nom2)
                choix2 = input(" faîtes votre choix parmi (pierre, papier, ciseaux ou puit): ")
                choix2ok = True
                if choix2 != 'pierre' and choix2 != 'papier' and choix2 != 'ciseaux' and choix1 != 'puit':
                    choix2ok = False

    #On affiche les choix de chacun
    print("Si on récapitule :",nom1, choix1, "et", nom2, choix2,"\n")


    #On regarde qui a gagné cette manche on calcule les points et on affiche le résultat

    if choix1 == 'pierre' and choix2 == 'papier' :
        gagnant = nom2
        joueur1 = joueur1 + 0
        joueur2 = joueur2 + 1
        print("le gagnant est",gagnant)
        print("Les scores à l'issue de cette manche sont donc",nom1, joueur1, "et", nom2, joueur2, "\n")

    if choix1 == 'pierre' and choix2 == 'ciseaux' :
        gagnant = nom1
        joueur1 = joueur1 + 1
        joueur2 = joueur2 + 0
        print("le gagnant est",gagnant)
        print("Les scores à l'issue de cette manche sont donc",nom1, joueur1, "et", nom2, joueur2, "\n")

    if choix1 == 'papier' and choix2 == 'ciseaux' :
        gagnant = nom2
        joueur1 = joueur1 + 0
        joueur2 = joueur2 + 1
        print("le gagnant est",gagnant)
        print("Les scores à l'issue de cette manche sont donc",nom1, joueur1, "et", nom2, joueur2, "\n")

    if choix1 == 'papier' and choix2 == 'pierre' :
        gagnant = nom1
        joueur1 = joueur1 + 1
        joueur2 = joueur2 + 0
        print("le gagnant est",gagnant)
        print("Les scores à l'issue de cette manche sont donc",nom1, joueur1, "et", nom2, joueur2, "\n")

    if choix1 == 'ciseaux' and choix2 == 'pierre' :
        gagnant = nom2
        joueur1 = joueur1 + 0
        joueur2 = joueur2 + 1
        print("le gagnant est",gagnant)
        print("Les scores à l'issue de cette manche sont donc",nom1, joueur1, "et", nom2, joueur2, "\n")

    if choix1 == 'ciseaux' and choix2 == 'papier' :
        gagnant = nom1
        joueur1 = joueur1 + 1
        joueur2 = joueur2 + 0
        print("le gagnant est",gagnant)
        print("Les scores à l'issue de cette manche sont donc",nom1, joueur1, "et", nom2, joueur2, "\n")

    if choix1 == 'puit' and choix2 == 'pierre' :
        gagnant = nom1
        joueur1 = joueur1 + 1
        joueur2 = joueur2 + 0
        print("le gagnant est",gagnant)
        print("Les scores à l'issue de cette manche sont donc",nom1, joueur1, "et", nom2, joueur2, "\n")

    if choix1 == 'puit' and choix2 == 'papier' :
        gagnant = nom2
        joueur1 = joueur1 + 0
        joueur2 = joueur2 + 1
        print("le gagnant est",gagnant)
        print("Les scores à l'issue de cette manche sont donc",nom1, joueur1, "et", nom2, joueur2, "\n")
    
    if choix1 == 'puit' and choix2 == 'ciseaux' :
        gagnant = nom1
        joueur1 = joueur1 + 1
        joueur2 = joueur2 + 0
        print("le gagnant est",gagnant)
        print("Les scores à l'issue de cette manche sont donc",nom1, joueur1, "et", nom2, joueur2, "\n")

    if choix1 == 'pierre' and choix2 == 'puit' :
        gagnant = nom2
        joueur1 = joueur1 + 0
        joueur2 = joueur2 + 1
        print("le gagnant est",gagnant)
        print("Les scores à l'issue de cette manche sont donc",nom1, joueur1, "et", nom2, joueur2, "\n")

    if choix1 == 'papier' and choix2 == 'puit' :
        gagnant = nom1
        joueur1 = joueur1 + 1
        joueur2 = joueur2 + 0
        print("le gagnant est",gagnant)
        print("Les scores à l'issue de cette manche sont donc",nom1, joueur1, "et", nom2, joueur2, "\n")

    if choix1 == 'ciseaux' and choix2 == 'puit' :
        gagnant = nom2
        joueur1 = joueur1 + 0
        joueur2 = joueur2 + 1
        print("le gagnant est",gagnant)
        print("Les scores à l'issue de cette manche sont donc",nom1, joueur1, "et", nom2, joueur2, "\n")
    
    if choix1 == choix2 :
        gagnant = "aucun de vous, vous être ex æquo"
        joueur1 = joueur1 + 0
        joueur2 = joueur2 + 0
        print("le gagnant est",gagnant)
        print("Les scores à l'issue de cette manche sont donc",nom1, joueur1, "et", nom2, joueur2, "\n")

    if np ==1 or np ==2 or np==3 or np==4:
        partie = True
    if np ==5:
        partie = False
        
    if np ==1 or np ==2 or np==3 or np==4:
        #On propose de c ou de s'arrêter 
        go = input("Souhaitez vous refaire une partie {} contre {} ? (O/N) ".format(nom1,nom2))
        if go == 'O':
            partie = True
        if go == 'N':
            partie = False
        if go != 'O' and go != 'N':
            partie = True
            print("Vous ne répondez pas à la question, on continue ")
  
        
if partie == False :
    print("Merci d'avoir joué ! A bientôt")