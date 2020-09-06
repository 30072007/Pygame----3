import pygame

#initailazation
pygame.init()

#display here, >>((800, 600))<< you can tell your height and length in pixels
screen = pygame.display.set_mode((800, 600))

#Text and icon
pygame.display.set_caption("name of your window")
icon = pygame.image.load('joystick.png')
pygame.display.set_icon(icon)

#last time we added this (up there)
##now this

#player
Playerimg = pygame.image.load('player.png')
PlayerX = 370
PlayerY = 480

def player():
    screen.blit(Playerimg, (PlayerX, PlayerY))

#game loop
#while running loop
running = True
while running:
    #screen.fill ((R, G, B)) (Red, Green, Blue)
    #move this at top for player to fill in screen.
    #for space color, we would have to turn 255 into 0.
    screen.fill ((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player()
    pygame.display.update()