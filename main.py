# Simple pygame program

# Import and initialize the pygame library
import pygame
import random
from config import *
from pygame.locals import (
    RLEACCEL,
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
map_image = pygame.image.load('assets/Evf3l3tWgAQ1k41.png')
map_rect = map_image.get_rect()


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20,10))
        self.surf.fill((255,220,220))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(1,3)
        
    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


# defines player object by extending pygame.sprite.Sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        # Loading player image
        self.surf = pygame.image.load("assets/attack4_1.png").convert()
        self.rect = self.surf.get_rect()


    def update(self, pressed_keys):
        if pressed_keys[K_w]:
            self.rect.move_ip(0,-2)
        if pressed_keys[K_a]:
            self.rect.move_ip(-2,0)
        if pressed_keys[K_s]:
            self.rect.move_ip(0,2)
        if pressed_keys[K_d]:
            self.rect.move_ip(2,0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

player = Player()

enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

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

        # if window is exited
        elif event.type == pygame.QUIT:
            running = False


        elif event.type == ADDENEMY:
            # create new enemy and assign sprite group
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)


    screen.blit(map_image, (MAP_X,MAP_Y))

    # gets all the keys pressed in this frame
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    enemies.update()

    #blit surface
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)


    # check if player collided with any enemies, if so, player dies
    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()
        running = False

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()