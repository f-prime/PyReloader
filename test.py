import pygame

s = pygame.display.set_mode((800, 600))
c = pygame.time.Clock()
color = 0
color2 = 0
color3 = 0
while True:
    c.tick(60)
    if color < 255:
        color += 1
    if color == 255:
        if color2 < 255:
            color2 += 1
    if color2 == 255:
        if color3 < 255:
            color3 += 1
    if color  == 255 and color2 == 255 and color3  == 255:
        color = color2 = color3 = 0

    s.fill((color,color2,color3))
    pygame.display.update()
