import json


def lec():
    with open("parking.json", "r") as f:
        x = json.load(f)
        return x
    
def ecriture():
    with open("parking.json", "w") as f:
        json.dump(dico_parking,f)


def init_parking():
    c=26
    for i in range(0,c):
        dico_parking[f'emplacement{i+1}']= False
    for ivaleur in dico_parking.values():
        ivaleur=False
    ecriture()
    
dico_parking = lec()


def garer(indice):
    
    dico_parking[f'emplacement{indice}']=True

def liberer(indice):

    dico_parking[f'emplacement{indice}']=False

def afficher_parking():
    for cle,valeur in dico_parking.items():
        if valeur ==True:
            valeur = "indisponnible"
        else:
            valeur = "disponible"
        print(f"l'{cle} est {valeur}")


def prop_garer():
    
    print("LES EMPLACEMENT DISPONNIBLE SONT :")
    for cle,valeur in dico_parking.items():
        if valeur == False:
            print(f"l'{cle}")

    nb = input("entre le numero de l'emplacement que tu souhaite attribuer\n==>")
    verif = nb.isdigit()
    while verif is not True:
        nb = input("entre le numero de l'emplacement que tu souhaite attribuer\n==>")
        verif = nb.isdigit()
    nb= int(nb)
    garer(nb)
    ecriture()


def prop_liberer():
    
    print("LES EMPLACEMENT INDISPONNIBLE SONT :")
    for cle,valeur in dico_parking.items():
        if valeur == True:
            print(f"l'{cle}")

    nb = input("entre le numero de l'emplacement que tu souhaite libérer\n==>")
    verif = nb.isdigit()
    while verif is not True:
        nb = input("entre le numero de l'emplacement que tu souhaite libérer\n==>")
        verif = nb.isdigit()
    nb= int(nb)
    liberer(nb)
    ecriture()


menu = {
    '1': afficher_parking,
    '2': prop_garer,
    '3': prop_liberer,
    '4' : init_parking
}

def menu_principal():
    print("***************")
    print("*             *")
    print("*    MENU     *")
    print("*  PRINCIPAL  *")
    print("*             *")
    print("***************")
    g = True
    prop=["1","2","3","4","quit","QUIT"]
    while g:
        choix = input(f"\n[1] Afficher l'état du parking\n[2] Garer une voiture\n[3] Sortir une voiture\n[4] Vider le parking\n\n[quit] Quittez\nQUE VEUT TU FAIRE ?\n==>")
        while choix not in prop:
            choix = input(f"\nQUE VEUT TU FAIRE ?\n\n[1] Afficher l'état du parking\n[2] Garer une voiture\n[3] Sortir une voiture\n[4] Vider le parking\n\n[quit] Quittez\n")
        if choix == "quit" or choix == "QUIT":
            ecriture()
            g=False
        for cle, valeur in menu.items():
            if choix == cle:
                valeur()
    ecriture()



menu_principal()
        
