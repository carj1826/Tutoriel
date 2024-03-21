#Création du tuple
Tuple = (1,2,3,4)

#Création de la liste
Liste = [5,6,7,8]

#Modification d'un élément de la liste
Liste[0]=10
#Afficher le résultat du changement
print(Liste)

#Tentative de modification d'un élément du tuple
#Tuple[0]=10 #Cela va créer une erreur; TypeError: 'tuple' object does not support item assignment

# Accéder aux éléments dans la liste et le tuple
print("Éléments de la liste :", Liste[0])    # Affichera :10
print("Éléments du tuple :", Tuple[0])      # Affichera : 1

#On peut aussi