# Tutoriel: Quelles sont les différences entre une liste et un tuple : pourquoi et comment les utiliser ?

## Établir le contexte de la problématique d'affaires ou technique menant au tutoriel
Au 21e siècle, bien savoir utiliser la technologie dans le monde des affaires peux être un avantage considérable par rapport à la compétition, mais peux aussi amener plusieurs enjeux. Par exemple, choisir la structure de données approprié pour stocker et manipuler les données d'affaires est très important pour le bon focntionnement de n'importe quel entreprise. Deux de ces structures en Python sont les listes et le tulpes et savoir les différencier permet de choisir la structure la plus approprié et rendre l'accès et la manipulation aux données d'affaires beaucoup plus simple pour le future.

Pour ce tutoriel, les conaissances préalables nécessaires sont:
- Une connaissance de base en Pyhton.
- Une compréhension des concepts de variables, de types de données et de structures de contrôle serait également bénéfique.
  
## Bâtir un exemple pour introduire le contenu du tutoriel en contexte de manipulation des données
Si nous prenons comme exemple une compagnie d'investissement. Cette compagnie doit stocker différentes infromations comme leur liste de clients, leur lise d'employés et les différents titres et produits que la compagnie gère. Pour stocker ces informations, la compagnie peut utiliser des listes et des tuples pour ensuite facilement y avoir accès. Par exemple, la compagnie peut elle même créer une liste ou un tuple pour stocker sa liste de client:

``` Python 
#Création du tuple
Tuple = ("Client1","Client2","Client3","Client4")

#Création de la liste
Liste = ["Client1","Client2","Client3","Client4"]
```
Les données sont maintenant stocké en liste et en tuple ce qui permet à la compagnie de manipuler ses données quand elle en a besoin. 

## Présenter de façon structurée et illustrer le contenu du tutoriel
Il y a plusieurs différences entre une liste et un tuple et plusieurs façon pour les utiliser. Premièrement, en regardant l'exemple plus haut de création d'une liste et d'un tuple, la première différence est la syntaxe. Les listes sont définies avec des crochets [] alors que les tuples sont défini avec des parenthèse (). 
Deuxièmement, la différence qui vient déterminer quel structure est la plus approprié est leur mutabilité. Les listes peuvent être modifiés, ce qui veut dire qu'on peut supprimer, ajouter et modifier les éléments dans des listes après leurs création. Au contraire, les tuples sont immuables, ce qui veut dire qu'on ne peut pas les modifiés après leurs création (Source). Voici un exemple pour représenter cette deuxième différence:

``` Python
#Modification d'un élément de la liste
Liste[0]="Client5"
#Afficher le résultat du changement
print(Liste)

#Tentative de modification d'un élément du tuple
#Tuple[0]="Client5" #Cela va créer une erreur; TypeError: 'tuple' object
#does not support item assignment
``` 
Comme on peut voir dans cet exemple, on peut facilement modifier un élément de la liste (Client1) par un nouveau (Client5). Cependant, on ne peut pas dire la même chose pour le tuple, car lorsqu'on essaye de modifier un élément dans le tuple, cela crée une erreur dans le code.
La troisième différence, qui découle de la deuxième, est l'utilisation des listes et des tuples. Il est mieux d'utiliser une liste lorsque ce sont des données que nous allons vouloir modifier dans le futur et utiliser un tuple quand ce sont des données qui ne doivent pas être modifiées. Pour notre exemple de compagnie d'investissement, si la liste de client doit être modifier fréquemment pour ajouter et retirer des clients, alors il est mieux de la stocker dans une liste. Si c'est une liste très importantes qui ne doit pas être modifié, alors on utilise un tuple.
La dernière différence est la performance d'un tuple comparé à une liste. En général, les tuples sont plus rapides que les listes à cause de leur immuabilité. (Source)
Une fois la liste et le tuple créer, la compagnie peut accéder à ses données de la même façon avec la fonction print:

``` Python
# Accéder aux éléments dans la liste et le tuple
print("Éléments de la liste :", Liste[0])    # Affichera :Client5
print("Éléments du tuple :", Tuple[1])      # Affichera : Client2
```

Maintenant que la différence entre les listes et les tuples et leurs utilisation est expliqué voici des bonnes pratiques et astuces pour la manipulation efficace des données:
1. 


- Assurer la répétabilité du contenu : une personne ayant suivi le tutoriel devrait reconnaître le contexte, savoir appliquer le contenu, pouvoir déterminer si c'est un succès
  
## Transférer les connaissances à d'autres contextes pouvant bénéficier du contenu du tutoriel par des cas d'utilisation ou des illustrations

## Énoncer les limites du tutoriel et les prochaines étapes d'apprentissage

## Synthétiser le contenu du tutoriel
- Revenir brièvement sur la problématique d'origine
- Revenir brièvement sur les concepts clés et leur utilisation
- Souligner la valeur personnelle au lecteur du tutoriel
- Indiquer les prochaines notions ou étapes d'apprentissage dans la perspective de parcours


Sources:
https://www.docstring.fr/glossaire/tuple/#:~:text=La%20diff%C3%A9rence%20fondamentale%20entre%20les,pouvez%20pas%20modifier%20leurs%20%C3%A9l%C3%A9ments.
