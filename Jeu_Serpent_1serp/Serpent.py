

#Ce code est un jeu du serpent, dans lequel le joueur contrôle un serpent qui se déplace
# sur un écran en mangeant des pommes et en évitant de frapper les bords de l'écran ou de se
# mordre la queue.
# Le joueur utilise les touches fléchées pour déplacer le serpent dans la direction correspondante.
# La pomme est placée aléatoirement sur l'écran, et le serpent grandit chaque fois qu'il mange une pomme.
# Le score du joueur est affiché en haut à gauche de l'écran.
# La fonction principale du jeu est jeu(), qui initialise le score, la position du serpent et de la pomme,
# et contient la boucle principale du jeu. Dans cette boucle, les événements sont gérés,
# la position du serpent est mise à jour, les collisions sont détectées, et l'affichage est mis à jour.
# Il y a  plusieurs fonctions auxiliaires pour afficher le score, le serpent et les messages,
# ainsi que des variables pour définir la taille et la vitesse du serpent et les couleurs utilisées dans le jeu.


import pygame
import random


# Initialisation de Pygame
pygame.init()



# Dimensions de la fenêtre
largeur_fenetre = 600
hauteur_fenetre = 400

# Création de la fenêtre
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))

# Titre de la fenêtre
pygame.display.set_caption('Jeu du serpent')

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)
vert = (0, 255, 0)
rouge = (255, 0, 0)

# Charger l'image de fond d'écran
fond_ecran = pygame.image.load("snk.png")
# Redimensionner l'image de fond d'écran
fond_ecran = pygame.transform.scale(fond_ecran, (largeur_fenetre, hauteur_fenetre))



# Boucle principale du jeu
jeu_encours = True
while jeu_encours:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            jeu_encours = False

    # Affichage de l'arrière-plan
    fenetre.blit(fond_ecran, (0, 0))

    # Autres instructions du jeu
    pygame.display.update()



# Variables du serpent
taille_serpent = 10
vitesse_serpent = 12


# Création d'une police personnalisée
police = pygame.font.SysFont("Arial", 20)


# Fonction pour afficher le score
def afficher_score(score):
    font = pygame.font.SysFont(None, 25)
    message = font.render(" Score : " + str(score), True, rouge)
    #fenetre.blit(message, [0, 0])
    fenetre.blit(message, (10, 10))

# Fonction pour afficher le serpent
def afficher_serpent(taille_serpent, liste):
    for xy in liste:
        pygame.draw.rect(fenetre, vert, [xy[0], xy[1], taille_serpent, taille_serpent])

# Fonction pour afficher un message
def afficher_message(texte, couleur):
    font = pygame.font.SysFont(None, 25)
    message = font.render(texte, True, couleur)
    fenetre.blit(message, [largeur_fenetre / 6, hauteur_fenetre / 3])


# Fonction principale du jeu
def jeu():
    # Initialisation du score
    score = 0


    # Position de départ du serpent
    serpent_x = largeur_fenetre / 2
    serpent_y = hauteur_fenetre / 2

    # Liste pour stocker les segments du serpent
    serpent_liste = []
    serpent_longueur = 1

    # Position de départ de la pomme
    pomme_x = round(random.randrange(0, largeur_fenetre - taille_serpent) / 10.0) * 10.0
    pomme_y = round(random.randrange(0, hauteur_fenetre - taille_serpent) / 10.0) * 10.0

    # Variables de direction du serpent
    deplacement_x = 0
    deplacement_y = 0

    # Boucle principale du jeu
    jeu_encours = True
    while jeu_encours:
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                jeu_encours = False
            if evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_LEFT:
                    deplacement_x = -taille_serpent
                    deplacement_y = 0
                elif evenement.key == pygame.K_RIGHT:
                    deplacement_x = taille_serpent
                    deplacement_y = 0
                elif evenement.key == pygame.K_UP:
                    deplacement_y = -taille_serpent
                    deplacement_x = 0
                elif evenement.key == pygame.K_DOWN:
                    deplacement_y = taille_serpent
                    deplacement_x = 0

        # Déplacement du serpent
        serpent_x += deplacement_x
        serpent_y += deplacement_y

        # Bordures de l'écran
        if serpent_x >= largeur_fenetre or serpent_x < 0 or serpent_y >= hauteur_fenetre or serpent_y < 0:
            jeu_encours = False

        # Affichage de l'arrière-plan
        fenetre.fill(noir)

        # Affichage de la pomme
        pygame.draw.rect(fenetre, rouge, [pomme_x, pomme_y, taille_serpent, taille_serpent])


        # Ajout d'un segment au serpent
        tete_serpent = []
        tete_serpent.append(serpent_x)
        tete_serpent.append(serpent_y)
        serpent_liste.append(tete_serpent)
        if len(serpent_liste) > serpent_longueur:
            del serpent_liste[0]

        # Gestion des collisions
        for segment in serpent_liste[:-1]:
            if segment == tete_serpent:
                jeu_encours = False

        # Affichage du serpent
        afficher_serpent(taille_serpent, serpent_liste)

        # Mise à jour de l'affichage
        pygame.display.update()

        # Gestion de la collision avec la pomme
        if serpent_x == pomme_x and serpent_y == pomme_y:
            pomme_x = round(random.randrange(0, largeur_fenetre - taille_serpent) / 10.0) * 10.0
            pomme_y = round(random.randrange(0, hauteur_fenetre - taille_serpent) / 10.0) * 10.0
            serpent_longueur += 1
            score += 15
        # Affichage du score
        afficher_score(score)

        # Vitesse du serpent
        pygame.time.Clock().tick(vitesse_serpent)


    # Affichage du score final
    afficher_message("             Score final : " + str(score), rouge )
    pygame.display.update()
    pygame.time.wait(3000)

    # Fermeture de Pygame
    pygame.quit()

# Lancement du jeu
jeu()

