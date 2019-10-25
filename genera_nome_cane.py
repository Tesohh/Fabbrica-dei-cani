from dognames import lista_nomi as nomiCani
import random
import os



#genera i nomi con la nostra quantità
def generaNome():
    indiceNomi = random.randint(0,len(nomiCani))
    return nomiCani[indiceNomi]




