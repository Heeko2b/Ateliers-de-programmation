import re

def variable2test(str:str) -> str:
    if str.strip() !="":
        split=str.split()
        split[0]=split[0].upper()
        for i in range(1, len(split)):
            split[i]=split[i].capitalize()

        return " ".join(split)
    else:
        return " "

def is_mail(str:str) -> (int, int):
    #On test si il y a un arobase dans le mail
    arobase=str.count("@")
    if arobase != 1:
        return (0, 2)
    splited=str.split("@")
    #On cherche si le corp du mail commence ou termine par un point, si oui on renvoie (0, 1)
    result= re.search("^(?!.*\.$)(?!.*\.\.)([\w^\.]*)$", splited[0])
    if not result:
        return (0, 1)
    domaine= re.search("^(?!.*\.\.)(?!^\.)[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*$", splited[1])
    if not domaine:
        return (0, 3)
    #On cherche si il y a un point avant le suffixe du mail, si oui on renvoie (0, 4)
    point= re.search("\.[a-zA-Z]{0,3}$", splited[1])
    print("point =",point)
    if not point:
        return (0, 4)
    else:
        return (1, 0)
    

    """valide=str.split("@")
    if len(valide) == 2:
        print(valide)
        for i in range(valide[0]):
            if (i==0 or i==(len(valide[0]))) and valide[i]=="." :
                return (0, 1)
    else:
        return (0, 2)"""
    
    
print(variable2test("battaglini jacques"))
print(is_mail("bisgambiglia@univ-corse.fr"))