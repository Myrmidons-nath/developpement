import pygame

class game:
    def __init__(self):
        pygame.display.set_caption("jeu bois")
        self.ecran = pygame.display.set_mode((1000, 1000))
        self.image = pygame.image.load(r"C:\Users\Nathan\Documents\github\git\pygame_projet\image_bois.png").convert()

        self.temps = pygame.time.Clock()
        self.x = 200
        self.y = 200
        self.boucle = True
    def run(self):
        while self.boucle:
            for event in pygame.event.get(): # releve tout les evenements qui se deroules
                if event.type == pygame.QUIT: #si l'evenement est quit 
                    self.boucle = False              # ferme la boucle 
            
            
            self.ecran.fill((0, 0, 0))
            self.ecran.blit(self.image, (200, 200))
            pygame.display.flip()
            