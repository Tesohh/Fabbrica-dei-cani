#============================================================================================
#MODULI
#============================================================================================
import pygame
import time
import random

#============================================================================================
#PRELIMINARI
#============================================================================================
pygame.init() #inizializziamo pygame

pygame.display.set_caption("Fabbrica dei cani") #impostiamo il titolo ad ASGARRA

screen = pygame.display.set_mode((600,600)) #impostiamo le dimensioni della finestra

font = pygame.font.Font('Cascadia.ttf', 28)



#============================================================================================
#VARIABILI
#============================================================================================
rosso = (255,0,0) #R, G, B
colore2 = (120,50,100)

background = pygame.image.load(r"prova sfondo 1.png")
background = pygame.transform.scale(background, (600,600))


# banana = pygame.image.load(r"banana.png")

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0, 255, 0)

frame = pygame.time.Clock()
fabbricaRaggiunta = False
casaRaggiunta = False
daDove = "casa"
tutorialSlide = 0
caniInCasa = 2
producendo = "Fermo"
giocoIniziato = False
caniTrasportati = False
quantitaTrasporto = 0
numeroRandom = 0


#============================================================================================
#funzioni
#============================================================================================
def blittaTutto():
    #hitbox
    hitboxT = pygame.draw.rect(screen, (255,0,0), Trasporto.hitbox,1)
    hitboxC = pygame.draw.rect(screen, (255,0,0), Casa.hitbox,1)
    hitboxF = pygame.draw.rect(screen, (255,0,0), Fabbrica.hitbox,1)

    #testo: cambia il contenuto e il colore
    testoTutorial = font.render(TestoTutorial.string, True, TestoTutorial.color) 
    testoTutorialRect = testoTutorial.get_rect()
    testoCasa = font.render(str(caniInCasa), True, TestoCasa.color) 
    testoFabbrica = font.render(str(producendo), True, TestoFabbrica.color) 
    testoTrasporto = font.render(TestoTrasporto.string, True, TestoTrasporto.color)

    #testo: aggiungi allo schermo
    screen.blit(testoTutorial, testoTutorialRect)
    screen.blit(testoCasa, (TestoCasa.x,TestoCasa.y))
    screen.blit(testoFabbrica, (TestoFabbrica.x,TestoFabbrica.y))
    screen.blit(testoTrasporto, (TestoTrasporto.x,TestoTrasporto.y))

    #refresh
    pygame.display.flip()

def blitBox(who):
    """BLITTA UNA HITBOX"""
    if who == "camion":
        hitboxT = pygame.draw.rect(screen, (255,0,0), Trasporto.hitbox,1)
        
    elif who == "casa":
        hitboxC = pygame.draw.rect(screen, (255,0,0), Casa.hitbox,1)
        
    elif who == "fabbrica":
        hitboxF = pygame.draw.rect(screen, (255,0,0), Fabbrica.hitbox,1)

def moveBox(who):
    """MUOVI UNA HITBOX"""
    if who == "camion":
        Trasporto.hitbox = (Trasporto.x, Trasporto.y, Trasporto.larghezza, Trasporto.altezza)
        
    elif who == "casa":
        Casa.hitbox = (Casa.x, Casa.y, Casa.larghezza, Casa.altezza)
        
    elif who == "fabbrica":
        Fabbrica.hitbox = (Fabbrica.x, Fabbrica.y, Fabbrica.larghezza, Fabbrica.altezza)
        
        
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
        

    def blittaggio(self):
        screen.blit(self.sprite, (self.x,self.y))

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

class Text:
    """CLASSE PER CREARE DEL TESTOH"""
    def __init__(self, x, y, size, color, string):
        

        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.string = str(string)
        self.testoh = font.render(self.string, True, self.color)
    def blitText(self):
        screen.blit(self.testoh, (self.x,self.y))

        


    



#==========================================================================================
# ISPANZE ---------------------------------------------------------------------------------
#==========================================================================================

Fabbrica = Edificio(50, 290, 120, 120, r"fabbrica.png")
Casa = Edificio(430, 290, 120, 120, r"casa_base.png")

Trasporto = Veicolo(360, 370, 70, 34, r"veicolo_base.png")


TestoTutorial = Text(0,0,32,black,"Benvenuto! Premi K per continuare")
TestoCasa = Text(480,410,32,black,"")
TestoFabbrica = Text(70,410,32,red,"")
TestoTrasporto = Text(Trasporto.x,Trasporto.y-10,32,green,"")
                                                 
#==========================================================================================



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

    testoTutorial = font.render(TestoTutorial.string, True, TestoTutorial.color) 
    testoTutorialRect = testoTutorial.get_rect()
    testoCasa = font.render(str(caniInCasa), True, TestoCasa.color) 
    testoFabbrica = font.render(str(producendo), True, TestoFabbrica.color) 
    testoTrasporto = font.render(TestoTrasporto.string, True, TestoTrasporto.color) 
    

    pressedKeys = pygame.key.get_pressed()
        
    if pressedKeys[pygame.K_SPACE] == 1:
        if giocoIniziato:
            if not caniTrasportati:
                if daDove == "casa":
                    TestoTrasporto.string = "..."
                    blittaTutto()
                    time.sleep(1)
                    quantitaTrasporto = 2
                    TestoTrasporto.string = str(quantitaTrasporto)
                    caniTrasportati = True
                    caniInCasa -= 2
                if daDove == "fabbrica":
                    TestoTrasporto.string = "..."
                    TestoFabbrica.color = green
                    producendo = " ..."
                    blittaTutto()
                    time.sleep(3) #@todo fixare che la pausa non fa cambiare i testi
                    TestoFabbrica.color = red
                    producendo = "Fermo"
                    caniTrasportati = True
                    numeroRandom = random.randint(1,3)
                    quantitaTrasporto += 2+numeroRandom
                    TestoTrasporto.string = str(quantitaTrasporto)

            if daDove == "casa":
                Trasporto.x -= 1
            if daDove == "fabbrica":
                Trasporto.x += 1
    #tutorial
    if pressedKeys[pygame.K_k] == 1:
        if tutorialSlide != 7:
            print("prossimo")
            tutorialSlide += 1
            time.sleep(0.3)
            if tutorialSlide == 1:
                TestoTutorial.string = "In questo gioco dovrai ottenere"
            if tutorialSlide == 2:
                TestoTutorial.string = "100 cani di cui 5 perfetti,"
            if tutorialSlide == 3:
                TestoTutorial.string = "quindi con tutti gli stat"
            if tutorialSlide == 4:
                TestoTutorial.string = "maggiori di 8."
            if tutorialSlide == 5:
                TestoTutorial.string = "Iniziamo!!!"
            if tutorialSlide == 6:
                TestoCasa.string = "2"
                TestoTutorial.string = "Adesso hai due cani."
            if tutorialSlide == 7:
                TestoTutorial.string = "Portali alla fabbrica con [SPAZIO]" 
                giocoIniziato = True  
    if pressedKeys[pygame.K_p] == 1:
        if tutorialSlide != 7:
            tutorialSlide = 6
            print("Premi K per completare il saltamento")
            time.sleep(0.1)
        
        
        
    #disegna le hitbox
    blitBox("camion")
    blitBox("casa")
    blitBox("fabbrica")
    
    
    # hitboxT = pygame.draw.rect(screen, (255,0,0), Trasporto.hitbox,1)
    # hitboxC = pygame.draw.rect(screen, (255,0,0), Casa.hitbox,1)
    # hitboxF = pygame.draw.rect(screen, (255,0,0), Fabbrica.hitbox,1)

    # #disegna il testo
    # screen.blit(testoTutorial, testoTutorialRect)
    # screen.blit(testoCasa, (TestoCasa.x,TestoCasa.y))
    # screen.blit(testoFabbrica, (TestoFabbrica.x,TestoFabbrica.y))
    # screen.blit(testoTrasporto, (TestoTrasporto.x,TestoTrasporto.y))

    #muove le hitbox
    moveBox("trasporto")
    moveBox("casa")
    moveBox("fabbrica")

    #muovi il testo del veicol
    TestoTrasporto.x = Trasporto.x
    TestoTrasporto.y = Trasporto.y - 30



    if hitboxT.colliderect(hitboxF):
        print("Asgarraa FABBRICA")
        daDove = "fabbrica"
        Trasporto.sprite = pygame.transform.flip(Trasporto.sprite, True, False)
        Trasporto.x += 2
        caniTrasportati = False

    if hitboxT.colliderect(hitboxC):
        print("Asgarraa CASA")
        daDove = "casa"
        Trasporto.sprite = pygame.transform.flip(Trasporto.sprite, True, False)
        Trasporto.x -= 2
    pygame.display.flip() #aggiorna lo schermo
    
    
    frame.tick(1000)

