import pygame #importation du module

pygame.init() # creation de la fenetre


ecran = pygame.display.set_mode((1000, 800)) #dimention de la fenetre
image = pygame.image.load(r"C:\Users\Nathan\Documents\github\git\pygame_projet\image_bois.png").convert()
temps = pygame.time.Clock()
jeu = True 
x = 200
y = 400
while jeu :
    for event in pygame.event.get(): # releve tout les evenements qui se deroules
        if event.type == pygame.QUIT: #si l'evenement est quit 
             jeu = False              # ferme la boucle 


    keys = pygame.key.get_pressed()
        
    if keys[pygame.K_LEFT]:
        x-=1
    if keys[pygame.K_RIGHT]:
        x+=1
    if keys[pygame.K_UP]:
        y-=1
    if keys[pygame.K_DOWN]:
        y+=1
    



    ecran.fill((0, 0, 0))
    ecran.blit(image, (x, y))
    pygame.display.flip()
    temps.tick(800)

pygame.quit() # fin boucle > quitte la fenetre