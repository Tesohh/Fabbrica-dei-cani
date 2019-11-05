#============================================================================================
#MODULI
#============================================================================================
import pygame
import time
import random
import pandas
import random
from genera_nome_cane import generaNome
from tkinter import filedialog
from tkinter import Tk
import pickle
import os.path




#============================================================================================
#PRELIMINARI
#============================================================================================
pygame.init() #inizializziamo pygame

musica = pygame.mixer.music.load(r"Suoni\/flauteggiamento.wav")
pygame.mixer.music.set_volume(0.1)


icona = pygame.image.load(r"Immagini\/icona.ico")

pygame.display.set_caption("Fabbrica dei cani") #impostiamo il titolo ad ASGARRA
pygame.display.set_icon(icona)

screen = pygame.display.set_mode((600,600)) #impostiamo le dimensioni della finestra

font = pygame.font.Font(r"Font\/noto.ttf", 28)




#============================================================================================
#VARIABILI
#============================================================================================
rosso = (255,0,0) #R, G, B
colore2 = (120,50,100)

background = pygame.image.load(r"Loghi\/splashscreen.png")
background = pygame.transform.scale(background, (600,600))


jimmy = pygame.image.load(r"Immagini\/jimmyneutron.png")
easteregg = pygame.image.load(r"Immagini\/easteregg.png")


casa_1 = pygame.image.load(r"Immagini\/casa_1.png")
casa_2 = pygame.image.load(r"Immagini\/casa_2.png")
casa_3 = pygame.image.load(r"Immagini\/casa_3.png")
casa_4 = pygame.image.load(r"Immagini\/casa_4.png")
casa_5 = pygame.image.load(r"Immagini\/casa_5.png")

casa_upgrade_1 = pygame.image.load(r"Immagini\/casa_upgrade_1.png") 
casa_upgrade_2 = pygame.image.load(r"Immagini\/casa_upgrade_2.png") 
casa_upgrade_3 = pygame.image.load(r"Immagini\/casa_upgrade_3.png") 
casa_upgrade_4 = pygame.image.load(r"Immagini\/casa_upgrade_4.png") 
casa_upgrade_5 = pygame.image.load(r"Immagini\/casa_upgrade_5.png") 
casa_upgrade_max = pygame.image.load(r"Immagini\/casa_upgrade_max.png") 

camion_1 = pygame.image.load(r"Immagini\/camion_1.png")
camion_2 = pygame.image.load(r"Immagini\/camion_2.png")
camion_3 = pygame.image.load(r"Immagini\/camion_3.png")
camion_4 = pygame.image.load(r"Immagini\/camion_4.png")
camion_5 = pygame.image.load(r"Immagini\/camion_5.png")

camion_upgrade_1 = pygame.image.load(r"Immagini\/camion_upgrade_1.png") 
camion_upgrade_2 = pygame.image.load(r"Immagini\/camion_upgrade_2.png") 
camion_upgrade_3 = pygame.image.load(r"Immagini\/camion_upgrade_3.png") 
camion_upgrade_4 = pygame.image.load(r"Immagini\/camion_upgrade_4.png") 
camion_upgrade_5 = pygame.image.load(r"Immagini\/camion_upgrade_5.png") 
camion_upgrade_max = pygame.image.load(r"Immagini\/camion_upgrade_max.png") 

fabbrica_1 = pygame.image.load(r"Immagini\/fabbrica_1.png")
fabbrica_2 = pygame.image.load(r"Immagini\/fabbrica_2.png")
fabbrica_3 = pygame.image.load(r"Immagini\/fabbrica_3.png")
fabbrica_4 = pygame.image.load(r"Immagini\/fabbrica_4.png")
fabbrica_5 = pygame.image.load(r"Immagini\/fabbrica_5.png")

fabbrica_upgrade_1 = pygame.image.load(r"Immagini\/fabbrica_upgrade_1.png") 
fabbrica_upgrade_2 = pygame.image.load(r"Immagini\/fabbrica_upgrade_2.png") 
fabbrica_upgrade_3 = pygame.image.load(r"Immagini\/fabbrica_upgrade_3.png") 
fabbrica_upgrade_4 = pygame.image.load(r"Immagini\/fabbrica_upgrade_4.png") 
fabbrica_upgrade_5 = pygame.image.load(r"Immagini\/fabbrica_upgrade_5.png") 
fabbrica_upgrade_max = pygame.image.load(r"Immagini\/fabbrica_upgrade_max.png") 



# banana = pygame.image.load(r"banana.png")

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0, 255, 0)
orange = (255,165,0)
yellow = (255,255,0)

frame = pygame.time.Clock()
staScrivendo = True
fabbricaRaggiunta = False
casaRaggiunta = False
daDove = "casa"
tutorialSlide = 0
caniInCasa = 0
giocoIniziato = False
tutorialFinito = False  
caniTrasportati = False
quantitaTrasporto = 2
numeroRandom = 0
starting = True
primaVolta = True
schei = 1
dogOverflow = 0
possibilitaDiScrivere = False
nome = ""
path = r"Immagini\/profilo.png"

caratteri = "abcdefghijklmnopqrstuvwxyz1234567890"
scrivendoNome = True

woof = pygame.mixer.Sound(r"Suoni\/woof.wav")
microWoof = pygame.mixer.Sound(r"Suoni\/woofHigh.wav")
camionStart = pygame.mixer.Sound(r"Suoni\/camionStart.wav")
camionGo = pygame.mixer.Sound(r"Suoni\/camion.wav")
success = pygame.mixer.Sound(r"Suoni\/success.wav")
error = pygame.mixer.Sound(r"Suoni\/error.wav")

pygame.mixer.Sound.set_volume(camionStart, 0.2)
pygame.mixer.Sound.set_volume(success, 0.4)
pygame.mixer.Sound.set_volume(error, 5)


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
        
def tooManyDogs(overflow):
    global dogOverflow,caniInCasa,quantitaTrasporto

    TestoCasa.color = red
    dogOverflow = caniInCasa - overflow
    print(dogOverflow)
    caniInCasa = overflow
    quantitaTrasporto += dogOverflow
    TestoTrasporto.string = str(quantitaTrasporto)

    
        


def mostraProfilo():
    global primaVolta, schei, finished, nome, Casa, Fabbrica, Trasporto

    if TestoNome.string == "filviegg":
        Profilo.costume = easteregg 
        Profilo.cambiaCostume()
        TestoSchei.string = f"{schei}      flex"
    if TestoNome.string == "filvieggbanana":
        schei += 1
    if TestoNome.string == "filvieggbananaasgarra":
        schei += 1000000000000000000000000000000000000
        TestoSchei.string = "           INFINITI"
    if TestoNome.string == "crash":
        TestoNome.string = "Crash tra 3..."
        TestoNome.blitText()
        pygame.display.flip()
        time.sleep(1)
        TestoNome.string = "Crash tra 3...2..."
        TestoNome.blitText()
        pygame.display.flip()
        time.sleep(1)
        TestoNome.string = "Crash tra 3...2...1..."
        TestoNome.blitText()
        pygame.display.flip()
        time.sleep(1)
        TestoNome.string = "Scherzetto!!!!!"
    Profilo.blittaggio()
    TestoSchei.blitText()
    TestoSchei.string = str(schei)
    Coin.blittaggio()

    BottoneCasa.blittaggio()
    BottoneCamion.blittaggio()
    BottoneFabbrica.blittaggio()
    return finished

def mostraTutorial(boolean):
    """ Valori accettati (0,1) """
    global tutorialSlide, giocoIniziato, scrivendoNome, possibilitaDiScrivere, tutorialFinito
    if not tutorialFinito:
        if boolean:
            if tutorialSlide != 10:
                if pressedKeys[pygame.K_k] == 1:
                    if tutorialSlide != 7 and tutorialSlide != 8:
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
            elif tutorialSlide == 8:
                TestoTutorial.string = "Portali in casa con [SPAZIO]"
            elif tutorialSlide == 9:
                TestoTutorial.string = "Bravo! Adesso ti lascio. CIAO! [k]"
            elif tutorialSlide == 10:
                mostraProfilo()
                tutorialFinito = True 
                if not possibilitaDiScrivere:
                    scrivendoNome = True
                    possibilitaDiScrivere = True
                    TestoNome.string = ""
                
            
            if tutorialSlide < 6:
                if pressedKeys[pygame.K_p] == 1:
                    if tutorialSlide != 7:
                        tutorialSlide = 10
                        print("Premi K per completare il saltamento")
                        time.sleep(0.1)  
    else:
        giocoIniziato = True
        tutorialSlide = 10
        mostraProfilo()
        if not possibilitaDiScrivere:
            scrivendoNome = pickle.load(open("possibilitaDiScrivere.dat", "rb"))
            possibilitaDiScrivere = True
    return giocoIniziato
    

def salva():
    global caniInCasa,caniTrasportati,nome,jimmy,Casa,Trasporto,Fabbrica,schei,path,TestoNome,scrivendoNome, tutorialFinito
    pickle.dump(caniInCasa, open("caniInCasa.dat", "wb"))
    pickle.dump(caniTrasportati,open("caniTrasportati.dat","wb"))

    pickle.dump(TestoNome.string,open("nome.dat","wb"))
    pickle.dump(path,open("fotoprofilo.dat", "wb"))

    pickle.dump(Casa.livello,open("CasaLivello.dat", "wb"))
    pickle.dump(Trasporto.livello,open("TrasportoLivello.dat", "wb"))
    pickle.dump(Fabbrica.livello,open("FabbricaLivello.dat", "wb"))

    pickle.dump(schei, open("schei.dat", "wb"))

    pickle.dump(scrivendoNome,open("possibilitaDiScrivere.dat", "wb"))
    pickle.dump(tutorialFinito, open("tutorialFinito.dat", "wb"))
    

def carica():
    global caniInCasa,caniTrasportati,nome,jimmy,Casa,Trasporto,Fabbrica,schei,path, scrivendoNome, tutorialFinito
    caniInCasa = pickle.load(open("caniInCasa.dat", "rb")) 
    caniTrasportati = pickle.load(open("caniTrasportati.dat","rb"))

    TestoNome.string = pickle.load(open("nome.dat","rb"))
    path = pickle.load(open("fotoprofilo.dat", "rb"))
    jimmy = pygame.image.load(path)
    Profilo.costume = jimmy
    Profilo.cambiaCostume()

    Casa.livello = pickle.load(open("CasaLivello.dat", "rb"))
    Trasporto.livello = pickle.load(open("TrasportoLivello.dat", "rb"))
    Fabbrica.livello = pickle.load(open("FabbricaLivello.dat", "rb"))

    scrivendoNome = pickle.load(open("possibilitaDiScrivere.dat", "rb"))

    if Casa.livello == 1:
        Casa.costume = casa_1
        BottoneCasa.upgradeBottone(casa_upgrade_2)
        Casa.cambiaCostume()
    if Casa.livello == 2:
        Casa.costume = casa_2
        BottoneCasa.upgradeBottone(casa_upgrade_3)
        Casa.cambiaCostume()
    if Casa.livello == 3:
        Casa.costume = casa_3
        BottoneCasa.upgradeBottone(casa_upgrade_4)
        Casa.cambiaCostume()
    if Casa.livello == 4:
        Casa.costume = casa_4
        BottoneCasa.upgradeBottone(casa_upgrade_5)
        Casa.cambiaCostume()
    if Casa.livello == 5:
        Casa.costume = casa_5
        BottoneCasa.upgradeBottone(casa_upgrade_max)
        Casa.cambiaCostume()
    
    if Fabbrica.livello == 1:
        BottoneFabbrica.upgradeBottone(fabbrica_upgrade_2)
        Fabbrica.costume = fabbrica_1
        Fabbrica.cambiaCostume()
    if Fabbrica.livello == 2:
        BottoneFabbrica.upgradeBottone(fabbrica_upgrade_3)
        Fabbrica.costume = fabbrica_2
        Fabbrica.cambiaCostume()
    if Fabbrica.livello == 3:
        BottoneFabbrica.upgradeBottone(fabbrica_upgrade_4)
        Fabbrica.costume = fabbrica_3
        Fabbrica.cambiaCostume()
    if Fabbrica.livello == 4:
        BottoneFabbrica.upgradeBottone(fabbrica_upgrade_5)
        Fabbrica.costume = fabbrica_4
        Fabbrica.cambiaCostume()
    if Fabbrica.livello == 5:
        BottoneFabbrica.upgradeBottone(fabbrica_upgrade_max)
        Fabbrica.larghezza += 15
        Fabbrica.altezza += 15
        Fabbrica.x -= 10
        Fabbrica.costume = fabbrica_5
        Fabbrica.cambiaCostume()

    if Trasporto.livello == 1:
        Trasporto.costume = camion_1
        Trasporto.cambiaCostume()
        BottoneCamion.upgradeBottone(camion_upgrade_2)
    if Trasporto.livello == 2:
        Trasporto.costume = camion_2
        BottoneCamion.upgradeBottone(camion_upgrade_3)
        Trasporto.cambiaCostume()
    if Trasporto.livello == 3:
        Trasporto.costume = camion_3
        BottoneCamion.upgradeBottone(camion_upgrade_4)
        Trasporto.cambiaCostume()
    if Trasporto.livello == 4:
        Trasporto.costume = camion_4
        BottoneCamion.upgradeBottone(camion_upgrade_5)
        Trasporto.y -= 60
        Trasporto.larghezza = 80
        Trasporto.altezza = 65
        Trasporto.cambiaCostume()

    if Trasporto.livello == 5:
        BottoneCamion.upgradeBottone(camion_upgrade_max)
        Trasporto.costume = camion_5
        Trasporto.y -= 60
        Trasporto.larghezza = 80
        Trasporto.altezza = 80
        Trasporto.cambiaCostume()

    
        
               


    nome = TestoNome.string
    schei = pickle.load(open("schei.dat", "rb"))
    tutorialFinito = pickle.load(open("tutorialFinito.dat", "rb"))

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

    def cambiaCostume(self):
        self.sprite = pygame.transform.scale(self.costume, (self.larghezza, self.altezza))

    def printaggio(self):
        print(self.x, self.y)

    def upgrade(self, costume,costumeBottone,target):
        global schei, nome
        if self.livello == 0 and schei >=1:
            schei -= 1
            pygame.mixer.Sound.play(success)
            self.livello += 1
            self.costume = costume
            self.cambiaCostume()
            target.upgradeBottone(costumeBottone)#@todo sistemare!!!!
        
        elif self.livello == 1 and schei >=2:
            schei -= 2
            pygame.mixer.Sound.play(success)
            print("UPGRADE AL LV 2")
            self.costume = costume
            self.cambiaCostume()
            self.livello += 1
            target.upgradeBottone(costumeBottone)
        
        elif self.livello == 2 and schei >=3:
            schei -= 3
            pygame.mixer.Sound.play(success)
            print("UPGRADE AL LV 3")
            self.costume = costume
            self.cambiaCostume()
            self.livello += 1
            target.upgradeBottone(costumeBottone)
        
        elif self.livello == 3 and schei >=5:
            pygame.mixer.Sound.play(success)
            schei -= 5
            self.costume = costume
            self.cambiaCostume()
            print("UPGRADE AL LV 4")
            self.livello += 1
            target.upgradeBottone(costumeBottone)

        elif self.livello == 4 and schei >=10:
            schei -= 10
            self.costume = costume
            self.cambiaCostume()
            pygame.mixer.Sound.play(success)
            print("UPGRADE AL LV 5")
            self.livello += 1
            target.upgradeBottone(costumeBottone)
        else:
            pygame.mixer.Sound.play(error)

    def ricaricaCostume(self,costume):
        self.costume = costume
        self.cambiaCostume()
    
    def upgradeBottone(self,costume):
        self.costume = costume
        self.cambiaCostume()
        
            

        
        
        
        
        

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

    def aggiungiCarattere(self, char):
        if char in caratteri:
            self.string += char

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

Profilo = Sprite(0,0,60,60,r"Immagini\/profilo.png")
Coin = Sprite(100,34,30,30,r"Immagini\/dogecoin.png")


TestoTutorial = Text(0,0,32,black,"Benvenuto! Premi K per continuare")
TestoCasa = Text(480,410,32,black,"")
TestoFabbrica = Text(70,410,32,red,"Fermo")
TestoTrasporto = Text(Trasporto.x,Trasporto.y-10,32,green,"")
TestoSchei = Text(70,30,32,black,schei)
TestoNome = Text(70,0,32,black,"")

CopriTestoF = Rectangle(48, 408, 122, 35, white)

BottoneCasa = Sprite(530,0,60,60,r"Immagini\/casa_upgrade_1.png")
BottoneCamion = Sprite(460,0,60,60,r"Immagini\/camion_upgrade_1.png")
BottoneFabbrica = Sprite(390,0,60,60,r"Immagini\/fabbrica_upgrade_1.png")




                                                 
#==========================================================================================


finished = False

if os.path.exists('caniInCasa.dat'):
    carica()
else:
    salva()
print("Gioco di Simone Tesini / Tesohh.\nCollaborazione di Filippo Vicari / Filvi.")
screen.blit(background, (0,0))
pygame.display.flip()
time.sleep(3)
background = pygame.image.load(r"Immagini\/sfondo.png")
pygame.mixer.music.play(-1)




while not finished:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT: #quando si preme la X chiudi e salva
            salva()
            finished = True           
        if scrivendoNome:
            if event.type == pygame.KEYDOWN:
                TestoNome.aggiungiCarattere(pygame.key.name(event.key)) 
                if event.key == pygame.K_BACKSPACE:
                    TestoNome.string = TestoNome.string[:-1]

                if event.key == pygame.K_RETURN:
                    if len(TestoNome.string)>0:
                        pygame.mixer.Sound.play(success)
                        print(TestoNome.string)
                        scrivendoNome = False

                        root = Tk()
                        root.filename =  filedialog.askopenfilename(initialdir = ".",title = "Scegli una foto",filetypes = (("foto",".png"),("foto",".jpg")))
                        path = root.filename
                        if len(path) == 0:
                            path = r"Immagini\/profilo.png"
                            pygame.mixer.Sound.play(error)
                        jimmy = pygame.image.load(path)
                        Profilo.costume = jimmy
                        Profilo.cambiaCostume()
                        root.destroy()
                        if path != r"Immagini\/profilo.png":
                            pygame.mixer.Sound.play(success)
                    else:
                        TestoNome.string = "metti qualcosa"
                        pygame.mixer.Sound.play(error)
                        TestoNome.blitText()
                        pygame.display.flip()
                        time.sleep(1)
                        TestoNome.string = ""

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            upCasa = screen.blit(BottoneCasa.sprite, (BottoneCasa.x, BottoneCasa.y))
            upCamion = screen.blit(BottoneCamion.sprite,(BottoneCamion.x,BottoneCamion.y))
            upFabbrica = screen.blit(BottoneFabbrica.sprite,(BottoneFabbrica.x,BottoneFabbrica.y))
            
            if upCasa.collidepoint(x, y):
                if Casa.livello == 0:
                    Casa.upgrade(casa_1, casa_upgrade_2, BottoneCasa)
                    TestoCasa.color = black
                elif Casa.livello == 1:
                    Casa.upgrade(casa_2, casa_upgrade_3, BottoneCasa)
                    TestoCasa.color = black
                elif Casa.livello == 2:
                    Casa.upgrade(casa_3, casa_upgrade_4, BottoneCasa)
                    TestoCasa.color = black
                elif Casa.livello == 3:
                    Casa.upgrade(casa_4, casa_upgrade_5, BottoneCasa)
                    TestoCasa.color = black
                elif Casa.livello == 4:
                    Casa.upgrade(casa_5, casa_upgrade_max, BottoneCasa)
                    TestoCasa.color = black
                else:
                    pygame.mixer.Sound.play(error)
            if upCamion.collidepoint(x, y):
                if Trasporto.livello == 0:
                    Trasporto.upgrade(camion_1, camion_upgrade_2, BottoneCamion)
                elif Trasporto.livello == 1:
                    Trasporto.upgrade(camion_2, camion_upgrade_3, BottoneCamion)
                elif Trasporto.livello == 2:
                    Trasporto.upgrade(camion_3, camion_upgrade_4, BottoneCamion)
                elif Trasporto.livello == 3:
                    Trasporto.upgrade(camion_4, camion_upgrade_5, BottoneCamion)
                    Trasporto.y -= 60
                    Trasporto.larghezza = 80
                    Trasporto.altezza = 65
                    Trasporto.cambiaCostume()
                elif Trasporto.livello == 4:
                    Trasporto.upgrade(camion_5, camion_upgrade_max, BottoneCamion)
                    Trasporto.larghezza = 80
                    Trasporto.altezza = 80
                    Trasporto.cambiaCostume()
                    
                else:
                    pygame.mixer.Sound.play(error)

            if upFabbrica.collidepoint(x,y):
                if Fabbrica.livello == 0:
                    Fabbrica.upgrade(fabbrica_1, fabbrica_upgrade_2, BottoneFabbrica)
                    
                elif Fabbrica.livello == 1:
                    Fabbrica.upgrade(fabbrica_2,fabbrica_upgrade_3, BottoneFabbrica)
                    
                elif Fabbrica.livello == 2:
                    Fabbrica.upgrade(fabbrica_3,fabbrica_upgrade_4, BottoneFabbrica)
                    
                        
                elif Fabbrica.livello == 3:
                    Fabbrica.upgrade(fabbrica_4, fabbrica_upgrade_5, BottoneFabbrica)
                    
                elif Fabbrica.livello == 4:
                    Fabbrica.upgrade(fabbrica_5, fabbrica_upgrade_max, BottoneFabbrica)
                    
                    Fabbrica.larghezza += 15
                    Fabbrica.altezza += 15
                    Fabbrica.x -= 10
                    Fabbrica.cambiaCostume()
                else:
                    pygame.mixer.Sound.play(error)
                    


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

    # mousePos = pygame.mouse.get_pos()
    # mousePointer = (mousePos, 1,1)
    # mouseHitbox = blitBox("mouse")

    # decidi se mostrare o no il tutorial bool 0 / 1
    mostraTutorial(1)
    
    
    

    #tiene testocasa.string sempre alla quantita dei cani
    TestoCasa.string = str(caniInCasa)
    
    
    TestoTrasporto.blitText()
    TestoFabbrica.blitText()
    TestoCasa.blitText()

    if tutorialSlide != 10:
        TestoTutorial.blitText()
    else:
        TestoNome.blitText()

    

    if pressedKeys[pygame.K_SPACE] == 1:
        if giocoIniziato:

            if starting == False:
                pygame.mixer.Sound.play(camionStart) 
                starting = True


            if daDove == "casa":
                if Trasporto.livello == 0:
                    Trasporto.x -= .5
                if Trasporto.livello == 1:
                    Trasporto.x -= 1
                elif Trasporto.livello == 2:
                    Trasporto.x -= 1.5
                elif Trasporto.livello == 3:
                    Trasporto.x -= 2.5
                elif Trasporto.livello == 4:
                    Trasporto.x -= 4
                elif Trasporto.livello == 5:
                    Trasporto.x -= 10


                # cambia il testo del trasporto
                TestoTrasporto.string = str(quantitaTrasporto)

                #se la hitbox del camion tocca quello della fabbrica
                if hitboxCamion.colliderect(hitboxFabbrica): 
                    TestoFabbrica.color = orange
                    TestoFabbrica.string = "   . . ."
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
                    if Fabbrica.livello == 0:
                        numeroRandom = 1
                    if Fabbrica.livello == 1:
                        numeroRandom = random.randint(1,2)
                    if Fabbrica.livello == 2:
                        numeroRandom = random.randint(1,3)
                    if Fabbrica.livello == 3:
                        numeroRandom = random.randint(2,3)
                    if Fabbrica.livello == 4:
                        numeroRandom = 3
                    if Fabbrica.livello == 5:
                        numeroRandom = random.randint(3,4)




                    caneBlu = random.randint(1,1000)
                    if caneBlu == 1000:
                        schei += 20
                        # TestoFabbrica.string = ""
                    quantitaTrasporto += numeroRandom
                    TestoTrasporto.string = str(quantitaTrasporto)

                    if primaVolta:
                        tutorialSlide = 8
                        
                

            
            # se sto arrivando dalla fabbrica
            elif daDove == "fabbrica":
                if Trasporto.livello == 0:
                    Trasporto.x += .5
                if Trasporto.livello == 1:
                    Trasporto.x += 1
                elif Trasporto.livello == 2:
                    Trasporto.x += 1.5
                elif Trasporto.livello == 3:
                    Trasporto.x += 2.5
                elif Trasporto.livello == 4:
                    Trasporto.x += 4
                elif Trasporto.livello == 5:
                    Trasporto.x += 10
                
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

                    if primaVolta:
                        tutorialSlide = 9

                    if Casa.livello == 0 and caniInCasa >= 5: #basta copiare per i prossimi livelli
                        tooManyDogs(5)
                    elif Casa.livello == 1 and caniInCasa >= 10: 
                        tooManyDogs(10)
                    elif Casa.livello == 2 and caniInCasa >= 25: 
                        tooManyDogs(25)
                    elif Casa.livello == 3 and caniInCasa >= 40: 
                        tooManyDogs(40)
                    elif Casa.livello == 4 and caniInCasa >= 50: 
                        tooManyDogs(50)
                    elif Casa.livello == 5 and caniInCasa >= 100: 
                        tooManyDogs(100)


             

                

    
    pygame.display.flip()

    #muove la hitbox del camion
    Trasporto.hitbox = (Trasporto.x, Trasporto.y, Trasporto.larghezza, Trasporto.altezza)
    
    if Casa.livello == 0 and caniInCasa >= 5: 
        TestoCasa.color = red
    if Casa.livello == 1 and caniInCasa >= 10: 
        TestoCasa.color = red
    if Casa.livello == 2 and caniInCasa >= 25: 
        TestoCasa.color = red
    if Casa.livello == 3 and caniInCasa >= 40: 
        TestoCasa.color = red
    if Casa.livello == 4 and caniInCasa >= 50: 
        TestoCasa.color = red
    if Casa.livello == 5 and caniInCasa >= 100: 
        TestoCasa.color = red
        


    #muovi il testo del veicol
    TestoTrasporto.x = Trasporto.x
    TestoTrasporto.y = Trasporto.y - 30

    pygame.display.flip() #aggiorna lo schermo
    
    frame.tick(1000)