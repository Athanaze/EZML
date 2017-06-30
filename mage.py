# coding: utf-8
import pygame
from pygame.locals import *
import const
from const import *
import hero
from hero import Hero

class Mage(hero.Hero):
    
    def __init__(self):
        Hero.__init__(self, pygame.transform.scale(pygame.image.load("assets/mage/anim/run/0.png").convert_alpha(), (AGRAN_M[0], AGRAN_M[1])), POS_INIT_M)
    
    def peutDepla(self, coord):
        newX = self.rect.x + coord[0]
        newY = self.rect.y + coord[1]
    
        newCX = self.rect.centerx + coord[0]
        newCY = self.rect.centery + coord[1]
        if newCX > 56 and newCX < 934 and newCY > 130 and newCY < 456:
            return True
        else:
            return False
            
        
    def monter(self):
        if self.peutDepla((0, -U)):
            self.depla((0, -U))
            
    def des(self):
        if self.peutDepla((0, U)):
            self.depla((0, U))
            
    def gauche(self):
        if self.peutDepla((-U, 0)):
            self.depla((-U, 0))
            
    def droite(self):
        if self.peutDepla((U, 0)):
            self.depla((U, 0))    
        
        