#INIZIO
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
from costumi import Casaa,Fabbricaa,Camionn,Bottonii



#============================================================================================
#PRELIMINARI
#============================================================================================ pygame.init() #inizializziamo pygame
pygame.mixer.init()
musica = pygame.mixer.music.load(r"Suoni/flauteggiamento.wav")
pygame.mixer.music.set_volume(0.1)


icona = pygame.image.load(r"Loghi/icona.ico")

pygame.display.set_icon(icona)  

screen = pygame.display.set_mode((600,600)) #impostiamo le dimensioni della finestra

pygame.display.set_caption("La Fabbrica dei Cybercani")

pygame.font.init()
font = pygame.font.Font(r"Font/noto.ttf", 28)




#============================================================================================
#VARIABILI
#============================================================================================
rosso = (255,0,0) #R, G, B
colore2 = (120,50,100)

background = pygame.image.load(r"Loghi/splashscreen.png")
background = pygame.transform.scale(background, (600,600))


jimmy = pygame.image.load(r"Immagini/jimmyneutron.png")
easteregg = pygame.image.load(r"Immagini/easteregg.png")



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
path = r"Immagini/profilo.png"
caniSelezionati = 5
caniMassimiInCasa = 5
haGuardatoIntro = False

caratteri = "abcdefghijklmnopqrstuvwxyz1234567890"
scrivendoNome = True

selezionandoNumero = False 


woof = pygame.mixer.Sound(r"Suoni/woof.wav")
microWoof = pygame.mixer.Sound(r"Suoni/woofHigh.wav")
camionStart = pygame.mixer.Sound(r"Suoni/camionStart.wav")
camionGo = pygame.mixer.Sound(r"Suoni/camion.wav")
success = pygame.mixer.Sound(r"Suoni/success.wav")
error = pygame.mixer.Sound(r"Suoni/error.wav")
splashscreen = pygame.mixer.Sound(r"Suoni/splashscreen.wav")
kaching = pygame.mixer.Sound(r"Suoni/kaching.wav")
intro = pygame.mixer.Sound(r"Suoni/narrazione.wav")

pygame.mixer.Sound.set_volume(camionStart, 0.2)
pygame.mixer.Sound.set_volume(success, 0.4)
pygame.mixer.Sound.set_volume(error, 5)

scena = "home"


#============================================================================================
#FUNZIONI
#============================================================================================
def caricamento(cosaDopo):
    global scena, background
    scena = "caricamento"
    background = pygame.image.load(r"Immagini/caricamento.png")



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
    global primaVolta, schei, finished, nome, Casa, Fabbrica, Trasporto, selezionandoNumero

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
    
    if scena == "home":
        Profilo.blittaggio()
        TestoSchei.blitText()
        TestoSchei.string = str(schei)
        Coin.x = TestoSchei.x + int(TestoSchei.returnSize()[0]) + 5
        Coin.blittaggio()

        BottoneCasa.blittaggio()
        BottoneCamion.blittaggio()
        BottoneFabbrica.blittaggio()

        if caniInCasa < 5:
            BottoneVendi.costume = Bottonii.vendigrigio
            BottoneVendi.cambiaCostume()
        else:
            BottoneVendi.costume = Bottonii.vendi
            BottoneVendi.cambiaCostume()

        if not selezionandoNumero:
            BottoneVendi.blittaggio()
        else:
            BottoneMenoCani.blittaggio()
            BottonePiuCani.blittaggio()
            TestoSelettore.blitText()
            BottoneConferma.blittaggio()
            BottoneAnnulla.blittaggio()
            BottoneConferma.x = posx_btn + width_btn/2 -  BottoneConferma.larghezza/2
            BottoneAnnulla.x = posx_btn + width_btn/2 -  BottoneAnnulla.larghezza/2
    return finished
def spostaTutorialAvanti():
    tutorial1.spostaAvanti()
    tutorial2.spostaAvanti()
    tutorial3.spostaAvanti()
    tutorial4.spostaAvanti()
    tutorial5.spostaAvanti()
    tutorial6.spostaAvanti()
    tutorial7.spostaAvanti()
    tutorial8.spostaAvanti()
    tutorial9.spostaAvanti()
    tutorial10.spostaAvanti()
def spostaTutorialIndietro():
    tutorial1.spostaIndietro()
    tutorial2.spostaIndietro()
    tutorial3.spostaIndietro()
    tutorial4.spostaIndietro()
    tutorial5.spostaIndietro()
    tutorial6.spostaIndietro()
    tutorial7.spostaIndietro()
    tutorial8.spostaIndietro()
    tutorial9.spostaIndietro()
    tutorial10.spostaIndietro()
    
def mostraTutorial(boolean):
    """ Valori accettati (0,1) """
    global tutorialSlide, giocoIniziato, scrivendoNome, possibilitaDiScrivere, tutorialFinito
    if not tutorialFinito:
        if boolean:
            if tutorialSlide == 10:
                mostraProfilo()
                background = pygame.image.load(r"Immagini/sfondo.png")
                tutorialFinito = True 
                if not possibilitaDiScrivere:
                    scrivendoNome = True
                    possibilitaDiScrivere = True
                    TestoNome.string = ""
        tutorial1.blittaggio()
        tutorial2.blittaggio()
        tutorial3.blittaggio()
        tutorial4.blittaggio()
        tutorial5.blittaggio()
        tutorial6.blittaggio()
        tutorial7.blittaggio()
        tutorial8.blittaggio()
        tutorial9.blittaggio()
        tutorial10.blittaggio()
        if tutorialSlide != 0 and not tutorialSlide >= 6:
            BottoneIndietro.blittaggio()
        if tutorialSlide != 6 and tutorialSlide != 7:
            BottoneAvanti.blittaggio()

        if tutorialSlide == 6 or tutorialSlide == 7:
            Profilo.blittaggio()
            TestoNome.x = Profilo.x + Profilo.larghezza/2 - TestoNome.returnSize()[0]/2
            TestoNome.y = Profilo.y + Profilo.altezza + 20
            TestoNome.blitText()
            #@TODO fare che quando si arriva alla home il profilo e il testonome siano al posto giusto

        
    else:
        giocoIniziato = True
        tutorialSlide = 10
        mostraProfilo()
        
        #Profilo = Sprite(70,0,60,60,r"Immagini/profilo.png")
        if not possibilitaDiScrivere:
            scrivendoNome = pickle.load(open("possibilitaDiScrivere.dat", "rb"))
            possibilitaDiScrivere = True
        
        
    return giocoIniziato
    

def salva():
    global caniInCasa,caniTrasportati,nome,jimmy,Casa,Trasporto,Fabbrica,schei,path,TestoNome,scrivendoNome, tutorialFinito, caniMassimiInCasa, haGuardatoIntro
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
    pickle.dump(caniMassimiInCasa, open("caniMassimiInCasa.dat","wb"))
    pickle.dump(haGuardatoIntro, open("haGuardatoIntro.dat","wb"))
    

def carica():
    global caniInCasa,caniTrasportati,nome,jimmy,Casa,Trasporto,Fabbrica,schei,path, scrivendoNome, tutorialFinito,caniMassimiInCasa, haGuardatoIntro
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
    haGuardatoIntro = pickle.load(open("haGuardatoIntro.dat", "rb"))

    if Casa.livello == 1:
        Casa.costume = Casaa.casa_1
        BottoneCasa.upgradeBottone(Casaa.casa_upgrade_2)
        Casa.cambiaCostume()
    if Casa.livello == 2:
        Casa.costume = Casaa.casa_2
        BottoneCasa.upgradeBottone(Casaa.casa_upgrade_3)
        Casa.cambiaCostume()
    if Casa.livello == 3:
        Casa.costume = Casaa.casa_3
        BottoneCasa.upgradeBottone(Casaa.casa_upgrade_4)
        Casa.cambiaCostume()
    if Casa.livello == 4:
        Casa.costume = Casaa.casa_4
        BottoneCasa.upgradeBottone(Casaa.casa_upgrade_5)
        Casa.cambiaCostume()
    if Casa.livello == 5:
        Casa.costume = Casaa.casa_5
        BottoneCasa.upgradeBottone(Casaa.casa_upgrade_max)
        Casa.cambiaCostume()
    
    if Fabbrica.livello == 1:
        BottoneFabbrica.upgradeBottone(Fabbricaa.fabbrica_upgrade_2)
        Fabbrica.costume = Fabbricaa.fabbrica_1
        Fabbrica.cambiaCostume()
    if Fabbrica.livello == 2:
        BottoneFabbrica.upgradeBottone(Fabbricaa.fabbrica_upgrade_3)
        Fabbrica.costume = Fabbricaa.fabbrica_2
        Fabbrica.cambiaCostume()
    if Fabbrica.livello == 3:
        BottoneFabbrica.upgradeBottone(Fabbricaa.fabbrica_upgrade_4)
        Fabbrica.costume = Fabbricaa.fabbrica_3
        Fabbrica.cambiaCostume()
    if Fabbrica.livello == 4:
        BottoneFabbrica.upgradeBottone(Fabbricaa.fabbrica_upgrade_5)
        Fabbrica.costume = Fabbricaa.fabbrica_4
        Fabbrica.cambiaCostume()
    if Fabbrica.livello == 5:
        BottoneFabbrica.upgradeBottone(Fabbricaa.fabbrica_upgrade_max)
        Fabbrica.larghezza += 15
        Fabbrica.altezza += 15
        Fabbrica.x -= 10
        Fabbrica.costume = Fabbricaa.fabbrica_5
        Fabbrica.cambiaCostume()

    if Trasporto.livello == 1:
        Trasporto.costume = Camionn.camion_1
        Trasporto.cambiaCostume()
        BottoneCamion.upgradeBottone(Camionn.camion_upgrade_2)
    if Trasporto.livello == 2:
        Trasporto.costume = Camionn.camion_2
        BottoneCamion.upgradeBottone(Camionn.camion_upgrade_3)
        Trasporto.cambiaCostume()
    if Trasporto.livello == 3:
        Trasporto.costume = Camionn.camion_3
        BottoneCamion.upgradeBottone(Camionn.camion_upgrade_4)
        Trasporto.cambiaCostume()
    if Trasporto.livello == 4:
        Trasporto.costume = Camionn.camion_4
        BottoneCamion.upgradeBottone(Camionn.camion_upgrade_5)
        Trasporto.y -= 60
        Trasporto.larghezza = 80
        Trasporto.altezza = 65
        Trasporto.cambiaCostume()

    if Trasporto.livello == 5:
        BottoneCamion.upgradeBottone(Camionn.camion_upgrade_max)
        Trasporto.costume = Camionn.camion_5
        Trasporto.y -= 60
        Trasporto.larghezza = 80
        Trasporto.altezza = 80
        Trasporto.cambiaCostume()

    
        
               


    nome = TestoNome.string
    schei = pickle.load(open("schei.dat", "rb"))
    tutorialFinito = pickle.load(open("tutorialFinito.dat", "rb"))
    caniMassimiInCasa = pickle.load(open("caniMassimiInCasa.dat", "rb"))

#============================================================================================
#CLASSI 
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
    def spostaAvanti(self):
        self.x -= 600
            # time.sleep(0.01)
    def spostaIndietro(self):
        self.x += 600
    
    

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
    
    def returnSize(self):
        self.text_width, self.text_height = font.size(self.string)
        size = (self.text_width, self.text_height)
        #print(f"Text width:{self.text_width} Text height:{self.text_height}")
        return size 

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
#ISTANZE
#==========================================================================================

Fabbrica = Edificio(50, 290, 120, 120, r"Immagini/fabbrica.png")
Casa = Edificio(430, 290, 120, 120, r"Immagini/casa_base.png")

Trasporto = Veicolo(360, 370, 70, 34, r"Immagini/veicolo_base.png")



Profilo = Sprite(225,123,150,150,r"Immagini/profilo.png")
#Profilo = Sprite(70,0,60,60,r"Immagini/profilo.png")


TestoNome = Text(70,0,32,black,"")




Coin = Sprite(100,34,30,30,r"Immagini/dogecoin.png")




TestoTutorial = Text(0,0,32,black,"Benvenuto! Premi K per continuare")
TestoCasa = Text(480,410,32,black,"")
TestoFabbrica = Text(70,410,32,red,"Fermo")
TestoTrasporto = Text(Trasporto.x,Trasporto.y-10,32,green,"")
TestoSchei = Text(70,30,32,black,schei)
TestoSottoSchei = Text(TestoSchei.x,TestoSchei.y+10,32,black, "")





CopriTestoF = Rectangle(48, 408, 122, 35, white)

BottoneCasa = Sprite(530,0,60,60,r"Immagini/casa_upgrade_1.png")
BottoneCamion = Sprite(460,0,60,60,r"Immagini/camion_upgrade_1.png")
BottoneFabbrica = Sprite(390,0,60,60,r"Immagini/fabbrica_upgrade_1.png")

width_btn = 92
height_btn = 33
posx_btn = Casa.x + Casa.larghezza/2 -  width_btn/2
posy_btn = 454
# definisco la posizione e la dimensione della freccetta SINISTRA per decrementare il valore dei cani venduti
width_menoCaniVendita = 23
height_menoCaniVendita = 28
posx_menoCaniVendita = posx_btn
posy_menoCaniVendita = posy_btn 

# definisco la posizione e la dimensione della freccetta DESTRA per decrementare il valore dei cani venduti

width_piuCaniVendita = 23
height_piuCaniVendita = 28
posx_piuCaniVendita = posx_btn + width_btn - width_piuCaniVendita
posy_piuCaniVendita = posy_btn

BottoneVendi = Sprite(posx_btn,posy_btn,width_btn,height_btn,r"Immagini/vendigrigio.png")

BottoneMenoCani = Sprite(posx_menoCaniVendita,posy_menoCaniVendita,width_menoCaniVendita,height_menoCaniVendita,r"Immagini/menoCani.png")
BottonePiuCani = Sprite(posx_piuCaniVendita,posy_piuCaniVendita,width_piuCaniVendita,height_piuCaniVendita,r"Immagini/piuCani.png")

posx_testoSel = posx_btn + width_btn/2
TestoSelettore = Text(posx_testoSel, posy_btn-5, 28, black,caniSelezionati)

posx_testoSel = posx_btn + width_btn/2 -  TestoSelettore.returnSize()[0]/2
TestoSelettore.x = posx_testoSel

BottoneConferma = Sprite(posx_btn, posy_menoCaniVendita+BottoneMenoCani.altezza+7, 93, 27, r"Immagini/conferma.png")
BottoneAnnulla = Sprite(posx_btn, BottoneConferma.y+BottoneConferma.altezza+7, 93, 27, r"Immagini/annulla.png")

Barretta = Sprite(198, 492, 5, 49, r"Immagini/barretta.png")

BottoneFacile = Sprite(64,229, 144,141,r"Immagini/facile.png")
BottoneMedioLock = Sprite(222,209, 155,161,r"Immagini/medio_lock.png")
BottoneMedio = Sprite(228,229, 144,141,r"Immagini/medio.png")
BottoneDifficileLock = Sprite(391,209, 155,161,r"Immagini/difficile_lock.png")
BottoneDifficile = Sprite(392,229, 144,141,r"Immagini/difficile.png")

DettagliFacile = Sprite(64,399, 489, 164, r"Immagini/dettagli_facile.png")
DettagliMedio = Sprite(64,399, 489, 164, r"Immagini/dettagli_medio.png")
DettagliDifficile = Sprite(64,399, 489, 164, r"Immagini/dettagli_difficile.png")

tutorial1 = Sprite(0,0,600,600, r"Immagini/background 1.png")
tutorial2 = Sprite(600,0,600,600, r"Immagini/background 2.png")
tutorial3 = Sprite(1200,0,600,600, r"Immagini/background 3.png")
tutorial4 = Sprite(1800,0,600,600, r"Immagini/background 4.png")
tutorial5 = Sprite(2400,0,600,600, r"Immagini/background 5.png")
tutorial6 = Sprite(3000,0,600,600, r"Immagini/background 6.png")
tutorial7 = Sprite(3600,0,600,600, r"Immagini/background 7.png")
tutorial8 = Sprite(4200,0,600,600, r"Immagini/background 8.png")
tutorial9 = Sprite(4800,0,600,600, r"Immagini/background 9.png")
tutorial10 = Sprite(5400,0,600,600, r"Immagini/background 10.png")

BottoneAvanti = Sprite(600-64, 237, 44, 44, r"Immagini/freccia destra.png")
BottoneIndietro = Sprite(24, 237, 44, 44, r"Immagini/freccia sinistra.png")






                                                 
#==========================================================================================
#LOGIN
#==========================================================================================

finished = False


if os.path.exists('caniInCasa.dat'):
    carica()
else:
    salva()


print("Gioco di Simone Tesini / Tesohh.\nCollaborazione di Filippo Vicari / Filvi.")
if nome == "leo":
    background = pygame.image.load(r"Loghi/leo.png")
if nome == "matteo":
    background = pygame.image.load(r"Loghi/matte.png")
if nome == "tesohh":
    background = pygame.image.load(r"Loghi/tesohh.png")

pygame.display.flip()





if not haGuardatoIntro:
    time.sleep(3)
    scena = "intro"

elif tutorialSlide == 0:
    scena = "caricamento"
    background = pygame.image.load(r"Immagini/caricamento.png")
    pygame.mixer.Sound.play(splashscreen)
    pygame.mixer.music.play(-1)
    print("bellas")
    Profilo.x = 70
    Profilo.y = 0
    Profilo.larghezza = 60
    Profilo.altezza = 60
    Profilo.cambiaCostume()
    TestoNome.x = 20
    TestoNome.y = 10
    





#==========================================================================================
#EVENTI
#==========================================================================================
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
                        tutorialSlide += 1
                        spostaTutorialAvanti()
                        root = Tk()
                        root.filename =  filedialog.askopenfilename(initialdir = ".",title = "Scegli una foto",filetypes = (("foto",".png"),("foto",".jpg")))
                        path = root.filename
                        if len(path) == 0:
                            path = r"Immagini/profilo.png"
                            pygame.mixer.Sound.play(error)
                        jimmy = pygame.image.load(path)
                        Profilo.costume = jimmy
                        Profilo.cambiaCostume()
                        root.destroy()
                        if path != r"Immagini/profilo.png":
                            pygame.mixer.Sound.play(success)
                            tutorialSlide += 1
                            spostaTutorialAvanti()

                    else:
                        TestoNome.string = "metti qualcosa"
                        pygame.mixer.Sound.play(error)
                        TestoNome.blitText()
                        pygame.display.flip()
                        time.sleep(1)
                        TestoNome.string = ""
#==========================================================================================
#CLICK
#==========================================================================================
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            upCasa = screen.blit(BottoneCasa.sprite, (BottoneCasa.x, BottoneCasa.y))
            upCamion = screen.blit(BottoneCamion.sprite,(BottoneCamion.x,BottoneCamion.y))
            upFabbrica = screen.blit(BottoneFabbrica.sprite,(BottoneFabbrica.x,BottoneFabbrica.y))

            botVendi = screen.blit(BottoneVendi.sprite,(BottoneVendi.x,BottoneVendi.y))

            botPiuCani = screen.blit(BottonePiuCani.sprite,(BottonePiuCani.x,BottonePiuCani.y))
            botMenoCani = screen.blit(BottoneMenoCani.sprite,(BottoneMenoCani.x,BottoneMenoCani.y))   
            botAnnulla = screen.blit(BottoneAnnulla.sprite,(BottoneAnnulla.x,BottoneAnnulla.y))   
            botConferma = screen.blit(BottoneConferma.sprite,(BottoneConferma.x,BottoneConferma.y))

            botFacile = screen.blit(BottoneFacile.sprite, (BottoneFacile.x,BottoneFacile.y))         
            botMedio = screen.blit(BottoneMedio.sprite, (BottoneMedio.x,BottoneMedio.y))         
            botDifficile = screen.blit(BottoneDifficile.sprite, (BottoneDifficile.x,BottoneDifficile.y))     
            avanti = screen.blit(BottoneAvanti.sprite,(BottoneAvanti.x,BottoneAvanti.y)) 
            indietro = screen.blit(BottoneIndietro.sprite,(BottoneIndietro.x,BottoneIndietro.y)) 

            if avanti.collidepoint(x, y):
                #if tutorialSlide != 6 and tutorialSlide != 7 and tutorialSlide != 9:
                tutorialSlide += 1 
                spostaTutorialAvanti()

            if indietro.collidepoint(x, y):
                if tutorialSlide != 0 and tutorialSlide != 6 and tutorialSlide != 7 and tutorialSlide != 8:
                    tutorialSlide -= 1   
                    spostaTutorialIndietro()

            if upCasa.collidepoint(x, y):
                if Casa.livello == 0:
                    Casa.upgrade(Casaa.casa_1, Casaa.casa_upgrade_2, BottoneCasa)
                    caniMassimiInCasa = 10
                    TestoCasa.color = black
                elif Casa.livello == 1:
                    Casa.upgrade(Casaa.casa_2, Casaa.casa_upgrade_3, BottoneCasa)
                    TestoCasa.color = black
                    caniMassimiInCasa = 25
                elif Casa.livello == 2:
                    Casa.upgrade(Casaa.casa_3, Casaa.casa_upgrade_4, BottoneCasa)
                    TestoCasa.color = black
                    caniMassimiInCasa = 40
                elif Casa.livello == 3:
                    Casa.upgrade(Casaa.casa_4, Casaa.casa_upgrade_5, BottoneCasa)
                    TestoCasa.color = black
                    caniMassimiInCasa = 50
                elif Casa.livello == 4:
                    Casa.upgrade(Casaa.casa_5, Casaa.casa_upgrade_max, BottoneCasa)
                    TestoCasa.color = black
                    caniMassimiInCasa = 100
                else:
                    pygame.mixer.Sound.play(error)

            if upCamion.collidepoint(x, y):
                if Trasporto.livello == 0:
                    Trasporto.upgrade(Camionn.camion_1, Camionn.camion_upgrade_2, BottoneCamion)
                elif Trasporto.livello == 1:
                    Trasporto.upgrade(Camionn.camion_2, Camionn.camion_upgrade_3, BottoneCamion)
                elif Trasporto.livello == 2:
                    Trasporto.upgrade(Camionn.camion_3, Camionn.camion_upgrade_4, BottoneCamion)
                elif Trasporto.livello == 3:
                    Trasporto.upgrade(Camionn.camion_4, Camionn.camion_upgrade_5, BottoneCamion)
                    Trasporto.y -= 60
                    Trasporto.larghezza = 80
                    Trasporto.altezza = 65
                    Trasporto.cambiaCostume()
                elif Trasporto.livello == 4:
                    Trasporto.upgrade(Camionn.camion_5, Camionn.camion_upgrade_max, BottoneCamion)
                    Trasporto.larghezza = 80
                    Trasporto.altezza = 80
                    Trasporto.cambiaCostume()
                    
                else:
                    pygame.mixer.Sound.play(error)

            if upFabbrica.collidepoint(x,y):
                if Fabbrica.livello == 0:
                    Fabbrica.upgrade(Fabbricaa.fabbrica_1, Fabbricaa.fabbrica_upgrade_2, BottoneFabbrica)
                    
                elif Fabbrica.livello == 1:
                    Fabbrica.upgrade(Fabbricaa.fabbrica_2,Fabbricaa.fabbrica_upgrade_3, BottoneFabbrica)
                    
                elif Fabbrica.livello == 2:
                    Fabbrica.upgrade(Fabbricaa.fabbrica_3,Fabbricaa.fabbrica_upgrade_4, BottoneFabbrica)
                    
                        
                elif Fabbrica.livello == 3:
                    Fabbrica.upgrade(Fabbricaa.fabbrica_4, Fabbricaa.fabbrica_upgrade_5, BottoneFabbrica)
                    
                elif Fabbrica.livello == 4:
                    Fabbrica.upgrade(Fabbricaa.fabbrica_5, Fabbricaa.fabbrica_upgrade_max, BottoneFabbrica)
                    
                    Fabbrica.larghezza += 15
                    Fabbrica.altezza += 15
                    Fabbrica.x -= 10
                    Fabbrica.cambiaCostume()
                else:
                    pygame.mixer.Sound.play(error)
            if not selezionandoNumero:
                if botVendi.collidepoint(x,y):
                    if caniInCasa >= 5:
                        selezionandoNumero = True
                    else:
                        pygame.mixer.Sound.play(error)
            else:
                if botPiuCani.collidepoint(x,y):
                    if (caniSelezionati != caniMassimiInCasa) and caniSelezionati != caniInCasa:
                        caniSelezionati += 5
                        if (caniSelezionati >= caniInCasa):
                            caniSelezionati = caniInCasa
                            TestoSelettore.color = red
                        else:
                            TestoSelettore.color = black
                        TestoSelettore.string = str(caniSelezionati)
                        TestoSelettore.x = posx_btn + width_btn/2 -  TestoSelettore.returnSize()[0]/2
                    else:
                        pygame.mixer.Sound.play(error)
                        TestoSelettore.color = red
                elif botMenoCani.collidepoint(x,y):
                    #@IDEA quando è a zero il bottone menocani e la conferma diventa grigia
                    if caniSelezionati > 0:
                        TestoSelettore.color = black
                        caniSelezionati -= 5
                        if caniSelezionati < 0:
                            caniSelezionati = 0
                        if caniSelezionati == 0:
                            TestoSelettore.color = red
                        else:
                            TestoSelettore.color = black
                        TestoSelettore.string = str(caniSelezionati)
                        TestoSelettore.x = posx_btn + width_btn/2 -  TestoSelettore.returnSize()[0]/2
                    else:
                        pygame.mixer.Sound.play(error)
                    
                elif botAnnulla.collidepoint(x,y):
                    selezionandoNumero = False
                elif botConferma.collidepoint(x,y):
                    if caniSelezionati != 0:
                        scena = "difficolta"
                    else:
                        pygame.mixer.Sound.play(error)
            if scena == "difficolta":
                if botFacile.collidepoint(x,y):
                    scena = "home"
                    caniInCasa -= caniSelezionati
                    schei += 0.1 * caniSelezionati
                    background = pygame.image.load(r"Immagini/sfondo.png")
                    pygame.display.flip()
                    selezionandoNumero = False
                    pygame.display.flip()
                    pygame.mixer.Sound.play(kaching)
                if botMedio.collidepoint(x,y):
                    if Trasporto.livello >= 3:
                        scena = "medio"
                    else:
                        pygame.mixer.Sound.play(error)

                if botDifficile.collidepoint(x,y):
                    if Trasporto.livello >= 4:
                        scena = "difficile"
                    else:
                        pygame.mixer.Sound.play(error)
               
#==========================================================================================
#SCENE / BLITTAMENTI
#==========================================================================================
    if scena == "intro":
        background = pygame.image.load(r"Immagini/black.png")
        pygame.mixer.Sound.play(intro)
        time.sleep(29)
        haGuardatoIntro = True
        scena = "home"
        background = pygame.image.load(r"Immagini/sfondo.png")
        pygame.mixer.music.play(-1)


    
    if scena == "home":
        hitboxCamion = blitBox("camion")
        hitboxCasa = blitBox("casa")
        hitboxFabbrica = blitBox("fabbrica")

    screen.blit(background, (0,0))

    if scena == "home":
        Fabbrica.blittaggio()
        Casa.blittaggio()
        Trasporto.blittaggio()

    elif scena == "caricamento":
        Barretta.blittaggio()
        if Barretta.larghezza != 210:
            Barretta.larghezza += 1
            Barretta.cambiaCostume()
        else:
            time.sleep(1.5)
            scena = "home"
            selezionandoNumero = False
            background = pygame.image.load(r"Immagini/sfondo.png")
            Barretta.larghezza = 5

    elif scena == "difficolta":
        background = pygame.image.load(r"Immagini/black.png")
        BottoneFacile.blittaggio()
        if Trasporto.livello >= 3:
            BottoneMedio.blittaggio()
        else:
            BottoneMedioLock.blittaggio()
        if Trasporto.livello >= 4:
            BottoneDifficile.blittaggio()
        else:
            BottoneDifficileLock.blittaggio()


        botFacile = screen.blit(BottoneFacile.sprite, (BottoneFacile.x,BottoneFacile.y))    
        botMedio = screen.blit(BottoneMedio.sprite, (BottoneMedio.x,BottoneMedio.y))    
        botDifficile = screen.blit(BottoneDifficile.sprite, (BottoneDifficile.x,BottoneDifficile.y))
        
        if botFacile.collidepoint(pygame.mouse.get_pos()):
            DettagliFacile.blittaggio()
        if botMedio.collidepoint(pygame.mouse.get_pos()):
            DettagliMedio.blittaggio()
        if botDifficile.collidepoint(pygame.mouse.get_pos()):
            DettagliDifficile.blittaggio()

    elif scena == "medio":
        pass


    # decidi se mostrare o no il tutorial bool 0 / 1

    #tiene testocasa.string sempre alla quantita dei cani
    TestoCasa.string = str(caniInCasa)
    
    if scena == "home":
        TestoTrasporto.blitText()
        TestoFabbrica.blitText()
        TestoCasa.blitText()
    
    TestoCasa.x = Casa.x + Casa.larghezza/2 -  TestoCasa.returnSize()[0]/2
    TestoFabbrica.x = Fabbrica.x + Fabbrica.larghezza/2 -  TestoFabbrica.returnSize()[0]/2

    if tutorialSlide != 10:
        TestoTutorial.blitText()
    else:
        if scena == "home":
            TestoNome.blitText()
        
        
        

        


#==========================================================================================
#TASTI
#==========================================================================================
    pressedKeys = pygame.key.get_pressed()

    mostraTutorial(1)
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

                    if caniInCasa >= caniMassimiInCasa: #basta copiare per i prossimi livelli
                        tooManyDogs(caniMassimiInCasa)
                    


             

                

    
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

#FINE
    frame.tick(1000)