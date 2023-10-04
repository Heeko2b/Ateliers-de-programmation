def date_est_valide(jour : int, mois : int, annee : int) -> bool :
    """Renvoie True si la date est valide, False sinon"""
    if jour < 1 or jour > 31 :
        return False
    elif mois < 1 or mois > 12 :
        return False
    elif annee < 1 :
        return False
    elif mois == 2 :
        if jour > 29 :
            return False
        elif jour == 29 :
            if annee % 4 != 0 :
                return False
            elif annee % 100 == 0 and annee % 400 != 0 :
                return False
            else :
                return True
        else :
            return True
    elif mois == 4 or mois == 6 or mois == 9 or mois == 11 :
        if jour > 30 :
            return False
        else :
            return True
    else :
        return True
    
def saisie_date_naissance() -> tuple :
    """Renvoie un tuple contenant la date de naissance"""
    jour = int(input("Entrez votre jour de naissance :"))
    mois = int(input("Entrez votre mois de naissance :"))
    annee = int(input("Entrez votre année de naissance :"))
    while date_est_valide(jour, mois, annee) == False :
        print("La date entrée n'est pas valide")
        jour = int(input("Entrez votre jour de naissance :"))
        mois = int(input("Entrez votre mois de naissance :"))
        annee = int(input("Entrez votre année de naissance :"))
    date = (jour, mois, annee)
    return date

def age(date_naissance) :
    """Renvoie l'age de la personne"""
    from datetime import date
    aujourdhui = date.today()
    jour = aujourdhui.day
    mois = aujourdhui.month
    annee = aujourdhui.year
    if date_naissance[1] > mois :
        return annee - date_naissance[2] - 1
    elif date_naissance[1] == mois :
        if date_naissance[0] > jour :
            return annee - date_naissance[2] - 1
        else :
            return annee - date_naissance[2]
    else :
        return annee - date_naissance[2]

def est_majeur(date_naissance) :
    """Renvoie True si la personne est majeure, False sinon"""
    if age(date_naissance) >= 18 :
        return True
    else :
        return False

def test_acces() :
    date_naissance = saisie_date_naissance()
    if est_majeur(date_naissance) == True :
        return True
    else :
        return False
    