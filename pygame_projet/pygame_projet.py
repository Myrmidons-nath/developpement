import pygame #importation du module

pygame.init() # creation de la fenetre


pygame.display.set_mode((500, 500)) #dimention de la fenetre

jeu = True 
while jeu :
    for event in pygame.event.get(): # releve tout les evenements qui se deroules
        if event.type == pygame.QUIT: #si l'evenement est quit 
             jeu = False            # ferme la boucle 


pygame.quit() # fin boucle > quitte la fenetre