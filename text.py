import pygame

pygame.init()

display_surface = pygame.display.set_mode((600, 600 ))

font = pygame.font.Font('Cascadia.ttf', 32)

text = font.render('FILVI BANANA ASGARRA', True, (255,255,255)) 
textRect = text.get_rect()

while True:

    for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()

    display_surface.blit(text, textRect)
    pygame.display.update()





