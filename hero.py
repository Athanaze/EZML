# coding: utf-8
import pygame
from pygame.locals import *
import const
from const import *
class Hero(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, img, pos):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = pos[0]
        self.rect.centery = pos[1]
        self.mana = 7
        self.mask = pygame.mask.from_surface(self.image)
        self.ratio = 0
        self.histoRatio = [self.ratio]
        self.histoMana = [self.mana]
        self.histoCoord = [(self.rect.x, self.rect.y)]

    def depla(self, coord):
        self.rect.x = self.rect.x + coord[0]
        self.rect.y = self.rect.y + coord[1]

    def perdreMana(self, quant):
        if self.mana > 0:
            self.mana -= quant
    
    def getMana(self):
        return self.mana
        
    def addMana(self, quant):
        if self.mana < 7:
            self.mana += quant 
    def getCoord(self):
        return(self.rect.x, self.rect.y)

    def getImg(self):
        return self.image
    
    def getRect(self):
        return self.rect

    def perdre(self):
        self.ratio -= 1
        self.histoRatio.append(self.ratio)


    def gagner(self):
        self.ratio += 3
        self.histoRatio.append(self.ratio)

    def getRatio(self):
        return self.ratio
    
    def setPos(self, coord):
        self.rect.x = coord[0]
        self.rect.y = coord[1]

    def getHistoRatio(self):
        return self.histoRatio

    def putHistoMana(self):
        self.histoMana.append(self.mana)

    def getHistoMana(self):
        return self.histoMana

    def putHistoCoord(self):
        self.histoCoord.append((self.rect.x, self.rect.y))

    def getHistoCoord(self):
        return self.histoCoord    