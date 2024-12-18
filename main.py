import numpy as np

# Taille de la grille
N = 7

# Initialisation de la grille aléatoire (0 ou 1)
frame = np.random.randint(0, 2, size=(N, N))  # Génère une grille 7x7 aléatoire avec des 0 et des 1

def afficher_grille(grille):
    """ Affiche la grille """
    for ligne in grille:
        print("   ".join(str(cellule) for cellule in ligne))
    print()

def voisins_vivants(i, j, grille):
    """ Calcule le nombre de voisins vivants d'une cellule en prenant en compte le padding """
    # Ajouter un padding de 0 autour de la grille
    grille_padding = np.pad(grille, pad_width=1, mode='constant', constant_values=0)
    
    # Décaler i et j pour tenir compte du padding
    i += 1
    j += 1
    
    # Somme des 8 voisins (en excluant la cellule elle-même)
    return np.sum(grille_padding[i-1:i+2, j-1:j+2]) - grille_padding[i, j]

def jeu_de_la_vie(grille):
    """ Applique les règles du jeu de la vie pour une génération """
    # Crée une nouvelle grille pour la génération suivante
    nouvelle_grille = np.zeros_like(grille)
    
    for i in range(N):  # Boucle sur toutes les lignes
        for j in range(N):  # Boucle sur toutes les colonnes
            # Nombre de voisins vivants
            voisins = voisins_vivants(i, j, grille)
            
            if grille[i][j] == 1:
                if voisins < 2 or voisins > 3:
                    nouvelle_grille[i][j] = 0  # Meurt par sous-population ou surpopulation
                else:
                    nouvelle_grille[i][j] = 1  # Reste en vie
            elif grille[i][j] == 0 and voisins == 3:
                nouvelle_grille[i][j] = 1  # Naît par reproduction
    
    return nouvelle_grille

# Afficher l'état initial
print("État initial (aléatoire) :")
afficher_grille(frame)

# Appliquer les règles et afficher les générations suivantes
for t in range(5):  # Afficher 5 générations
    frame = jeu_de_la_vie(frame)
    print(f"Génération {t+1}:")
    afficher_grille(frame)
