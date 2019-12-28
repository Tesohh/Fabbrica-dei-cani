def raddoppia(asgarra):
    asgarra = asgarra * 2
    return asgarra

triplica = lambda a: a * 3
printa = lambda cosa: print(cosa)

numeri = [2,5,8,1]
numeridoppi = map(raddoppia, numeri)
numeritripli = map(triplica, numeri)

printa(f"Numeri: {numeri}")
printa(f"Numeri raddoppiati: {list(numeridoppi)}")
printa(f"Numeri triplicati: {list(numeritripli)}")
