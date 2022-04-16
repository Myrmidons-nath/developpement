import pygame
from jeu import game
if __name__ == '__main__':
    pygame.init()
    game = game()
    game.run()

pygame.quit()