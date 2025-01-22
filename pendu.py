import pygame
import random
pygame.init()

screen = pygame.display.set_mode((640, 750))      
pygame.display.set_caption("Pendu")

BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
POLICE = pygame.font.Font(None, 100)

mots = ["MAISON", "CHAT", "CHIEN", "TRAIN", "MARCHE"]
mot_choisi = random.choice(mots)
devine = ["_"] * len(mot_choisi)
erreurs = 0
erreurs_max = 10
lettres_devinees = set()

en_cours = True
horloge = pygame.time.Clock()

while en_cours:
    screen.fill(BLANC)  

    texte = POLICE.render(" ".join(devine), True, NOIR)
    screen.blit(texte, (screen.get_width() // 2 - texte.get_width() // 2, 100))

    if erreurs >= erreurs_max:
        en_cours = False

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

