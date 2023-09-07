def message_imc(x : int) -> str :
    if x < 16.5 :
        message = "dénutrition ou famine"
    elif x <= 18.5 :
        message ="maigreur"
    elif x <= 25 :
        message ="corpulence normale"
    elif x <= 30 :
        message ="surpoids"
    elif x <= 35 :
        message ="obésité modérée"
    elif x <= 40 :
        message ="obésité sévère"
    elif x > 40 :
        message ="obésité morbide"
    return message
boucle = 0
while boucle < 6 :
    poids =int(input ("Indiquez votre IMC :"))
    msg=message_imc(poids)
    print("Vous êtes en situation de ",msg,)
    boucle += 1