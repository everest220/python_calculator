print("Bonjour, nous allons te demander de choisir 2 nombres que l'on va diviser")
dividende = int(input("Entre le dividende : "))
diviseur = int(input("Entre le diviseur : "))
resultatDivision = dividende // diviseur
resteDivision = dividende - (diviseur * resultatDivision)
print(F"Le resultat entier de la division est de {resultatDivision}")
print(F"Le reste de la division est de {resteDivision}")