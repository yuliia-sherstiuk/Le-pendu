import pygame


LARGEUR, HAUTEUR=700, 600

screen= pygame.display.set_mode((LARGEUR, HAUTEUR))

BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
OLIVE = (128, 128, 0)
VERT = (0,128, 0)
BLEU = (0,0,255)
JAUNE = (255,255,0)
MAROON = (128,0,0)

def dessiner_pendu(erreurs):
    if erreurs>0:
        pygame.draw.line(screen, NOIR, (50,400),(250,400), 5)# base

    if erreurs>1:
        pygame.draw.line(screen, MAROON, (100,400),(100,275), 5)# tronc     
    if erreurs>2:
        pygame.draw.line(screen, MAROON, (100,275),(175,275), 5)# branche

    if erreurs>3:
        pygame.draw.line(screen, MAROON, (175,275),(175,300), 1)# corde

    if erreurs>4:
        pygame.draw.circle(screen,NOIR, (175,300),10.0,0)# tête
    if erreurs>5:
        pygame.draw.line(screen, NOIR, (175,300),(175,350), 3)# corps
    if erreurs>6:
        pygame.draw.line(screen, NOIR, (175,315),(190,330), 3)# bras droit
    if erreurs>7:
        pygame.draw.line(screen, NOIR, (175,315),(160,330), 3)# bras gauche
    if erreurs>8:
        pygame.draw.line(screen, NOIR, (175,350),(190,370), 3)# jambe droit
    if erreurs>9:
        pygame.draw.line(screen, NOIR, (175,350),(160,370), 3)# jambe gauche