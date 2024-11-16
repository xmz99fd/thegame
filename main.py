# Import the pygame module

import pygame
import random

# Import pygame.locals for easier access to key coordinates

# Updated to conform to flake8 and black standards

from pygame.locals import(

    RLEACCEL,
   
    K_UP,

    K_DOWN,

    K_LEFT,

    K_RIGHT,

    K_ESCAPE,

    KEYDOWN,

    QUIT,
)


# Define constants for the screen width and height

SCREEN_WIDTH = 1920

SCREEN_HEIGHT = 1080

# Initialize pygame
pygame.init()

# Create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Setup for sounds (optional, defaults are good)
pygame.mixer.init()

# Initialize font for the scoreboard
pygame.font.init()
font = pygame.font.Font(None, 74)

# Define a player object by extending pygame.sprite.Sprite

# Define the enemy object by extending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'enemy'


    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
            


# The surface drawn on the screen is now an attribute of 'player'

class Player(pygame.sprite.Sprite):

    def __init__(self):

        super(Player, self).__init__()

        self.surf = pygame.image.load("smallball.png").convert()

        self.surf.set_colorkey((255, 255, 255), RLEACCEL)

        self.rect = self.surf.get_rect()



    # Move the sprite based on user keypresses

    def update(self, pressed_keys):

        if pressed_keys[K_UP]:

            self.rect.move_ip(0, -15)

        if pressed_keys[K_DOWN]:

            self.rect.move_ip(0, 15)

        if pressed_keys[K_LEFT]:

            self.rect.move_ip(-15, 0)

        if pressed_keys[K_RIGHT]:

            self.rect.move_ip(15, 0)


        # Keep player on the screen

        if self.rect.left < 0:

            self.rect.left = 0

        if self.rect.right > SCREEN_WIDTH:

            self.rect.right = SCREEN_WIDTH

        if self.rect.top <= 0:

            self.rect.top = 0

        if self.rect.bottom >= SCREEN_HEIGHT:

            self.rect.bottom = SCREEN_HEIGHT

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("better.png"  ).convert_alpha()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 2, SCREEN_WIDTH + 2),
                random.randint(0, SCREEN_HEIGHT),
                )
            )   
        self.speed = random.randint(10, 40)


    # Move the sprite based on speed

    # Remove the sprite when it passes the left edge of the screen

    def update(self):

        self.rect.move_ip(-self.speed, 0)

        if self.rect.right < 0:

            self.kill()



# Initialize pygame

pygame.init()


# Create the screen object

# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Create a custom event for adding a new enemy

ADDENEMY = pygame.USEREVENT + 1

pygame.time.set_timer(ADDENEMY, 250)


# Instantiate player. Right now, this is just a rectangle.

player = Player()

# Create groups to hold enemy sprites and all sprites

# - enemies is used for collision detection and position updates

# - all_sprites is used for rendering

enemies = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()

all_sprites.add(player)

bg = pygame.image.load("pitch.png").convert()

# Variable to keep the main loop running

running = True

start_time = pygame.time.get_ticks()

# Setup for sounds. Defaults are good.

pygame.mixer.init()

# Setup the clock for a decent framerate
clock = pygame.time.Clock()
time = 0

# Main loop

while running:

    time = time +1

    # for loop through the event queue

    for event in pygame.event.get():

        # Check for KEYDOWN event

        if event.type == KEYDOWN:

            # If the Esc key is pressed, then exit the main loop

            if event.key == K_ESCAPE:

                running = False

        # Check for QUIT event. If QUIT, then set running to false.

        elif event.type == QUIT:

            running = False


        # Add a new enemy?

        elif event.type == ADDENEMY:

            # Create the new enemy and add it to sprite groups

            new_enemy = Enemy()

            enemies.add(new_enemy)

            all_sprites.add(new_enemy)

    screen.blit(bg, (0,0))

    # Update the player sprite based on user keypresses
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

# Update enemy position

    enemies.update()



    # Draw the player on the screen
    screen.blit(player.surf, player.rect)

    # Draw all sprites

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

# Check if any enemies have collided with the player

    if pygame.sprite.spritecollideany(player, enemies):

    # If so, then remove the player and stop the loop

        player.kill()

        running = False

    elapsed_time_sec = time//60

    score_text = font.render(f"Time: {elapsed_time_sec} s", True, (255, 255, 255))  # White color
    
    screen.blit(score_text, (10, 10))
    pygame.display.flip()
    # Ensure program maintains a rate of 30 frames per second

    clock.tick(60)


print(elapsed_time_sec)

