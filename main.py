import pygame
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
)
import math

class Player(pygame.sprite.Sprite):
    def __init__(self, up, left, right, down, color):
        super(Player, self).__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect()

        self.up = up
        self.left = left
        self.right = right
        self.down = down

        self.speed = 8

    def update(self, pressed_keys):
        if pressed_keys[self.up]:
            self.rect.move_ip(0, -self.speed)
        if pressed_keys[self.down]:
            self.rect.move_ip(0, self.speed)
        if pressed_keys[self.left]:
            self.rect.move_ip(-self.speed, 0)
        if pressed_keys[self.right]:
            self.rect.move_ip(self.speed, 0)

        # Check if player is in bounds
        if self.rect.left < play_rect.left + 3:
            self.rect.left = play_rect.left + 3
        if self.rect.right > play_rect.right - 3:
            self.rect.right = play_rect.right - 3
        if self.rect.top <= play_rect.top + 3:
            self.rect.top = play_rect.top + 3
        if self.rect.bottom >= play_rect.bottom - 3:
            self.rect.bottom = play_rect.bottom - 3

    def rotate(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.rect.left, mouse_y - self.rect.top
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        self.image = pygame.transform.rotate(self.image, int(angle))
        self.rect = self.image.get_rect()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

clock = pygame.time.Clock()
pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

play_area = pygame.Surface((1024, 576))
play_area.set_alpha(128)
play_rect = play_area.get_rect()
play_rect.x = (SCREEN_WIDTH-play_area.get_width())/2
play_rect.y = 100

play_border = play_rect.copy()

player1 = Player(K_w, K_a, K_d, K_s, (255, 87, 51))
player1.rect.x = play_rect.left + 25
player1.rect.y = play_rect.top + (play_area.get_height()-player1.image.get_height())/2

player2 = Player(K_UP, K_LEFT, K_RIGHT, K_DOWN, (51, 164, 255))
player2.rect.x = play_rect.right - player2.image.get_width() - 25
player2.rect.y = play_rect.top + (play_area.get_height()-player2.image.get_height())/2

player_list = pygame.sprite.Group()
player_list.add(player1, player2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEMOTION:
            player1.rotate()

    pressed_keys = pygame.key.get_pressed()
    player1.update(pressed_keys)
    player2.update(pressed_keys)

    screen.fill((218, 209, 170))
    screen.blit(play_area, ((SCREEN_WIDTH-play_area.get_width())/2, 100))
    play_area.fill((140, 139, 139))
    pygame.draw.rect(screen, (96, 95, 93), play_border, 5)
    player_list.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()