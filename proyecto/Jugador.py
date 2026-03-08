import pygame

class jugador:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tamaño = 30
        self.velocidad = 4
        self.vida = 100
        self.color = (0, 0, 200)
        self.escondido = False

    def movimiento(self, keys, paredes, zonas_ocultas):
        #  Movimiento en Y (W/S) con su propia colisión 
        if keys[pygame.K_w]:
            self.y -= self.velocidad
        if keys[pygame.K_s]:
            self.y += self.velocidad

        # Rect solo para verificar colisión en Y
        rect_y = pygame.Rect(self.x, self.y, self.tamaño, self.tamaño)
        for pared in paredes:
            if rect_y.colliderect(pared):
                self.y += self.velocidad if keys[pygame.K_w] else -self.velocidad

        #  Movimiento en X (A/D) con su propia colisión 
        if keys[pygame.K_a]:
            self.x -= self.velocidad
        if keys[pygame.K_d]:
            self.x += self.velocidad

        #  Rect solo para verificar colisión en X
        rect_x = pygame.Rect(self.x, self.y, self.tamaño, self.tamaño)
        for pared in paredes:
            if rect_x.colliderect(pared):
                self.x += self.velocidad if keys[pygame.K_a] else -self.velocidad

        #  Detectar escondite 
        self.escondido = False
        rect_final = pygame.Rect(self.x, self.y, self.tamaño, self.tamaño)
        for zona in zonas_ocultas:
            if rect_final.colliderect(zona):
                self.escondido = True

    def draw(self, screen):
        if self.escondido:
            color_final = (0, 150, 0)   # verde = escondido
        else:
            color_final = self.color    # azul = visible

        pygame.draw.rect(screen, color_final, (self.x, self.y, self.tamaño, self.tamaño))