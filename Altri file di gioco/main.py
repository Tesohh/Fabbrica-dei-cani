from dognames import lista_nomi as nomiCani
import random
import os


# # fa scegliere all'utente quanti nomi vuole generare
# def quantitaNomi():
#     quanto = input("Quanti nomi genero?\n")
    
#     # controlla se l'input è un numero e ritorna il numero
#     try:
#         quanto = int(quanto) + 1
#         return quanto

#     # se non lo è dai un errore e ritorna False    
#     except ValueError as err:
#         os.system("cls")
#         print(f"Hai inserito un valore non numerico\nErrore: {err}")
#         return False

#genera i nomi con la nostra quantità
def generaNomi(quanto):

    # controlla se l'input è un numero, se si printa i nomi
    try: 
        for i in range(1,quanto):
            indiceNomi = random.randint(0,len(nomiCani))
            print(f"Nome cane {i}: {nomiCani[indiceNomi]}")
        return indiceNomi

    #se è sbagliato da errore
    except TypeError as err:
        os.system("cls")
        print(f"\n\nHai inserito un valore non numerico\nBanana: {err}")
        return False

#controllo che tutto sia giusto e continua a chiederlo        
while True:
    # testVariabile = quantitaNomi()
    
    # controllo che quantitaNomi() non sia false
    testLista = generaNomi(1)
        
        # controllo che generaNomi() non sia false        
    if testLista:
        break

