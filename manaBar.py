import pygame
from pygame.locals import *
class ManaBar(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self,mana):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        self.ss = [pygame.transform.scale(pygame.image.load("assets/mana/rainbow/0.png").convert_alpha(), (140, 40)),
                   pygame.transform.scale(pygame.image.load("assets/mana/rainbow/1.png").convert_alpha(), (140, 40)),
                   pygame.transform.scale(pygame.image.load("assets/mana/rainbow/2.png").convert_alpha(), (140, 40)),
                   pygame.transform.scale(pygame.image.load("assets/mana/rainbow/3.png").convert_alpha(), (140, 40)),
                   pygame.transform.scale(pygame.image.load("assets/mana/rainbow/4.png").convert_alpha(), (140, 40)),
                   pygame.transform.scale(pygame.image.load("assets/mana/rainbow/5.png").convert_alpha(), (140, 40)),
                   pygame.transform.scale(pygame.image.load("assets/mana/rainbow/6.png").convert_alpha(), (140, 40)),
                   pygame.transform.scale(pygame.image.load("assets/mana/rainbow/7.png").convert_alpha(), (140, 40))]
        
        for i in self.ss:
            i = pygame.transform.scale(i, (140, 40))
        self.image = self.ss[mana]
        
        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()

    def refr(self, mana):
        self.image = self.ss[mana]
        
    def getImg(self):
        return self.image
        