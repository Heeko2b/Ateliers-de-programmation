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
    c1 = input("{nom} faîtes votre choix parmi (pierre, papier, ciseaux): ".format(nom=nom1))
    if c1 != 'pierre' and c1 != 'papier' and c1 != 'ciseaux': #boucle qui détermine si la réponse est correcte
        c1ok = False
        print("Je n'ai pas compris votre réponse")
        while c1ok == False :
            print("Joueur ", nom1)
            c1 = input(" faîtes votre choix parmi (pierre, papier, ciseaux): ")
            c1ok = True
            if c1 != 'pierre' and c1 != 'papier' and c1 != 'ciseaux':
                c1ok = False
                print("Je n'ai pas compris votre réponse")

    if nom2 == 'Machine': 
        #Ici il faudrait plutôt vérifier que cpo == 'O' autrement
        #il y a un problème si le joueur 2 s'appelle Machine !
        e2 = ['papier','pierre','ciseaux'][random.randint(0, 2)]


    if nom2 != 'Machine':
        print("Joueur", nom2)
        e2 = input("faîtes votre choix parmi (pierre, papier, ciseaux): ")
        if e2 != 'pierre' and e2 != 'papier' and e2 != 'ciseaux':
            j2bon = False
            print("Je n'ai pas compris votre réponse")
            while not j2bon :
                print("Joueur ", nom2)
                e2 = input(" faîtes votre choix parmi (pierre, papier, ciseaux): ")
                j2bon = True
                if e2 != 'pierre' and e2 != 'papier' and e2 != 'ciseaux':
                    j2bon = False

    #On affiche les choix de chacun
    print("Si on récapitule :",nom1, c1, "et", nom2, e2,"\n")


    #On regarde qui a gagné cette manche on calcule les points et on affiche le résultat
    if c1 == 'papier' and e2 == 'papier' :
        w12 = "aucun de vous, vous être ex æquo"
        joueur1 = joueur1 + 0
        joueur2 = joueur2 + 0
        print("le gagnant est",w12)
        print("Les scores à l'issue de cette manche sont donc",nom1, joueur1, "et", nom2, joueur2, "\n")

    if c1 == 'pierre' and e2 == 'papier' :
        w12 = nom2
        joueur1 = joueur1 + 0
        joueur2 = joueur2 + 1
        print("le gagnant est",w12)
        print("Les scores à l'issue de cette manche sont donc",nom1, joueur1, "et", nom2, joueur2, "\n")

    if c1 == 'pierre' and e2 == 'pierre' :
        w12 = "aucun de vous, vous être ex æquo"
        joueur1 = joueur1 + 0
        joueur2 = joueur2 + 0
        print("le gagnant est",w12)
        print("Les scores à l'issue de cette manche sont donc",nom1, joueur1, "et", nom2, joueur2, "\n")

    if c1 == 'pierre' and e2 == 'ciseaux' :
        w12 = nom1
        joueur1 = joueur1 + 1
        joueur2 = joueur2 + 0
        print("le gagnant est",w12)
        print("Les scores à l'issue de cette manche sont donc",nom1, joueur1, "et", nom2, joueur2, "\n")

    if c1 == 'papier' and e2 == 'ciseaux' :
        w12 = nom2
        joueur1 = joueur1 + 0
        joueur2 = joueur2 + 1
        print("le gagnant est",w12)
        print("Les scores à l'issue de cette manche sont donc",nom1, joueur1, "et", nom2, joueur2, "\n")

    if c1 == 'papier' and e2 == 'pierre' :
        w12 = nom1
        joueur1 = joueur1 + 1
        joueur2 = joueur2 + 0
        print("le gagnant est",w12)
        print("Les scores à l'issue de cette manche sont donc",nom1, joueur1, "et", nom2, joueur2, "\n")

    if c1 == 'ciseaux' and e2 == 'pierre' :
        w12 = nom2
        joueur1 = joueur1 + 0
        joueur2 = joueur2 + 1
        print("le gagnant est",w12)
        print("Les scores à l'issue de cette manche sont donc",nom1, joueur1, "et", nom2, joueur2, "\n")

    if c1 == 'ciseaux' and e2 == 'ciseaux' :
        w12 = "aucun de vous, vous être ex æquo"
        joueur1 = joueur1 + 0
        joueur2 = joueur2 + 0
        print("le gagnant est",w12)
        print("Les scores à l'issue de cette manche sont donc",nom1, joueur1, "et", nom2, joueur2, "\n")

    if c1 == 'ciseaux' and e2 == 'papier' :
        w12 = nom1
        joueur1 = joueur1 + 1
        joueur2 = joueur2 + 0
        print("le gagnant est",w12)
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