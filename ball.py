import pygame
from pygame.locals import *
import const
from const import *
class Ball(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, ball, coord):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = ball
        
        self.mask = pygame.mask.from_surface(self.image)
        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.x = coord[0]
        self.rect.y = coord[1]
    
    def checkCol(self, spr):
        return pygame.sprite.collide_mask(self, spr)
    
    def isOut(self):
        
        if self.rect.x > LONG:
            return True
        
        elif self.rect.x < 0:
            return True
        
        else:
            return False
        
    def getCoord(self):
        return(self.rect.x, self.rect.y)