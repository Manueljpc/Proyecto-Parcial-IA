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
        
    def movimiento(self,keys, paredes, zonas_ocultas):
        #para guardar la posicion 
        old_x = self.x
        old_y = self.y
        
        if keys[pygame.K_w]:
            self.x -= self.velocidad #izquierda
        if keys[pygame.K_s]:
            self.x += self.velocidad #derecha
            
        rect_v_x = pygame.rect(self.x,self.y, self.tamaño, self.tamaño)
        # si el rectangulo del jugador toca una pared se anula el movimiento a la posicion anterior
        for pared in paredes:
            if rect_v_x.colliderect(pared):
                self.x = old_x  
            
        if keys[pygame.K_a]:     
            self.y -= self.velocidad # arriba
        if keys[pygame.K_d]:
            self.y += self.velocidad # abajo
               
        rect_v_y = pygame.rect(self.x,self.y, self.tamaño, self.tamaño)
        # si el rectangulo del jugador toca una pared se anula el movimiento a la posicion anterior
        for pared in paredes:
            if rect_v_y.colliderect(pared):
                self.y = old_y
                
                
        self.escondido = False # desde el principio no estamos escondidos
        for zona in zonas_ocultas:
            if rect_v_y.colliderect(zona):
                self.escondido = True
                    
                
    # esto es para mostrar al jugador cuando sea llamado            
    def draw(self,screen):
        color_final = (0,50,100)  
        
        if self.escondido: 
            color_final = (0,50,100) 
            
        else:
        
            color_final = self.color
        
        pygame.draw.rect(screen, color_final,( self.x,self.y, self.tamaño, self.tamaño ))             