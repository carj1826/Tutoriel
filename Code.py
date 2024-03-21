#Création du tuple
Tuple = ("Client1","Client2","Client3","Client4")

#Création de la liste
Liste = ["Client1","Client2","Client3","Client4"]

#Modification d'un élément de la liste
Liste[0]="Client5"
#Afficher le résultat du changement
print(Liste)

#Tentative de modification d'un élément du tuple
#Tuple[0]="Client5" #Cela va créer une erreur; TypeError: 'tuple' object does not support item assignment

# Accéder aux éléments dans la liste et le tuple
print("Éléments de la liste :", Liste[0])    # Affichera :Client5
print("Éléments du tuple :", Tuple[1])      # Affichera : Client2

#On peut aussi