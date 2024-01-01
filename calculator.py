# THIS PROGRAM IS A MINI CALCULATOR
# IF YOU HAVE ANY QUESTION, YOU CAN CONTACT LEYNA BY MAIL : tarek.sassi@gmail.com
#

print("Salut !!!!! Bienvenue dans le programme de calcul de Leyna ;-)")
choixCalcul = input("Choisis ton calcul : Addition (A), Soustraction (S), Multiplication (M) ou Divison (D) : ")
nombreCalcul1 = int(input("Entre le premier nombre : "))
nombreCalcul2 = int(input("Entre le deuxième nombre : "))

if choixCalcul == "A":
    resultatAddition = nombreCalcul1 + nombreCalcul2
    print("Le résultat de ton addition est", resultatAddition)
elif choixCalcul == "S":
    resultatSoustraction = nombreCalcul1 - nombreCalcul2
    print("Le résultat de ta soustraction est", resultatSoustraction)
elif choixCalcul == "M":
    resultatMultiplication = nombreCalcul1 * nombreCalcul2
    print("Le résultat de ta multiplication est", resultatMultiplication)
elif choixCalcul == "D":
    resultatDivision = nombreCalcul1 / nombreCalcul2
    print("Le résultat de ta division est",resultatDivision)
else:
    print("Erreur de saisis, il faut choisir soit la lettre A,S,M ou D.")