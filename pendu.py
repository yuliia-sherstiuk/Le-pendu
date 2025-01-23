import pygame
import random
import os

pygame.init()

# Configuration de la fenêtre
LARGEUR, HAUTEUR = 700, 600
screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("  PENDU.   Devinez le mot. ")

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
OLIVE = (128, 128, 0)
VERT = (0,128, 0)
BLEU = (0,0,255)
JAUNE = (255,255,0)
MAROON = (128,0,0)
# Police
POLICE = pygame.font.SysFont("chalkduster.ttf", 50)

# Initialisation des variables
erreurs = 0
erreurs_max = 10
horloge = pygame.time.Clock()
en_cours = True

# Chemin vers le fichier de mots
chemin_dossier = r"C:\Users\djana\Documents\pendu"
chemin_fichier = os.path.join(chemin_dossier, "mots.txt")

# Lecture ou création du fichier mots.txt
if not os.path.exists(chemin_fichier):
    print(f"Le fichier '{chemin_fichier}' est introuvable.")
    with open(chemin_fichier, "w") as f:
        f.write("PENDU\nPYTHON\nPROGRAMMATION\n")
    print(f"Un fichier 'mots.txt' a été créé à l'emplacement : {chemin_fichier}")

with open(chemin_fichier, "r") as f:
    mots = f.read().splitlines()

# Choix d'un mot aléatoire
mot_choisi = random.choice(mots).upper()
devine = ["_"] * len(mot_choisi)
lettres_devinees = set()

def dessiner_pendu(erreurs):
    # Dessin du pendu
    if erreurs > 0:
        pygame.draw.line(screen,NOIR , (150, 500), (550, 500), 7)
    if erreurs > 1:
        pygame.draw.line(screen, MAROON, (300, 500), (300, 200), 15)
    if erreurs > 2:
        pygame.draw.line(screen, MAROON, (295, 200), (400, 200), 7)
    if erreurs > 3:
        pygame.draw.line(screen, NOIR, (400, 200), (400, 250), 3)
    if erreurs > 4:
        pygame.draw.circle(screen, ROUGE, (400, 270), 20, 5)
    if erreurs > 5:
        pygame.draw.line(screen, VERT, (400, 290), (400, 350), 10)
    if erreurs > 6:
        pygame.draw.line(screen, JAUNE, (400, 310), (360, 300), 5)
    if erreurs > 7:
        pygame.draw.line(screen, JAUNE, (400, 310), (440, 300), 5)
    if erreurs > 8:
        pygame.draw.line(screen, ROUGE, (400, 350), (380, 400), 8)
    if erreurs > 9:
        pygame.draw.line(screen, ROUGE, (400, 350), (420, 400), 8)


while en_cours:
    screen.fill(BLANC)
    

    # Affichage du mot deviné
    texte = POLICE.render(" ".join(devine), True, BLEU)
    screen.blit(texte, (LARGEUR // 2 - texte.get_width() // 2, 100))

    # Affichage du pendu
    dessiner_pendu(erreurs)

    # Vérification des conditions de fin
    if erreurs >= erreurs_max:
        texte = POLICE.render("Vous avez perdu !", True, OLIVE)
        screen.blit(texte, (LARGEUR // 2 - texte.get_width() // 2, 40))
        pygame.display.flip()
        pygame.time.wait(10000)
        en_cours = False

    if "_" not in devine:
        texte = POLICE.render("Vous avez gagné !", True, ROUGE)
        screen.blit(texte, (LARGEUR // 2 - texte.get_width() // 2, 40))
        pygame.display.flip()
        pygame.time.wait(10000)
        en_cours = False

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False
        if event.type == pygame.KEYDOWN:
            lettre = event.unicode.upper()
            if lettre.isalpha() and lettre not in lettres_devinees:
                lettres_devinees.add(lettre)
                if lettre in mot_choisi:
                    for i, char in enumerate(mot_choisi):
                        if char == lettre:
                            devine[i] = lettre
                else:
                    erreurs += 1

    pygame.display.flip()
    horloge.tick(1000)

pygame.quit()

