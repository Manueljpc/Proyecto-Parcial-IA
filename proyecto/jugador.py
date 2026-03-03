import pygame
import os
#la clase jugador con sus atributos
class jugador:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.tamaño = 40
        self.velocidad = 4
        self.vida = 100
        self.color = (0, 0, 100)
        
        #sprites
        
        ruta = os.path.join("assets","imagenes","sprites","player.png")
        self.sprite = pygame.image.load(ruta).convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite,(self.tamaño,self.tamaño))
        
        
        #movimientos del jugador
        
    def movimiento(self,keys):
        if keys[pygame.K_w]:
            self.y -= self.velocidad
        if keys[pygame.K_s]:
            self.y += self.velocidad
        if keys[pygame.K_a]:     
            self.x -= self.velocidad
        if keys[pygame.K_d]:
            self.x += self.velocidad
                
    # esto es para mostrar al jugador cuando sea llamado            
    def draw(self,screen):
        pygame.blit(self.sprite,( self.x,self.y ))             