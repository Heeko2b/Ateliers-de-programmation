def message_imc(x : float) -> str :
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
    else :
        message ="obésité morbide"
    return message


print("Vous êtes en situation de",message_imc(10))
print("Vous êtes en situation de",message_imc(20))
print("Vous êtes en situation de",message_imc(30))
print("Vous êtes en situation d'",message_imc(40))
print("Vous êtes en situation d'",message_imc(50))