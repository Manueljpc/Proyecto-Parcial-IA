
import pygame
import sys
from Jugador import jugador
from enemigo import enemigo
from Mapa import mapa

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("furtivité dans l'ombre")
clock = pygame.time.Clock()


mi_mapa = mapa()


personaje = jugador (100,100)


running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
#mover al jugador

    keys = pygame.key.get_pressed()
    
    
    paredes_del_mapa = mi_mapa.obtener_paredes()
    
    escondites_del_mapa = mi_mapa.obtener_escondites()
    
    personaje.movimiento(keys, paredes_del_mapa, escondites_del_mapa )
    
#darle color al fondo
    screen.fill((200, 200, 200))
    
    mi_mapa.draw(screen)
    

    personaje.draw(screen)
    
    
    
    pygame.display.flip()

    clock.tick(60) 
     
pygame.quit()
sys.exit()