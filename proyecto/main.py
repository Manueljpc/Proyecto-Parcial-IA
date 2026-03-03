
import pygame
from jugador import jugador
from enemigo import enemigo

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("furtivité dans l'ombre")
clock = pygame.time.Clock()

jugador = jugador(100,100)
enemigo = enemigo(400,300)
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
#mover al jugador
    keys = pygame.key.get_pressed()
    jugador.movimiento(keys)
#darle color al fondo
    screen.fill((0, 0, 255))
    jugador.draw(screen)
    enemigo.draw(screen)

    
    pygame.display.flip()

    clock.tick(60)  

pygame.quit()