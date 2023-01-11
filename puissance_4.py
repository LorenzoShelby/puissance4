import pygame
import pygame.mixer
import pygame_menu
import time 
import random

import verifP4 as v
import verifP4_2 as v2

pygame.mixer.get_init()
pygame.init()
size = (692,790)
scorejaune = 0
scorerouge = 0
screen = pygame.display.set_mode (size)
pygame.display.set_caption("Puissance 4")
myfont = pygame.font.SysFont("monospace",32,0)
pion1 = pygame.image.load("PionJaune.png")
pion2 = pygame.image.load("PionRouge.png")
son =pygame.mixer.Sound("sonvictoire1.wav")
sonjeu =pygame.mixer.Sound("sonjeu.wav")



M = [[0, 0, 0, 0, 0, 0, 0], \
     [0, 0, 0, 0, 0, 0, 0], \
     [0, 0, 0, 0, 0, 0, 0], \
     [0, 0, 0, 0, 0, 0, 0], \
     [0, 0, 0, 0, 0, 0, 0], \
     [0, 0, 0, 0, 0, 0, 0]]

def pp(a,b,jj):
        pion1 = pygame.image.load("PionJaune.png")
        pion2 = pygame.image.load("PionRouge.png")
        screen.blit(j12(jj,pion1,pion2), (position(a, b,j12(jj,pion1,pion2),pion1,pion2)))

def qqj(j):
    if j%2 == 0:
        return 1
    elif j%2 == 1:
        return 2


def j12(j,pion1,pion2):
    if j%2 == 0 :
        return pion1
    return pion2

def position(a,b,j,pion1,pion2):
    if(0 <= a <100):
        a = 15
        c = 0
    elif(100 <=a <200):
        a = 113
        c = 1
    elif(200 <= a <300):
        a = 213
        c = 2
    elif(300 <= a <400):
        a = 305
        c = 3
    elif(400 <= a <500):
        a = 402
        c = 4
    elif 500 <=a <589:
        a = 503
        c = 5
    else:
        a = 597
        c = 6
    return a, (pm(c,j,pion1)*97.5+140)


def positionlmax(a):
    if(0 <= a <100):
        a = 15
        c = 0
        return c
    elif(100 <=a <200):
        a = 113
        c = 1
        return c
    elif(200 <= a <300):
        a = 213
        c = 2
        return c
    elif(300 <= a <400):
        a = 305
        c = 3
        return c
    elif(400 <= a <500):
        a = 402
        c = 4
        return c
    elif 500 <=a <589:
        a = 503
        c = 5
        return c
    else:
        a = 597
        c = 6
        return c


def veriflmax(a):
    c= positionlmax(a)
    if M[0][c] != 0:
        print('ikl y a un point')
        return True
        
def pm(a,j,pion1):
    jo=0
    if j==pion1:
        jo=1
    else:
        jo=2
    for i in range(5, 0, -1):
        if(M[i][a] == 0):
            M[i][a]=jo
            print(M)
            return i
    M[0][a]=jo
    return 0



class Game:
    def Run():
        jetonjoue=0
        global scorejaune
        global scorerouge
        global M
        M = [[0, 0, 0, 0, 0, 0, 0], \
            [0, 0, 0, 0, 0, 0, 0], \
            [0, 0, 0, 0, 0, 0, 0], \
            [0, 0, 0, 0, 0, 0, 0], \
            [0, 0, 0, 0, 0, 0, 0], \
            [0, 0, 0, 0, 0, 0, 0]]
        image = pygame.image.load ("Grille.png")
        titre=pygame.image.load("titre.png")
        score_jaune= myfont.render(f"Score du Jaune : {scorejaune}", 1, (255,255,0))
        score_rouge= myfont.render(f"Score du Rouge : {scorerouge}", 1, (255,0,0))
        screen.blit (image, (0,130))
        screen.blit(titre,(220,0))
        screen.blit(score_jaune, (0,720))
        screen.blit(score_rouge, (0,750))
        pygame.display.flip ()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type==pygame.MOUSEBUTTONUP:
                    
                    x,y= pygame.mouse.get_pos()
                   
                    if veriflmax(x) == True:
                        pass
                    else:
                        pp(x,y,jetonjoue)
                        pygame.display.flip()
                        sonjeu.play()
                        if v.verif(M)==True:
                            if qqj(jetonjoue)==1:
                                scorejaune += 1
                                son.play()
                                winjaune()
                                
                            else:
                                scorerouge += 1
                                son.play()
                                winrouge()
                        if v.verif(M) == 4:
                            Null()
                        jetonjoue+=1
                
                elif event.type == pygame.QUIT:
                    running = False
        pygame.quit()

def jeuia():
    jetonjoue=0
    global M
    global scorejaune
    global scorerouge
    M = [[0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0]]

    image = pygame.image.load ("Grille.png")
    titre=pygame.image.load("titre.png")
    score_jaune= myfont.render(f"Score du Jaune : {scorejaune}", 1, (255,255,0))
    score_rouge= myfont.render(f"Score du Rouge : {scorerouge}", 1, (255,0,0))
    screen.blit (image, (0,130))
    screen.blit(titre,(220,0))
    screen.blit(score_jaune, (0,720))
    screen.blit(score_rouge, (0,750))
    pygame.display.flip ()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONUP:
                x,y= pygame.mouse.get_pos()
                if veriflmax(x) == True:
                        pass
                else:

                    screen.blit(pion1, (position(x, y,j12(jetonjoue,pion1,pion2),pion1,pion2)))
                    pygame.display.flip()
                    sonjeu.play()
                    if v.verif(M)==True:
                        scorejaune += 1
                        son.play()
                        winj1()
                    if v.verif(M) == 4:
                        Null2()
                    jetonjoue+=1
                    time.sleep(0.5)
                    e=random.randint(0, 589)
                    screen.blit(pion2, (position(e, y,j12(jetonjoue,pion1,pion2),pion1,pion2)))
                    pygame.display.flip()
                    sonjeu.play()
                    if v.verif(M)==True:
                        if v.verif(M)==True:
                            scorerouge += 1
                            son.play()
                            winj2()
                        if v.verif(M) == 4:
                            Null2()
                    jetonjoue+=1
            elif event.type == pygame.QUIT:
                    running = False

def jeuia2():
    jetonjoue=0
    global M
    global scorejaune
    global scorerouge
    M = [[0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0]]

    image = pygame.image.load ("Grille.png")
    titre=pygame.image.load("titre.png")
    score_jaune= myfont.render(f"Score du Jaune : {scorejaune}", 1, (255,255,0))
    score_rouge= myfont.render(f"Score du Rouge : {scorerouge}", 1, (255,0,0))
    screen.blit (image, (0,130))
    screen.blit(titre,(220,0))
    screen.blit(score_jaune, (0,720))
    screen.blit(score_rouge, (0,750))
    pygame.display.flip ()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONUP:

                x,y= pygame.mouse.get_pos()
                if veriflmax(x) == True:
                        pass
                else:
                    screen.blit(pion1, (position(x, y,j12(jetonjoue,pion1,pion2),pion1,pion2)))
                    pygame.display.flip()
                    sonjeu.play()
                    if v.verif(M)==True:
                        scorejaune += 1
                        son.play()
                        winj1_2()
                    if v.verif(M) == 4:
                        Null2_2()
                    jetonjoue+=1
                    time.sleep(0.5)
                    if v2.verif(M) != None:
                        if veriflmax(x) == True:
                            pass
                        else:
                            screen.blit(pion2, (position(v2.verif(M), y,j12(jetonjoue,pion1,pion2),pion1,pion2)))
                    else:
                        print('il va la')
                        e=random.randint(0, 589)
                        while veriflmax(e) == True:
                            e = random.randint(0, 589)
                        screen.blit(pion2, (position(e, y,j12(jetonjoue,pion1,pion2),pion1,pion2)))
                    pygame.display.flip()
                    sonjeu.play()
                    if v.verif(M)==True:
                        if v.verif(M)==True:
                            scorerouge += 1
                            son.play()
                            winj2_2()
                        if v.verif(M) == 4:
                            Null2_2()
                    jetonjoue+=1
            elif event.type == pygame.QUIT:
                    running = False

def menu():
    menu = pygame_menu.Menu('PUISSANCE 4!', 400, 300,theme=pygame_menu.themes.THEME_BLUE)
    global scorejaune
    global scorerouge
    scorejaune=0
    scorerouge=0
    menu.add.button('1 Joueur', sousmenu)
    menu.add.button('2 Joueurs', Game.Run)
    menu.add.button('Quitter', pygame_menu.events.EXIT)
    menu.mainloop(screen)
    pygame.quit()

def sousmenu():
    menu = pygame_menu.Menu('Choisir dificulté', 400, 300,theme=pygame_menu.themes.THEME_BLUE)
    menu.add.button('facile',jeuia )
    menu.add.button('difficile',jeuia2)
    menu.add.button('Quitter', pygame_menu.events.EXIT)
    menu.mainloop(screen)
    pygame.quit()
    
def winrouge():
        ga=pygame_menu.Menu('Le joueur Rouge Gagne!', 500, 400, theme=pygame_menu.themes.THEME_BLUE)
        ga.add.button('Continuer', Game.Run)
        ga.add.button('Retour au menu', menu)
        ga.add.button('Quitter', pygame_menu.events.EXIT)
        ga.mainloop(screen)
        pygame.quit()

def winjaune():
        ga2=pygame_menu.Menu('Le joueur Jaune Gagne!', 500, 400, theme=pygame_menu.themes.THEME_BLUE)
        ga2.add.button('Continuer', Game.Run)
        ga2.add.button('Retour au menu', menu)
        ga2.add.button('Quitter', pygame_menu.events.EXIT)
        ga2.mainloop(screen)
        pygame.quit()

def Null():
    ga3=pygame_menu.Menu('Egalité!', 500, 400, theme=pygame_menu.themes.THEME_BLUE)
    ga3.add.button('Continuer', Game.Run)
    ga3.add.button('Retour au menu', menu)
    ga3.add.button('Quitter', pygame_menu.events.EXIT)
    ga3.mainloop(screen)
    pygame.quit

def winj1():
        ga=pygame_menu.Menu('Le joueur Jaune Gagne!', 500, 400, theme=pygame_menu.themes.THEME_BLUE)
        ga.add.button('Continuer', jeuia)
        ga.add.button('Retour au menu', menu)
        ga.add.button('Quitter', pygame_menu.events.EXIT)
        ga.mainloop(screen)
        pygame.quit()

def winj2():
        ga2=pygame_menu.Menu('Le joueur Rouge Gagne!', 500, 400, theme=pygame_menu.themes.THEME_BLUE)
        ga2.add.button('Continuer', jeuia)
        ga2.add.button('Retour au menu', menu)
        ga2.add.button('Quitter', pygame_menu.events.EXIT)
        ga2.mainloop(screen)
        pygame.quit()

def winj1_2():
        ga=pygame_menu.Menu('Le joueur Jaune Gagne!', 500, 400, theme=pygame_menu.themes.THEME_BLUE)
        ga.add.button('Continuer', jeuia2)
        ga.add.button('Retour au menu', menu)
        ga.add.button('Quitter', pygame_menu.events.EXIT)
        ga.mainloop(screen)
        pygame.quit()

def winj2_2():
        ga2=pygame_menu.Menu('Le joueur Rouge Gagne!', 500, 400, theme=pygame_menu.themes.THEME_BLUE)
        ga2.add.button('Continuer', jeuia2)
        ga2.add.button('Retour au menu', menu)
        ga2.add.button('Quitter', pygame_menu.events.EXIT)
        ga2.mainloop(screen)
        pygame.quit()

def Null2_2():
    ga3=pygame_menu.Menu('Egalité!', 500, 400, theme=pygame_menu.themes.THEME_BLUE)
    ga3.add.button('Continuer', jeuia2)
    ga3.add.button('Retour au menu', menu)
    ga3.add.button('Quitter', pygame_menu.events.EXIT)
    ga3.mainloop(screen)
    pygame.quit()

def Null2():
    ga3=pygame_menu.Menu('Egalité!', 500, 400, theme=pygame_menu.themes.THEME_BLUE)
    ga3.add.button('Continuer', jeuia)
    ga3.add.button('Retour au menu', menu)
    ga3.add.button('Quitter', pygame_menu.events.EXIT)
    ga3.mainloop(screen)
    pygame.quit()

menu()
