import time

import pygame
import math
import time

pygame.init()
WIDTH = 500
HEIGHT = 500
display = pygame.display.set_mode((WIDTH, HEIGHT))
run = True
angle = 1

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
    for i in range(360):
        time.sleep(0.1)
        # IT JUST FUCKING WORKS
        end_x = (math.sin(i * (math.pi / 180)) * 100) + HEIGHT/2
        end_y = (math.cos(i *  math.pi / 180) * 100) + WIDTH/2
        pygame.draw.line(display, (255,255,255), (WIDTH/2, HEIGHT/2), (end_x, end_y))
        pygame.display.update()