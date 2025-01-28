import pygame
import random
import os

LARGEUR, HAUTEUR = 700, 600
screen = pygame.display.set_mode((LARGEUR, HAUTEUR))

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

def end(winner):
    perduTxt = 'Perdu! Tappez sur le clavier pour jouer encore...'
    gagneTxt = 'Gagne! Encoure une fois?'
    pygame.time.delay(1000)
    screen.fill(BLANC)

    if winner:
        label = POLICE.render(gagneTxt, 1, NOIR)
    else:
        label = POLICE.render(perduTxt, 1, NOIR)

    wordTxt = POLICE.render(mot_choisi.upper(), 1, NOIR)
    wordWas = POLICE.render('Le mot a été: ', 1, NOIR)

    screen.blit(wordTxt, (LARGEUR / 2 - wordTxt.get_width() / 2, 295))
    screen.blit(wordWas, (LARGEUR / 2 - wordWas.get_width() / 2, 245))
    screen.blit(label, (LARGEUR / 2 - label.get_width() / 2, 140))
    pygame.display.update()