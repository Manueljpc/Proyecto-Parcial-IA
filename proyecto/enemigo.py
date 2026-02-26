import pygame

class enemigo:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.tamaño = 40
        self.velocidad = 2
        self.vida = 100
        
        self.color = (0, 255, 0)
        
                
    def draw(self,screen):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.tamaño,self.tamaño))  