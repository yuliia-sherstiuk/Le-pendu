import pygame
import random
pygame.init()

screen = pygame.display.set_mode((640, 750))      
pygame.display.set_caption("Pendu")

BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
POLICE = pygame.font.Font(None, 50)

mots = ["MAISON", "CHAT", "CHIEN", "TRAIN", "MARCHE"]
mot_choisi = random.choice(mots)
devine = ["_"] * len(mot_choisi)
erreurs = 0
erreurs_max = 11
lettres_devinees = set()

en_cours = True
horloge = pygame.time.Clock()


def dessiner_pendu(erreurs):
    # Base de la potence
    if erreurs > 0:
        pygame.draw.line(screen, NOIR, (150, 500), (500, 500), 7)  
    if erreurs > 1:
        pygame.draw.line(screen, NOIR, (300, 500), (300, 200), 15)  
    if erreurs > 2:
        pygame.draw.line(screen, NOIR, (295, 200), (400, 200),7)  
    if erreurs > 3:
        pygame.draw.line(screen, NOIR, (400, 200), (400, 250), 3) 
    if erreurs > 4:
        pygame.draw.circle(screen, NOIR, (400, 270), 20, 5)  
    if erreurs > 5:
        pygame.draw.line(screen, NOIR, (400, 290), (400, 350), 10)  
    if erreurs > 6:
        pygame.draw.line(screen, NOIR, (400,310), (360, 300), 5)  
    if erreurs > 7:
        pygame.draw.line(screen, NOIR, (400, 310), (440, 300), 5) 
    if erreurs > 8:
        pygame.draw.line(screen, NOIR, (400, 350), (380, 400), 8) 
    if erreurs > 9:
        pygame.draw.line(screen, NOIR, (400, 350), (420, 400), 8)  
   
    
 # Base 

while en_cours:
    screen.fill(BLANC)  

    texte = POLICE.render(" ".join(devine), True, NOIR)
    screen.blit(texte, (screen.get_width() // 2 - texte.get_width() // 2, 100))

    if erreurs >= erreurs_max:
        en_cours = False

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

    pygame.display.flip()
    horloge.tick(30)

pygame.quit()
