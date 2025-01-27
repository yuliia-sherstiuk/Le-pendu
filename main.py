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






def end(winner):
    perduTxt = 'Perdu!'
    gagneTxt = 'Gagné!'
    #pygame.time.delay(1000)
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


while en_cours:
    screen.fill(BLANC)

    

    # Carré des lettres faux
    erreurs_rect=pygame.draw.rect(screen, ROUGE, (375, 275, 300, 100), 2)  
    erectX= erreurs_rect.left+10
    erectY= erreurs_rect.top+10

    # Affichage du lettres non correctes

    for lettre in lettres_devinees:
        if lettre in mot_choisi:
            continue
        lettre_surface=POLICE.render(lettre, True, ROUGE)
        lettre_rect=lettre_surface.get_rect()

        if erectX +lettre_rect.width>erreurs_rect.right-10:
            erectX=erreurs_rect.left+10
            erectY+=lettre_rect.height+5
        screen.blit(lettre_surface, (erectX, erectY))
        erectX+=lettre_rect.width+5
    

    # Affichage du pendu
    dessiner_pendu(erreurs)




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
    
    # Affichage du mot deviné
    texte = POLICE.render(" ".join(devine), True, BLEU)
    screen.blit(texte, (LARGEUR // 2 - texte.get_width() // 2, 100))

    if erreurs> erreurs_max:
        end(False)
    elif "_" not in devine:
        end(True)

    pygame.display.flip()
    horloge.tick(100)

pygame.quit()









