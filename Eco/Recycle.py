import pygame
pygame.init()

WIDTH = 900
HEIGHT = 700
TITLE = "Recylce Marathon"

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)

bg = pygame.image.load("ecobg.png")
bg = pygame.transform.scale(bg, (WIDTH,HEIGHT))
screen.blit(bg,(0,0))

run = True

while run:
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
pygame.quit()
