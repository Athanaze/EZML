# coding: utf-8
import pygame
from pygame.locals import *
import const
from const import *
import manaBar
from manaBar import ManaBar
import dragon
import mage
from dragon import Dragon
from mage import Mage
import ball
from ball import Ball
import time
import matplotlib.pyplot as plt
class Manitou:
    def __init__(self):
        self.round = 0
        # Initialise le jeu
        self.fen = pygame.display.set_mode((LONG, LARGE))
        self.fond = pygame.image.load("fond.png").convert()
        self.fond = pygame.transform.scale(self.fond, (1014, 534))
        self.fen.blit(self.fond, (0, 0))

        loop = pygame.mixer.Sound("loop.wav")
        loop.play()

        self.imgFBall = pygame.transform.scale(pygame.image.load("assets/balls/fireball.gif").convert_alpha(), (160, 160))
        self.imgIBall = pygame.transform.scale(pygame.image.load("assets/balls/iceball.gif").convert_alpha(), (160, 160))

        self.fBall = pygame.sprite.Group()
        self.iBall = pygame.sprite.Group()

        self.mage = Mage()
        self.dragon = Dragon()
        #Bar de mana
        self.manab = ManaBar(self.mage.getMana())
        self.manabD = ManaBar(self.dragon.getMana())
        self.imgGo = pygame.transform.scale(pygame.image.load("go.png").convert_alpha(), (602, 322))

        pygame.display.flip()

    def newRound(self):

        for f in self.fBall:
            f.kill()

        for i in self.iBall:
            i.kill()
        self.mage.setPos(POS_INIT_M)
        self.dragon.setPos(POS_INIT_D)

        self.mage.putHistoMana()
        self.dragon.putHistoMana()

        self.round += 1
        print('Le round ', self.round, 'commence !')
        
    def gameOver(self, perdant):
        
        #self.fen.blit(self.imgGo, (GO_X, GO_Y))
        print("== Game Over ==")
        
        if perdant == MAGE:
            self.mage.perdre()
            self.dragon.gagner()

        if perdant == DRAGON:
            self.dragon.perdre()
            self.mage.gagner()
        self.newRound()
        print("Ratio du mage")
        print(self.mage.getRatio())
        print("Ratio du dragon")
        print(self.dragon.getRatio())

    def tirerD(self):
        if self.dragon.getMana() > 0:
            self.fBall.add(Ball(self.imgFBall, (self.dragon.rect.x - 100, self.dragon.rect.y + 43)))
            self.dragon.perdreMana(1)

    def tirerM(self):
        if self.mage.getMana() > 0:
            self.iBall.add(Ball(self.imgIBall, (self.mage.rect.x + 110, self.mage.rect.y + 100)))
            self.mage.perdreMana(1)

    def refresh(self):


        self.manab.refr(self.mage.getMana())
        self.manabD.refr(self.dragon.getMana())

        self.fen.blit(self.fond, (0, 0))

        self.fen.blit(self.mage.getImg(), self.mage.getRect())
        self.fen.blit(self.dragon.getImg(), self.dragon.getRect())

        self.fen.blit(self.manab.getImg(), (self.mage.getCoord()[0] + 100, self.mage.getCoord()[1] + 30))
        self.fen.blit(self.manabD.getImg(), (self.dragon.getCoord()[0] + 10, self.dragon.getCoord()[1] - 10))

        for i in self.iBall:
            i.rect.x += 3
            self.fen.blit(i.image, i.rect)
            # conti = i.checkCol(self.dragon)
            if i.checkCol(self.dragon):
                self.gameOver(1)
            if i.isOut():
                i.kill()

        for j in self.fBall:
            j.rect.x -= 3
            self.fen.blit(j.image, j.rect)

            # conti = j.checkCol(self.mage)
            if j.checkCol(self.mage):
                self.gameOver(0)

            if j.isOut():
                j.kill()
    
    def graph(self):
        plt.plot(self.dragon.getHistoRatio(), linewidth=5, label="Dragon")
        plt.plot(self.mage.getHistoRatio(), linewidth=5, label="Mage")
        plt.plot(self.dragon.getHistoMana(), linewidth=5, label="Mana du dragon")
        plt.plot(self.mage.getHistoMana(), linewidth=5, label="Mana du mage")
        
        plt.ylabel('Ratio et mana')
        plt.xlabel('Round')
        plt.axis([-10, self.round, 0, 50])
        plt.legend() 
        plt.show()