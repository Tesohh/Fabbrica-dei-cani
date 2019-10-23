import pandas
import random
from genera_nome_cane import generaNome
import time

everyDog = []


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
        
    def aggiungiDog(self, ):
        return ((self.name, self.perfect))

        
    def printaggio(self):
        print("=======================")
        print(f"Nome: {self.name}\nVelocità: {self.speed}\nPelosità: {self.furriness}\nAbbiatezza: {self.barkiness}\naffettuosità: {self.awwness}\nPerfetto? {self.perfect}")
        print("=======================")
    



qualita = 0





for i in range(0,10):
    temp = f"doggo{i}"
    
doggo = Cane(qualita)
doggo2 = Cane(qualita)
doggo3 = Cane(qualita)
doggo.printaggio()
doggo2.printaggio()
doggo3.printaggio()
everyDog.append(doggo.aggiungiDog())
everyDog.append(doggo2.aggiungiDog())
everyDog.append(doggo3.aggiungiDog())

print(everyDog)









