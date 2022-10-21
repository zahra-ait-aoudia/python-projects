# Demander de choisir la difficulté
difficulte = input("Choisissez une difficulté: débutant, intermédiaire ou expert: ")

# Donner un nombre de vie en fonction de la difficulté choisie
Vies = 0
    
def niveau(param):

    nbVies = 0
    
    while nbVies == 0:
        
        if param == "débutant":
            nbVies = 10

        elif param == "intermédiaire":
            nbVies = 7

        elif param == "expert":
            nbVies = 4

        else:
            param = input("Choisissez une difficulté: débutant, intermédiaire ou expert: ")

    return(nbVies)

while Vies == 0:
    Vies = niveau(difficulte)

# Les fonctions utilisées
def underscore2(ranWord , L = []):
    r = ''
    for i in ranWord:
        if i in L:
            r += i + ' '
        else:
            r += '_ '
            
    return r[:-1]

def saisie():
    lettre = input("entrez une lettre: ")
    if len(lettre) > 1 or ord(lettre) < 65 or ord(lettre) > 122:
        print(" ")
        return saisie()
    else:
        print(" ")
        return lettre.upper()

# Choisir un mot dans le dictionnaire au hasard 
import random

with open("dico_france.txt", "r", encoding='ISO-8859-1') as file:
    allText = file.read()
    words = list(map(str, allText.split()))

    ranWorda = random.choice(words)
    ranWorda = ranWorda.upper()

    tablo = { 'éèêẽ' : 'e'
            , 'ç'    : 'c'
            , 'àâã'  : 'a'
            , 'ù'    : 'u'
            }

    ranWord_sans_accents = ''
    for i in ranWorda:
        for k in tablo:
            if i in k: i = tablo[k]; break
        ranWord_sans_accents += i

    ranWord = ranWord_sans_accents


# Tant qu'il reste des vies au joueur, le jeu continu
for Vies in range (Vies, 0, -1):  
    lettres_deja_proposees = []
    affichage = underscore2(ranWord)
    print(affichage)

    while '_' in affichage:
        
        if difficulte == "débutant" or difficulte == "intermédiaire":
            print("Lettres déjà proposées: " + str(lettres_deja_proposees))
        
        print("Nombre de vies restante: " + str(Vies))
        lettre = saisie()
        
        if lettre not in lettres_deja_proposees:
            lettres_deja_proposees += [ lettre ]

        elif lettre in lettres_deja_proposees:
            print("Lettre déjà proposée, veillez en choisir une autre.")
            Vies = Vies

        if lettre not in ranWord:
            Vies -= 1
            
        affichage = underscore2(ranWord , lettres_deja_proposees)
        print(affichage)

        if Vies == 0:
            print("Vous avez perdu")
            break

    if Vies>=1:       
        print("Vous avez gagné")
    
    break



