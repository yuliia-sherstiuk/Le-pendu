import pygame
import random
import os

pygame.init()

# Configuration de la fenêtre
LARGEUR, HAUTEUR = 700, 600
screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("  PENDU.   Devinez le mot. ")

# Police
POLICE = pygame.font.SysFont("chalkduster.ttf", 50)

# Initialisation des variables
erreurs = 0
erreurs_max = 10
horloge = pygame.time.Clock()
en_cours = True

# Chemin vers le fichier de mots
chemin_dossier = "./"
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
