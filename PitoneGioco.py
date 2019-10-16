#============================================================================================
#MODULI
#============================================================================================
import pygame
import time

#============================================================================================
#VARIABILI
#============================================================================================
rosso = (255,0,0) #R, G, B
colore2 = (120,50,100)

background = pygame.image.load(r"sfondo.jpg")
background = pygame.transform.scale(background, (600,600))

# banana = pygame.image.load(r"banana.png")

black = (0,0,0)
white = (255,255,255)
frame = pygame.time.Clock()
fabbricaRaggiunta = False
casaRaggiunta = False
daDove = "casa"

#============================================================================================
#SPRITE E FANTA -----------------------------------------------------------------------------
#============================================================================================

class Sprite:
    """NUOVO SPRITE ASGARRA
    argomenti: x, y, velocità"""
    def __init__(self, x, y, larghezza, altezza, costume, livello = 0):
        self.x = x
        self.y = y
        self.costume = pygame.image.load(costume)
        self.altezza = altezza
        self.larghezza = larghezza
        self.sprite = pygame.transform.scale(self.costume, (larghezza, altezza))
        self.hitbox = (self.x, self.y, larghezza,altezza)
        # self.banana = pygame.draw.rect(screen, (255,0,0), self.hitbox,1)


        # self.sprite = self.sprite.get_rect()
        if livello >= 0:
            self.livello = livello
        else:
            self.livello = abs(livello) #trasformiamo in positivo
        


    def printaggio(self):
        print(self.x, self.y)
    def upgrade(self):
        self.livello += 1
    def downgrade(self):
        if self.livello: #controlla se livello non è 0
            self.livello -= 1 
    
    

class Veicolo(Sprite):
    def impostaVelocità(self, velocità=1):
        self.velocità = abs(velocità)
    def girati(self, orizzontale, verticale):
        self.sprite = pygame.transform.flip(self.sprite, orizzontale, verticale) #orizzontale, verticale
    


class Edificio(Sprite):
    def impostaCapienza(self, capienzaCasa=5):
        self.capienzaCasa = abs(capienzaCasa)
    



#==========================================================================================
# ISPANZE ---------------------------------------------------------------------------------
#==========================================================================================

Fabbrica = Edificio(50, 290, 120, 120, r"fabbrica.png")
Casa = Edificio(430, 290, 120, 120, r"casa_base.png")

Trasporto = Veicolo(360, 370, 70, 34, r"veicolo_base.png")
                                                 
#==========================================================================================
pygame.init() #inizializziamo pygame
pygame.display.set_caption("Fabbrica dei cani") #impostiamo il titolo ad ASGARRA


screen = pygame.display.set_mode((600,600)) #impostiamo le dimensioni della finestra

finished = False



while not finished:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT: #quando si preme la X
            finished = True           #chiudi

    # aggiungere gli sprite al gioco
    screen.blit(background, (0, 0))
    screen.blit(Trasporto.sprite, (Trasporto.x, Trasporto.y))
    screen.blit(Casa.sprite, (Casa.x, Casa.y))#aggiungiamo l'immagine allo schermo (x, y)
    screen.blit(Fabbrica.sprite, (Fabbrica.x, Fabbrica.y)) #aggiungiamo l'immagine allo schermo (x, y)


    pressedKeys = pygame.key.get_pressed()
        
    if pressedKeys[pygame.K_SPACE] == 1:
        if daDove == "casa":
            Trasporto.x -= 1
        if daDove == "fabbrica":
            Trasporto.x += 1
    if pressedKeys[pygame.K_g] == 1:
        Trasporto.sprite = pygame.transform.flip(Trasporto.sprite, True, False)
        time.sleep(0.1)
        
    
    # @todo fixare sta roba
    # print(fabbricaRaggiunta)
    # if Trasporto.x < Fabbrica.x + 100:
    #     fabbricaRaggiunta = True
    # else:
    #     fabbricaRaggiunta = False

    # if fabbricaRaggiunta:
        
    #     Trasporto.x += 20
    #     #pygame.display.flip()
    #     time.sleep(2)

        # daDove = "fabbrica"
        

    # if Trasporto.x < Casa.x:
    #     casaRaggiunta = True
    # else:
    #     casaRaggiunta = False

    # if casaRaggiunta: #cambia direzione
    #     time.sleep(2)
    #     Trasporto.x -= 20
    #     Trasporto.sprite = pygame.transform.flip(Trasporto.sprite, True, False)
    #     daDove = "casa"
        
        
        

    #muove le hitbox
    Trasporto.hitbox = (Trasporto.x, Trasporto.y, Trasporto.larghezza, Trasporto.altezza)
    Casa.hitbox = (Casa.x, Casa.y, Casa.larghezza, Casa.altezza)
    Fabbrica.hitbox = (Fabbrica.x, Fabbrica.y, Fabbrica.larghezza, Fabbrica.altezza)

    #disegna le hitbox
    
    bananaT = pygame.draw.rect(screen, (255,0,0), Trasporto.hitbox,1)
    bananaC = pygame.draw.rect(screen, (255,0,0), Casa.hitbox,1)
    bananaF = pygame.draw.rect(screen, (255,0,0), Fabbrica.hitbox,1)

    if bananaT.colliderect(bananaF):
        print("Asgarra")

    pygame.display.flip() #aggiorna lo schermo
    
    
    frame.tick(1000)