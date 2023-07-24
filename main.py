# Simple pygame program

# Import and initialize the pygame library
import pygame
from config import *
from pygame.locals import (
    K_w,
    K_a,
    K_s,
    K_d,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75,25))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()
    def update(self, pressed_keys):
        if pressed_keys[K_w]:
            self.rect.move_ip(0,-5)
        if pressed_keys[K_a]:
            self.rect.move_ip(0,5)
        if pressed_keys[K_s]:
            self.rect.move_ip(-5,0)
        if pressed_keys[K_d]:
            self.rect.move_ip(5,0)

player = Player()
# Run until the user asks to quit
running = True

# event handler
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        
        # if escape is pressed close game
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
                        
        elif event.type == pygame.QUIT:
            running = False

    # gets all the keys pressed in this frame
    pressed_keys = pygame.key.get_pressed()

    player.update(pressed_keys)
    # Fill the background with black
    screen.fill((0,0,0))


    #blit surface
    screen.blit(player.surf, player.rect)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()