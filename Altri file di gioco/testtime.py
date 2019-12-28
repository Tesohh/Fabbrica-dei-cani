import time
import pygame 


finished = False
PRINTAGGIO = 1

millis = 2000


pygame.init()



clocc = clock.tick(1)

while True:
    
    while not finished:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT: #quando si preme la X
                finished = True           #chiudi
            if event.type == PRINTAGGIO:
                print("tesohh")
                millis = 0
    if clocc == 1:
        print("tesohh")
