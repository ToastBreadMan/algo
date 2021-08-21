import pygame
import math
import time

step_size = 3

class Character:
    def __init__(self, x, y, rotation, display, fov, display3d):
        self.x = x
        self.y = y
        self.rotation = rotation
        self.display = display
        self.fov = fov
        self.display3d = display3d

    def render(self):
        pygame.draw.circle(self.display, (255, 0, 0), (self.x, self.y), 5)

    def see(self):
        angle = 1
        while int(angle) <= 360:
            step_val = 0
            print(angle)
            while True:
                end_x = (math.sin(self.rotation + angle * math.pi / 180) * step_val) + self.x
                end_y = (math.cos(self.rotation + angle * math.pi / 180) * step_val) + self.y
                """
                if end_x >= WIDTH or end_y >= HEIGHT or end_x <= 1 or end_y <= 1 or display.get_at((int(end_x), int(end_y))) == (255,255,255,255):
                    print('stopped', end_x,end_y)
                    break
                """
                if end_x <= 0:
                    break
                if end_y <= 0:
                    break
                if end_y >= HEIGHT:
                    break
                if end_x >= WIDTH:
                    break
                if display.get_at((int(end_x), int(end_y))) == (255,255,255):
                    break
                step_val += step_size
                pygame.draw.line(self.display, (255, 0, 0), (self.x, self.y), (end_x, end_y))
            angle += 3

    def see_angle(self):
        min_angle = -self.fov//2
        max_angle = self.fov//2
        for i in range(min_angle, max_angle):
            step_val = 0
            while True:
                end_x = (math.sin((self.rotation + i) * math.pi / 180) * step_val) + self.x
                end_y = (math.cos((self.rotation + i) * math.pi / 180) * step_val) + self.y
                if end_x <= 0:
                    break
                if end_y <= 0:
                    break
                if end_y >= HEIGHT:
                    break
                if end_x >= WIDTH:
                    break
                if display.get_at((int(end_x), int(end_y))) == (255, 255, 255):
                    if step_val != 0:
                        pygame.draw.circle(self.display3d, (255,255,255), (end_x - WIDTH/2, HEIGHT/2), (1/step_val) * 1000)
                    break
                pygame.draw.line(self.display, (255,0,0), (self.x, self.y), (end_x, end_y))
                # maybe with value mapping ?
                step_val += 1

        #TODO:HAS TO HAVE MULTIBLE WINDOWS

run = True
WIDTH = 800
HEIGHT = 800
pygame.init()
display = pygame.display.set_mode((800, 800))
pygame.init()
display3d = pygame.display.set_mode((900,900), 1)
player = Character(WIDTH/2, HEIGHT/2, 0, display, 90, display3d)

while run:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.rotation += 1
            if event.key == pygame.K_RIGHT:
                player.rotation -= 1

    pygame.draw.line(display, (255,255,255), (0,0), (WIDTH, HEIGHT-200), 10)
    pygame.draw.line(display, (255,255,255), (WIDTH, 0), (WIDTH/2, HEIGHT), 10)

    player.x = mouse_x
    player.y = mouse_y
    # player.render()
    player.see_angle()

    pygame.display.update()
    display.fill((0,0,0))

