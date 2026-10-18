def lireProp(what: str) -> str:
    but = input("les " +f"{what}  sont: " ).upper()
    print(but)
    return(but)





def lireFait(what: str) -> set[str]:
    but = input("les  " +f"{what}  "  ).upper()
    liste = but.split(",")
    ensemble =set()
    for i in liste:
        ensemble.add(i.strip().upper())

    print(ensemble)
    return ensemble

def lireRegles()-> list[list]:
    stop = 0
    regles = []
    
    while(stop ==0): 
        a = lireFait("premisses") #une liste de premisses
        b =lireProp("conclusions") #une chaine qui contient les conc
        l= [a,b]
        regles.append(l)
        
        stop = int(input("0 pour continuer et 1 pour s'arreter "))
    print(regles)
    return regles

lireProp("conclusion")

def chainageAvant(buts,faits,regles):
    for but in buts:
        if(but in faits):
            return True

    modifié = True
    while(modifié):
        modifié = False
        for regle in regles:
            if((regle[0] in faits) and (regle[1] not in faits)):
                faits.append(regle[1])
                modifié = True
                if(buts in faits):
                    ("true")
                    return True
    return False


          
    


#r = lireRegles()
b =['S']
f = ['V','L']
print(chainageAvant(b,f,[[['H'], 'M'], [['L'], 'M'], [['V', 'M'], 'S']]))

    

        




