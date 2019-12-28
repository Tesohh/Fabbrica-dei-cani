import pygame
pygame.init()

caratteri = "abcdefghijklmnopqrstuvwxyz1234567890"

display = pygame.display.set_mode((600,600))


font = pygame.font.Font(r"Font\/noto.ttf", 32)
string = ""
text = font.render(string, False, (255,255,255))


def aggiungiCarattere(char):
    global string
    if char in caratteri:
        string += char
def update():
    text = font.render(string, False, (255,255,255))


running = True
while running == True:
    display.fill([0, 0, 0])
    display.blit(text,(0,0))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            aggiungiCarattere(pygame.key.name(event.key))
            update()
            if event.key == pygame.K_BACKSPACE:
                string = string[:-1]
            if event.key == pygame.K_RETURN:
                if len(string)>0:
                    print(string)
                    running = False
                else:
                    print("Un nome devi ben averlo! Tu hai detto che ti chiami:   ")
        


    
    