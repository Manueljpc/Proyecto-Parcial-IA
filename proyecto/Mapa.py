import pygame


import pygame

class mapa:
    def __init__(self):
        self.tile = 32
        self.matriz = [
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,2,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,2,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,1,1,1,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,2,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,1],
            [1,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        ]
        self.ancho = len(self.matriz[0])
        self.alto = len(self.matriz)

    def draw(self, screen):
        for fila in range(self.alto):
            for col in range(self.ancho):
                rect = pygame.Rect(col * self.tile, fila * self.tile, self.tile, self.tile)
                
                if self.matriz[fila][col] == 1:
                    pygame.draw.rect(screen, (50, 50, 50), rect)
                elif self.matriz[fila][col] == 2:
                    pygame.draw.rect(screen, (0, 80, 0), rect)
                else:
                    pygame.draw.rect(screen, (20, 20, 20), rect)

    def obtener_paredes(self):
        paredes = []
        for fila in range(self.alto):
            for col in range(self.ancho):
                if self.matriz[fila][col] == 1:
                    paredes.append(pygame.Rect(col * self.tile, fila * self.tile, self.tile, self.tile))
        return paredes

    def obtener_escondites(self):
        escondites = []
        for fila in range(self.alto):
            for col in range(self.ancho):
                if self.matriz[fila][col] == 2:
                    escondites.append(pygame.Rect(col * self.tile, fila * self.tile, self.tile, self.tile))
        return escondites        