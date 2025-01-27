import pygame
import random
import os


pygame.init()


# Configuration de la fenêtre
LARGEUR, HAUTEUR = 700, 600
screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("PENDU. Devinez le mot.")


# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
BLEU = (0, 0, 255)
VERT = (0, 128, 0)


# Police
POLICE = pygame.font.SysFont("chalkduster.ttf", 50)
PETITE_POLICE = pygame.font.SysFont("chalkduster.ttf", 30)


# Chemin vers le fichier de mots
chemin_dossier = "./"
chemin_fichier = os.path.join(chemin_dossier, "mots.txt")


# Lecture ou création du fichier mots.txt
if not os.path.exists(chemin_fichier):
    with open(chemin_fichier, "w") as f:
        f.write("PENDU\nPYTHON\nPROGRAMMATION\n")


# Fonction pour ajouter un mot dans mots.txt
def ajouter_mot():
    ajout_en_cours = True
    input_text = ""


    while ajout_en_cours:
        screen.fill(BLANC)


        texte = POLICE.render("Ajoutez un mot:", True, NOIR)
        screen.blit(texte, (LARGEUR // 2 - texte.get_width() // 2, 100))


        input_surface = POLICE.render(input_text, True, BLEU)
        screen.blit(input_surface, (LARGEUR // 2 - input_surface.get_width() // 2, 200))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and input_text.strip():
                    with open(chemin_fichier, "a") as f:
                        f.write(input_text.strip().upper() + "\n")
                    ajout_en_cours = False
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode


        pygame.display.flip()