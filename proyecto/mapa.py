import pygame
import random


ancho_mapa = 25 # 25 por 32 es igual a 800  
alto_mapa = 18 # 18 por 32 es igual a 576
tile = 32


class mapa:
    def __init__(self):
        
        #aqui 1 es igual a un muro y 0 es igual a suelo
        
        self.matriz = [[1 for _ in range(ancho_mapa)] for _ in range(alto_mapa)]
        self.obstaculos = []
        self.generar 
        
    def generar(self):
        cantidad_habitaciones = 6
        
        for in range(cantidad_habitaciones):
            w = random.randint(4, 7)
            h = random.randint(4, 7)
            x = random.randint()
            y = random.randint()
            