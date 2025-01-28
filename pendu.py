import pygame
import random
pygame.init()

#bongiorno
window=pygame.display.set_mode((500,500))


wordlist=["one", "two", "three", "four", "five", "six", "seven"]

def pen():
    score=0
    running=True
        
    while score<8 and running:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False

        keys=pygame.key.get_pressed()
        if keys[pygame.K_q]:
            exit()
        if keys[pygame.K_SPACE]:
            score+=1
            
        pygame.display.update()
        window.fill((255,255,255))

        pygame.draw.line(window, (114,73,30), (50,400),(250,400), 5)# base

        pygame.draw.line(window, (114,73,30), (100,400),(100,275), 5)# pillar

        pygame.draw.line(window, (114,73,30), (100,275),(175,275), 5)# hanger

        if score==1: #hangman drawing if statements\/
            pygame.draw.line(window, (142,89,60), (175,275),(175,300), 1)# noose
        if score==2:
            pygame.draw.line(window, (142,89,60), (175,275),(175,300), 1)# noose
            pygame.draw.circle(window,(0,0,0), (175,300),10.0,0)# head
        if score==3:
            
            pygame.draw.line(window, (142,89,60), (175,275),(175,300), 1)# noose
            pygame.draw.circle(window,(0,0,0), (175,300),10.0,0)# head
            pygame.draw.line(window, (0,0,0), (175,300),(175,350), 3)# body
            
        if score==4:
            
            pygame.draw.line(window, (142,89,60), (175,275),(175,300), 1)# noose
            pygame.draw.circle(window,(0,0,0), (175,300),10.0,0)# head
            pygame.draw.line(window, (0,0,0), (175,300),(175,350), 3)# body
            pygame.draw.line(window, (0,0,0), (175,315),(190,330), 3)# armR
        if score==5:
            
            pygame.draw.line(window, (142,89,60), (175,275),(175,300), 1)# noose
            pygame.draw.circle(window,(0,0,0), (175,300),10.0,0)# head
            pygame.draw.line(window, (0,0,0), (175,300),(175,350), 3)# body
            pygame.draw.line(window, (0,0,0), (175,315),(190,330), 3)# armR
            pygame.draw.line(window, (0,0,0), (175,315),(160,330), 3)# armL
        if score==6:
            pygame.draw.line(window, (142,89,60), (175,275),(175,300), 1)# noose
            pygame.draw.circle(window,(0,0,0), (175,300),10.0,0)# head
            pygame.draw.line(window, (0,0,0), (175,300),(175,350), 3)# body
            pygame.draw.line(window, (0,0,0), (175,315),(190,330), 3)# armR
            pygame.draw.line(window, (0,0,0), (175,315),(160,330), 3)# armL
            pygame.draw.line(window, (0,0,0), (175,350),(190,370), 3)# legR
        if score==7:
            pygame.draw.line(window, (142,89,60), (175,275),(175,300), 1)# noose
            pygame.draw.circle(window,(0,0,0), (175,300),10.0,0)# head
            pygame.draw.line(window, (0,0,0), (175,300),(175,350), 3)# body
            pygame.draw.line(window, (0,0,0), (175,315),(190,330), 3)# armR
            pygame.draw.line(window, (0,0,0), (175,315),(160,330), 3)# armL
            pygame.draw.line(window, (0,0,0), (175,350),(190,370), 3)# legR
            pygame.draw.line(window, (0,0,0), (175,350),(160,370), 3)# legL
            

        



def main():
    running=True
    while running:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
    
        '''score=0
        pen(score)'''
        
        
pen()