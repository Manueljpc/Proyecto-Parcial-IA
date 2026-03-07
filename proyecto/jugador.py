import pygame

#la clase jugador con sus atributos
class jugador:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.tamaño = 30
        self.velocidad = 4
        self.vida = 100
        self.color = (0, 0, 100)
        self.escondido = False # esto es para cuando ponga el sistema de sigilo, si es que lo pongo
        
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
        pygame.draw.rect(screen, self.color,( self.x,self.y, self.tamaño, self.tamaño ))             