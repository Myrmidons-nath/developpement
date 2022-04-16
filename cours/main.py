import pygame #importation du module 

pygame.init()
fenetre = pygame.display.set_mode((400, 400))

jeu = True
while jeu==True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            jeu = False
        
    keys = pygame.key.get_pressed()
        
    if keys[pygame.K_LEFT]:
        print("gauche")
    if keys[pygame.K_RIGHT]:
        print("droite")
    if keys[pygame.K_UP]:
        print("haut")
    if keys[pygame.K_DOWN]:
        print("bas")

