import sys
import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group
from random import randint

screen_width = 1400
screen_height = 800

class ADrop(Sprite):
    def __init__(self, screen):
        self.screen = screen
        super(ADrop, self).__init__()
        self.image = pygame.image.load('images/a-drop-of-299775_640_1.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.x = self.screen_rect.left
        self.rect.y = self.rect.top
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Raindrops")
    drops = Group()
    create_window(screen, drops)
    random_drop(screen, drops)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((70, 130, 180))
        run_drop(screen, drops)
        drops.draw(screen)
        for drop in drops.copy():
            if drop.rect.top > screen_height:
                drop.y = 0
                drop.rect.bottom = drop.y
        
        pygame.display.flip()

def create_window(screen, drops):
    a_drop = ADrop(screen)
    a_drop_width = a_drop.rect.width
    available_space_x = screen_width - 2 * a_drop_width
    number_drops_x = int(available_space_x / (7 * a_drop_width))
    number_rows = get_number_rows(screen, a_drop.rect.height)
    for row_number in range(number_rows):
        for a_drop_number in range(number_drops_x):
            a_drop = ADrop(screen)
            a_drop.x = a_drop_width + 8 * a_drop_width * a_drop_number
            a_drop.rect.x = a_drop.x
            a_drop.rect.y = (a_drop.rect.height
                            + 2 * a_drop.rect.height * row_number)
            drops.add(a_drop)

def get_number_rows(screen, a_drop_height):
    available_space_y = screen_height - a_drop_height
    number_rows = int(available_space_y / (2 * a_drop_height))
    return number_rows

def random_drop(screen, drops):
    """ Случайное смещешие капель по х."""
    for misaligned_a_drop in drops.sprites():
        misaligned_a_drop.x = misaligned_a_drop.rect.x + randint(-100, 100)
        misaligned_a_drop.rect.x = misaligned_a_drop.x
        misaligned_a_drop.y = misaligned_a_drop.rect.y + randint(-30, 30)
        misaligned_a_drop.rect.y = misaligned_a_drop.y 
        
def run_drop(screen, drops):
    """ Случайное смещешие капель по y."""
    for misaligned_a_drop in drops.sprites():
        misaligned_a_drop.y = misaligned_a_drop.rect.y + randint(0, 3)
        misaligned_a_drop.rect.y = misaligned_a_drop.y 

run_game()
