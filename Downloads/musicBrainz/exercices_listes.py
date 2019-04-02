couleurs = ['bleu', 'jaune', 'vert']

def affiche_couleurs(tableau):
    print('Les couleurs sont : ', end='')
    for couleur in tableau:
        # À faire : séparer les couleurs par des virgules.
        print(couleur, end='')
    print('.')

def construit_chaine_couleurs(tableau):
    resultat = 'Les couleurs sont : '
    return resultat

## Tests d'utilisation des fonctions

print("QUESTION 1 -- Affichage des couleurs :")
affiche_couleurs(couleurs)

print("QUESTION 2 -- Tentative d'affectation non pertinente:")
chaine = affiche_couleurs(couleurs)
print("L'affectation est faite, voici le résultat :")
print(chaine)

print("Une affectation qui devrait marcher :")
chaine = construit_chaine_couleurs(couleurs)
print("La chaine est construite, je vais l'afficher")
print(chaine)

print("SECTION 2.2 -- La même chose avec des tuples :")
couleurs_tuple = ('bleu', 'jaune', 'vert')
affiche_couleurs(couleurs_tuple)
print(construit_chaine_couleurs(couleurs_tuple))
