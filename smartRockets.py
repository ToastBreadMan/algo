import time

import pygame
import random
import math

class Rocket:
    def __init__(self, width, height, display, goal):
        self.x = width/2
        self.y = 0
        self.moves = [] # maybe five ? designated locations
        self.display = display
        self.goal = goal
        self.score = 0
        for i in range(2):
            self.moves.append((random.uniform(0, width), random.uniform(0, height)))

    def move(self):
        index = 0
        for i in range(1*30):
            if i % 30 == 0:
                index += 1
            dx, dy = (self.moves[index][0] - self.x, self.moves[index][1] - self.y)#problem is here
            stepx, stepy = (dx / 30., dy / 30.)
            self.x = self.x + stepx
            self.y = self.y + stepy
            self.render()
        self.calc_score()

    def render(self):
        pygame.draw.circle(self.display, (255, 0, 0), (self.x, self.y), 5)
        pygame.display.update()
        self.calc_score()

    def calc_score(self):
        distance = math.sqrt((goal[0]-self.x)**2+(goal[1]-self.y))
        self.score = 1/distance

WIDTH = 500
HEIGHT = 500
run = True

pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))

rockets = []

goal = (WIDTH/2, HEIGHT)

for rocket in range(6):
    rockets.append(Rocket(WIDTH, HEIGHT, display, goal))

while run: #Generation over after every iteration
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

    pygame.draw.circle(display, (0,0,255), (goal[0], goal[1]), 5)
    for rocket in rockets:
        rocket.move()
        display.fill((0, 0, 0))
        pygame.draw.circle(display, (0, 0, 255), (goal[0], goal[1]), 5)

    time.sleep(0.2)
    mating_pool = []
    for rocket in rockets:
        num = int(rocket.score * 100 * 10)
        for i in range(num):
            mating_pool.append(rocket)
    for rocket in rockets:
        mating_partner = random.choice(mating_pool)
        while True:
            if mating_partner is rocket:
                mating_partner = random.choice(mating_pool)
            else:
                break
        dna = []
        mpdna = mating_partner.moves[len(mating_partner.moves)//2:]
        rdna = rocket.moves[:len(rocket.moves)//2]
        rocket.moves = mpdna + rdna
        rocket.score = 0
        rocket.x = WIDTH/2
        rocket.y = 0
        print("RESET!")
