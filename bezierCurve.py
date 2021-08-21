import random
import time

import pygame

width = 500
height = 500

run = True
pygame.init()
display = pygame.display.set_mode((width, height))
randomX = []
randomY = []
randomY = randomY[::-1]
numsEndpoints = 4
iteration = 3
outer = None

def calc_x(i, x1, x2):
    px = (1-i)*x1+i*x2
    return px

def calc_y(i, y1, y2):
    py = (1-i)*y1+i*y2
    return py

def draw_curve(i, x1, y1, x2, y2):
    px = calc_x(i, x1, x2)
    py = calc_y(i, y1, y2)
    return px, py

def add_numbers(numsEndpoints):
    for i in range(numsEndpoints):
        randomX.append(random.uniform(0, width-width/4))
        randomY.append(random.uniform(0, height-height/4))

def calc_recursion(numsEndpoints):
    input_val = numsEndpoints
    steps = 0
    curr = input_val
    while True:
        if int(curr) != curr:
            steps += 1
            return steps
        if curr == 1:
            break
        curr = curr/2
        steps += 1
    return steps

def recursion(iteration):
    a = randomX[::2]
    b = randomX[1::2]
    c = randomY[::2]
    d = randomY[1::2]
    element_vals_x = list()
    element_vals_y = list()
    range_num =calc_recursion(numsEndpoints)
    for i in range(range_num):
        element_vals_x.append(calc_x(iteration, a[i], b[i]))
        element_vals_y.append(calc_y(iteration, c[i], d[i]))
    return draw_curve(iteration, element_vals_x[0], element_vals_y[0], element_vals_x[1], element_vals_y[1])
add_numbers(numsEndpoints)
print(recursion(0.2))

while run:
    iteration += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                randomX = list()
                randomY = list()

                add_numbers(numsEndpoints)
                iteration = 0
                display.fill((0, 0, 0))


    for i in range(numsEndpoints):
        pygame.draw.circle(display, (255,0,255), (randomX[i], randomY[i]), 4)

    for i in range(iteration):
        curr_curve_val = recursion(i/iteration)
        pygame.draw.circle(display, (255,255,255), (curr_curve_val[0], curr_curve_val[1]), 5)
        pygame.display.update()
    #display.fill((0,0,0))