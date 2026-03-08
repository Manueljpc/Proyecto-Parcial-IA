import pygame


class mapa:
    def __init__(self):
        
        #aqui 1 es igual a un muro y 0 es igual a suelo
        
        self.tile = 32 # el tamaño de las celdas en pixeles
        self.matriz = [
            # el 1 representan paredes el 2 esondites y el 0 piso, por donde se puede transitar
        [1,1,1,1,1,1,1,1],
        [1,0,2,0,0,0,0,1],
        [1,0,0,0,2,0,0,1],
        [1,1,1,1,1,1,1,1]
            
            
               
        ]
        
        self.ancho = len(self.matriz[0])# lo que hace es calcular el ancho basado en la lista
        self.alto = len(self.matriz) # lo mismo pero para lo alto
        
        
    def draw (self,screen):
        
        for fila in range(self.alto):
            for col in range(self.ancho):
                rect = pygame.Rect(col * self.tile, fila * self.tile, self.tile, self.tile) 
        
        
            if self.matriz[fila][col] == 1:
                pygame.draw.rect(screen, (50, 50, 50), rect)
            elif self.matriz[fila][col] == 2:
                pygame.draw.rect(screen, (0, 80, 0), rect)
            else:
                pygame.draw.rect(screen,(20,20,20),rect)        
                pygame.draw.rect()     
                
    
    def obtener_paredes(self):
        paredes = []
        for fila in range(self.alto):
            for col in range(self.ancho):
                if self.matriz[fila][col] == 1:
                    paredes.append(pygame.rect(col*self.tile, fila*self.tile, self.tile, self.tile, self.tile ))               