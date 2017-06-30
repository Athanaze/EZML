# coding: utf-8

import pygame
import time
from pygame.locals import *
from threading import Thread
import manitou
from manitou import Manitou
import const
from const import *


pygame.init()


manitou = Manitou()
conti = True
manitou.newRound()
#Recharge constante du mana
class BackgroundTimer(Thread):
    def run(self):
        while conti:
            time.sleep(5)
            manitou.mage.addMana(1)
            manitou.dragon.addMana(1)

timer = BackgroundTimer()
timer.start()


# Vérifie si les joueurs bougent
class BackgroundTimer2(Thread):
    def run(self):
        while conti:
            time.sleep(1)
            manitou.mage.putHistoCoord()
            hc = manitou.mage.getHistoCoord()
            hcD = manitou.dragon.getHistoCoord()

            # Si le mage ne bouge pas assez
            #if abs(hc[-1][0] - hc[-2][0]) < 5 or abs(hc[-1][1] - hc[-2][2]) < 5:
                # Si le dragon ne bouge pas assez
            #    if abs(hcD[-1][0] - hcD[-2][0]) < 5 or abs(hcD[-1][1] - hcD[-2][2]) < 5:
            #        manitou.gameOver(MAGE)

            # Si le dragon ne bouge pas assez
            #if abs(hcD[-1][0] - hcD[-2][0]) < 5 or abs(hcD[-1][1] - hcD[-2][2]) < 5:



timer2 = BackgroundTimer2()
timer2.start()


pygame.key.set_repeat(1, 1)
# BOUCLE DE JEU

while conti:
    pygame.time.Clock().tick(60)
    for e in pygame.event.get():
        if e.type == QUIT:
            conti = False

        if e.type == KEYDOWN:
            if e.key == K_UP:
                manitou.dragon.monter()

            if e.key == K_DOWN:
                manitou.dragon.des()

            if e.key == K_LEFT:
                manitou.dragon.gauche()

            if e.key == K_RIGHT:
                manitou.dragon.droite()

            if e.key == K_w:
                manitou.mage.monter()

            if e.key == K_s:
                manitou.mage.des()

            if e.key == K_a:
                manitou.mage.gauche()

            if e.key == K_d:
                manitou.mage.droite()

            if e.key == K_ESCAPE:
                conti = False

        if e.type == KEYUP:
            if e.key == K_e:
                manitou.tirerM()

            if e.key == K_RSHIFT:
                manitou.tirerD()

    manitou.refresh()
    pygame.display.flip()

if conti == False:
    manitou.graph()
