import random

def gen_list_random_int(int_nbr=10, int_binf=0, int_bsup=10)->list:
    """Génère une liste de n entiers aléatoires compris entre int_binf et int_bsup

    Args:
        ch (str): _description_
        mot (str): _description_

    Returns:
        list: _description_
    """
    rand=[]
    for i in range(int_nbr):
        rand.append(random.randint(int_binf, int_bsup-1))
    return rand

print(gen_list_random_int(5,2,20))