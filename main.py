import pygame
from pygame.display import update

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_w,
    K_a,
    K_s,
    K_d,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

class Player(pygame.sprite.Sprite):
    def __init__(self, up, left, right, down, color):
        super(Player, self).__init__()
        self.surf = pygame.Surface((50, 50))
        self.surf.fill(color)
        self.rect = self.surf.get_rect()
        self.up = up
        self.left = left
        self.right = right
        self.down = down

    def update(self, pressed_keys):
        if pressed_keys[self.up]:
            self.rect.move_ip(0, -5)
        if pressed_keys[self.down]:
            self.rect.move_ip(0, 5)
        if pressed_keys[self.left]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[self.right]:
            self.rect.move_ip(5, 0)

        # Check if player is in bounds
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

pygame.init()
pygame.display.set_caption('Cyberpunk 2088')

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

player1 = Player(K_w, K_a, K_d, K_s, (255, 87, 51))
player2 = Player(K_UP, K_LEFT, K_RIGHT, K_DOWN, (51, 164, 255))

running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == pygame.QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()
    player1.update(pressed_keys)
    player2.update(pressed_keys)

    screen.fill((255, 255, 255))
    screen.blit(player1.surf, player1.rect)
    screen.blit(player2.surf, player2.rect)

    pygame.display.flip()

pygame.quit()