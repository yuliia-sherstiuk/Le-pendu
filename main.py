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




def dessiner_bouton(surface, x,y,largeur,hauteur, texte, couleur, vol_couleur, police):
    global events
    souris_pos= pygame.mouse.get_pos()
    bouton_rect= pygame.Rect(x, y, largeur, hauteur)
    voler=bouton_rect.collidepoint(souris_pos)

    couleur_actuelle=vol_couleur if voler else couleur
    pygame.draw.rect(surface, couleur_actuelle, bouton_rect, border_radius=10)

    texte_surface=police.render(texte, True, BLANC)
    texte_rect=texte_surface.get_rect(center=(x+largeur//2, y +hauteur//2))
    surface.blit(texte_surface, texte_rect)
    if voler and pygame.mouse.get_pressed()[0]:
        return True
    return False



def ajouter_mot():
    ajout_en_cours = True
    input_text = ""


    while ajout_en_cours:
        screen.fill(BLANC)
        global events
        events=pygame.event.get()

        for event in events:
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()

        if dessiner_bouton(screen, LARGEUR/2, HAUTEUR/2, 200, 100, "Annuler", NOIR, ROUGE, POLICE):
            menu()
            return


        texte = POLICE.render("Ajoutez un mot:", True, NOIR)
        screen.blit(texte, (LARGEUR // 2 - texte.get_width() // 2, 100))


        input_surface = POLICE.render(input_text, True, BLEU)
        screen.blit(input_surface, (LARGEUR // 2 - input_surface.get_width() // 2, 200))


        for event in events:
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


def menu():
    global en_cours

    while en_cours:
        screen.fill(BLANC)
        events=pygame.event.get()

        if dessiner_bouton(screen, 100, 200, 200, 100, "Lancer ", NOIR, BLEU, POLICE ):
            boucle_principale()
        
        elif dessiner_bouton(screen, 350, 200, 300, 100, "Ajouter des mots", NOIR, BLEU, POLICE):
            ajouter_mot()
            pygame.event.clear()

        
        for event in events:
            if event.type==pygame.QUIT:
                en_cours=False

        pygame.display.flip()




def boucle_principale():
    global en_cours, erreurs, mot_choisi
    
    erreurs=0

    # Choix d'un mot aléatoire
    mot_choisi = random.choice(mots).upper()
    devine = ["_"] * len(mot_choisi)
    lettres_devinees = set()

    while en_cours:
        screen.fill(BLANC)
        events=pygame.event.get()

        

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

        if dessiner_bouton(screen, LARGEUR/2, 400, 150, 100, "Quitter", NOIR, ROUGE, POLICE):
            end(False)
            pygame.time.delay(2000)
            return




        for event in events:
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
            pygame.time.delay(2000)
            menu()
            return
        elif "_" not in devine:
            end(True)
            pygame.time.delay(2000)
            menu()
            return

        pygame.display.flip()
        horloge.tick(100)

menu()

pygame.quit()









