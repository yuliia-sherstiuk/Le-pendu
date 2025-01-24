
import pygame
import random

pygame.init()
winHeight = 600
winWidth = 700
win = pygame.display.set_mode((winWidth, winHeight))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
LIGHT_BLUE = (102, 255, 255)

btn_font = pygame.font.SysFont("arial", 20)
guess_font = pygame.font.SysFont("monospace", 24)
lost_font = pygame.font.SysFont('arial', 45)
word = ''
guessed = []
hangmanPics = [
    pygame.image.load('pendu1.png'),
    pygame.image.load('pendu2.png'),
    pygame.image.load('pendu3.png'),
    pygame.image.load('pendu4.png'),
    pygame.image.load('pendu5.png'),
    pygame.image.load('pendu6.png'),
    pygame.image.load('pendu7.png')
]

limbs = 0

def redraw_game_window():
    global guessed
    global hangmanPics
    global limbs

    win.fill(WHITE)

    # Display guessed word
    spaced = spacedOut(word, guessed)
    label1 = guess_font.render(spaced, 1, BLACK)
    rect = label1.get_rect()
    length = rect[2]
    win.blit(label1, (winWidth / 2 - length / 2, 100))

    # Display hangman image
    pic = hangmanPics[limbs]
    win.blit(pic, (winWidth / 2 - pic.get_width() / 2 + 20, 150))

    pygame.display.update()

def randomWord():
    file = open('words.txt')
    f = file.readlines()
    file.close()
    i = random.randrange(0, len(f) - 1)
    return f[i].strip()

def hang(guess):
    global word
    if guess.lower() not in word.lower():
        return True
    else:
        return False

def spacedOut(word, guessed=[]):
    spacedWord = ''
    for char in word:
        if char != ' ':
            if char.upper() in guessed:
                spacedWord += char.upper() + ' '
            else:
                spacedWord += '_ '
        else:
            spacedWord += ' '
    return spacedWord

def end(winner=False):
    global limbs
    lostTxt = 'You Lost! Press any key to play again...'
    winTxt = 'WINNER! Press any key to play again...'
    redraw_game_window()
    pygame.time.delay(1000)
    win.fill(GREEN)

    if winner:
        label = lost_font.render(winTxt, 1, BLACK)
    else:
        label = lost_font.render(lostTxt, 1, BLACK)

    wordTxt = lost_font.render(word.upper(), 1, BLACK)
    wordWas = lost_font.render('The word was: ', 1, BLACK)

    win.blit(wordTxt, (winWidth / 2 - wordTxt.get_width() / 2, 295))
    win.blit(wordWas, (winWidth / 2 - wordWas.get_width() / 2, 245))
    win.blit(label, (winWidth / 2 - label.get_width() / 2, 140))
    pygame.display.update()

    again = True
    while again:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                again = False
    reset()

def reset():
    global limbs
    global guessed
    global word

    limbs = 0
    guessed = []
    word = randomWord()

# MAINLINE
word = randomWord()
inPlay = True

while inPlay:
    redraw_game_window()
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inPlay = False
        if event.type == pygame.KEYDOWN:
            # Check if the key pressed is a letter
            if event.unicode.isalpha():
                letter = event.unicode.upper()
                if letter not in guessed:
                    guessed.append(letter)
                    if hang(letter):
                        if limbs != 6:
                            limbs += 1
                        else:
                            end()
                    else:
                        if spacedOut(word, guessed).count('_') == 0:
                            end(True)

pygame.quit()
# Always quit pygame when done
