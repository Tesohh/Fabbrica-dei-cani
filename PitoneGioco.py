#============================================================================================
#MODULI
#============================================================================================
import pygame
import time
import random
import pandas
import random
from genera_nome_cane import generaNome

#============================================================================================
#PRELIMINARI
#============================================================================================
pygame.init() #inizializziamo pygame

musica = pygame.mixer.music.load(r"Suoni\/flauteggiamento.wav")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

icona = pygame.image.load(r"Immagini\/icona.ico")

pygame.display.set_caption("Fabbrica dei cani") #impostiamo il titolo ad ASGARRA
pygame.display.set_icon(icona)

screen = pygame.display.set_mode((600,600)) #impostiamo le dimensioni della finestra

font = pygame.font.Font(r"Font\/Cascadia.ttf", 28)



#============================================================================================
#VARIABILI
#============================================================================================
rosso = (255,0,0) #R, G, B
colore2 = (120,50,100)

background = pygame.image.load(r"Immagini\/prova sfondo 1.png")
background = pygame.transform.scale(background, (600,600))

        



# banana = pygame.image.load(r"banana.png")

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0, 255, 0)
orange = (255,165,0)

frame = pygame.time.Clock()
fabbricaRaggiunta = False
casaRaggiunta = False
daDove = "casa"
tutorialSlide = 0
caniInCasa = 0
giocoIniziato = False
caniTrasportati = False
quantitaTrasporto = 2
numeroRandom = 0
starting = False


woof = pygame.mixer.Sound(r"Suoni\/woof.wav")
microWoof = pygame.mixer.Sound(r"Suoni\/woofHigh.wav")
camionStart = pygame.mixer.Sound(r"Suoni\/camionStart.wav")
camionGo = pygame.mixer.Sound(r"Suoni\/camion.wav")

pygame.mixer.Sound.set_volume(camionStart, 0.2)

#============================================================================================
#funzioni
#============================================================================================


def blitBox(who):
    """BLITTA UNA HITBOX"""
    if who == "camion":
        hitboxT = pygame.draw.rect(screen, (255,0,0), Trasporto.hitbox,1)
        return hitboxT
        
    elif who == "casa":
        hitboxC = pygame.draw.rect(screen, (255,0,0), Casa.hitbox,1)
        return hitboxC
        
    elif who == "fabbrica":
        hitboxF = pygame.draw.rect(screen, (255,0,0), Fabbrica.hitbox,1)
        return hitboxF

def mostraTutorial(boolean):
    """ Valori accettati (0,1) """
    global tutorialSlide, giocoIniziato
    if boolean:
        if pressedKeys[pygame.K_k] == 1:
            if tutorialSlide != 7:
                print("prossimo")
                tutorialSlide += 1
                time.sleep(0.3)
                # cambia il testo del tutorial
                if tutorialSlide == 1:
                    TestoTutorial.string = "In questo gioco dovrai ottenere"
                elif tutorialSlide == 2:
                    TestoTutorial.string = "100 cani di cui 5 perfetti,"
                elif tutorialSlide == 3:
                    TestoTutorial.string = "quindi con tutti gli stat"
                elif tutorialSlide == 4:
                    TestoTutorial.string = "maggiori di 8."
                elif tutorialSlide == 5:
                    TestoTutorial.string = "Iniziamo!!!"
                elif tutorialSlide == 6:
                    TestoCasa.string = "2"
                    TestoTutorial.string = "Adesso hai due cani."
                elif tutorialSlide == 7:
                    TestoTutorial.string = "Portali alla fabbrica con [SPAZIO]" 
                    giocoIniziato = True  
        if pressedKeys[pygame.K_p] == 1:
            if tutorialSlide != 7:
                tutorialSlide = 6
                print("Premi K per completare il saltamento")
                time.sleep(0.1)  
    else:
        giocoIniziato = True
    return giocoIniziato


#============================================================================================
#SPRITE E FANTA -----------------------------------------------------------------------------
#============================================================================================

class Sprite:
    """NUOVO SPRITE ASGARRA
    argomenti: x, y, larghezza, altezza, costume, livello = 0"""

    def __init__(self, x, y, larghezza, altezza, costume, livello = 0):
        self.x = x
        self.y = y
        self.costume = pygame.image.load(costume)
        self.altezza = altezza
        self.larghezza = larghezza
        self.sprite = pygame.transform.scale(self.costume, (larghezza, altezza))
        self.hitbox = (self.x, self.y, larghezza,altezza)
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
        
    def blitText(self):
        self.testoh = font.render(self.string, True, self.color)
        screen.blit(self.testoh, (self.x,self.y))

class Rectangle:
    def __init__(self, x,y,larghezza,altezza,color):
        self.x = x
        self.y = y
        self.larghezza = larghezza
        self.altezza = altezza
        self.color = color
        self.rect = pygame.Rect(self.x,self.y,self.larghezza,self.altezza)

    def blittaggio(self):
        self.drawRect = pygame.draw.rect(screen, self.color, self.rect)



class Cane:
    """ CLASSE PER FARE UN NUOVO CANE"""
    def __init__(self, qualita):
        self.speed = random.randint(1,10) + qualita

        if self.speed > 10:
            self.speed = 10

        self.furriness = random.randint(1,10) + qualita

        if self.furriness > 10:
            self.furriness = 10
        
        self.barkiness = random.randint(1,10)+ qualita

        if self.barkiness > 10:
            self.barkiness = 10

        self.awwness = random.randint(1,10)+ qualita

        if self.awwness > 10:
            self.awwness = 10


        if self.speed >= 8 and self.furriness >= 8 and self.furriness >= 8 and self.awwness >= 8:
            self.perfect = True
            self.name = input("Complimenti! Hai trovato un cane perfetto. Che nome vuoi dargli?\n")
            print("Wow! Bel nome!!!!\n")
        else:
            self.perfect = False
            self.name = generaNome()
        
        self.age = 0



    



#==========================================================================================
# ISPANZE ---------------------------------------------------------------------------------
#==========================================================================================

Fabbrica = Edificio(50, 290, 120, 120, r"Immagini\/fabbrica.png")
Casa = Edificio(430, 290, 120, 120, r"Immagini\/casa_base.png")

Trasporto = Veicolo(360, 370, 70, 34, r"Immagini\/veicolo_base.png")


TestoTutorial = Text(0,0,32,black,"Benvenuto! Premi K per continuare")
TestoCasa = Text(480,410,32,black,"")
TestoFabbrica = Text(70,410,32,red,"Fermo")
TestoTrasporto = Text(Trasporto.x,Trasporto.y-10,32,green,"")
CopriTestoF = Rectangle(48, 408, 122, 35, white)
                                                 
#==========================================================================================


finished = False



while not finished:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT: #quando si preme la X
            finished = True           #chiudi

    # hitbox
    hitboxCamion = blitBox("camion")
    hitboxCasa = blitBox("casa")
    hitboxFabbrica = blitBox("fabbrica")



    # aggiungere gli sprite al gioco
    screen.blit(background, (0, 0))
    Fabbrica.blittaggio()
    Casa.blittaggio()
    Trasporto.blittaggio()
    

    # screen.blit(Trasporto.sprite, (Trasporto.x, Trasporto.y))
    # screen.blit(Casa.sprite, (Casa.x, Casa.y))#aggiungiamo l'immagine allo schermo (x, y)
    # screen.blit(Fabbrica.sprite, (Fabbrica.x, Fabbrica.y)) #aggiungiamo l'immagine allo schermo (x, y)

    pressedKeys = pygame.key.get_pressed()

    # decidi se mostrare o no il tutorial bool 0 / 1
    mostraTutorial(0)
    
    
    

    #tiene testocasa.string sempre alla quantita dei cani
    TestoCasa.string = str(caniInCasa)
    
    
    TestoTrasporto.blitText()
    TestoFabbrica.blitText()
    TestoCasa.blitText()
    TestoTutorial.blitText()

    

    if pressedKeys[pygame.K_SPACE] == 1:


            if starting == False:
                pygame.mixer.Sound.play(camionStart) 
                starting = True


            if daDove == "casa":
                Trasporto.x -= 1


                # cambia il testo del trasporto
                TestoTrasporto.string = str(quantitaTrasporto)

                #se la hitbox del camion tocca quello della fabbrica
                if hitboxCamion.colliderect(hitboxFabbrica): 
                    TestoFabbrica.color = orange
                    TestoFabbrica.string = " ..."
                    CopriTestoF.blittaggio()
                    TestoFabbrica.blitText()
                    TestoCasa.blitText()
                    TestoTrasporto.blitText()
                    pygame.display.flip()
                    pygame.mixer.Sound.play(woof)


                    Trasporto.x += 2
                    
                    time.sleep(3)
                    TestoFabbrica.color = green
                    TestoFabbrica.string = "Fatto!"
                    daDove = "fabbrica"

                    #gira il camion
                    Trasporto.sprite = pygame.transform.flip(Trasporto.sprite, True, False) 
                    caniTrasportati = False
                    #pygame.mixer.Sound.play(woof)
                    
                    pygame.mixer.Sound.play(microWoof)

                    

                    caniTrasportati = True
                    
                    # crea un numero random, assegnalo a quantita trasporto e cambia il testo di TestoTRasporto
                    numeroRandom = random.randint(1,3)
                    quantitaTrasporto += 2 + numeroRandom
                    TestoTrasporto.string = str(quantitaTrasporto)

                

            
            # se sto arrivando dalla fabbrica
            elif daDove == "fabbrica":
                Trasporto.x += 1
                
                if not hitboxCamion.colliderect(hitboxCasa) and not hitboxCamion.colliderect(hitboxCasa):
                    TestoFabbrica.string = "Fermo"
                    TestoFabbrica.color = red 
                    

                #se la hitbox del camion tocca quello della casa
                if hitboxCamion.colliderect(hitboxCasa):
                    daDove = "casa"

                    #gira il camion
                    Trasporto.sprite = pygame.transform.flip(Trasporto.sprite, True, False)
                    Trasporto.x -= 2


                    
                    time.sleep(1)
                    caniTrasportati = True

                    caniInCasa += quantitaTrasporto - 2
                    quantitaTrasporto = 2
                    TestoTrasporto.string = str(quantitaTrasporto)
                    

             

                

    
    pygame.display.flip()

    #muove la hitbox del camion
    Trasporto.hitbox = (Trasporto.x, Trasporto.y, Trasporto.larghezza, Trasporto.altezza)
    
    #muovi il testo del veicol
    TestoTrasporto.x = Trasporto.x
    TestoTrasporto.y = Trasporto.y - 30

    pygame.display.flip() #aggiorna lo schermo
    
    frame.tick(1000)