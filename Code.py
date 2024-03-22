#Création du tuple
Tuple = ("Client1","Client2","Client3","Client4")

#Création de la liste
Liste = ["Client1","Client2","Client3","Client4"]

#Modification d'un élément de la liste
Liste[0]="Client5"
#Afficher le résultat du changement
print(Liste)    #Affichera: ['Client5', 'Client2', 'Client3', 'Client4']

#Tentative de modification d'un élément du tuple
#Tuple[0]="Client5" #Cela va créer une erreur; TypeError: 'tuple' object
                        # does not support item assignment

#Ajout d'un élément dans la liste
Liste.append("Client6")
#Afficher le résultat de l'ajout
print(Liste)    #Affichera: ['Client5', 'Client2', 'Client3', 'Client4', 'Client6']

#Tentative d'ajout d'un élément dans le tuple
#Tuple.append("Client6") #Cela va encore créer une erreur; AttributeError: 'tuple' object
                            # has no attribute 'append'

# Accéder aux éléments dans la liste et le tuple
print("Éléments de la liste :", Liste[0])    # Affichera :Client5
print("Éléments du tuple :", Tuple[1])      # Affichera : Client2

#On peut aussi