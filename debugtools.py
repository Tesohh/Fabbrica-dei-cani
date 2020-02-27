import pickle
# import gioco

richiesta = input("schei / livellocasa / livellocamion / livellofabbrica / caniincasa\n")

if richiesta == "schei":
    valore = int(input("Inserire valore: "))
    if not isinstance(valore, int):
        print("Valore non valido.")
    else: 
        pickle.dump(valore, open("schei.dat", "wb"))
        print(f"Modificato {richiesta} a {valore}")

elif richiesta == "livellocasa":
    valore = int(input("Inserire valore: "))
    if not valore >= 5 and not isinstance(valore, int):
        print("Valore non valido o troppo alto.")
    else: 
        pickle.dump(valore, open("CasaLivello.dat", "wb"))
        print(f"Modificato {richiesta} a {valore}")

elif richiesta == "livellocamion":
    valore = int(input("Inserire valore: "))
    if not valore >= 5 and not isinstance(valore, int):
        print("Valore non valido o troppo alto.")
    else: 
        pickle.dump(valore, open("TrasportoLivello.dat", "wb"))
        print(f"Modificato {richiesta} a {valore}")

elif richiesta == "livellofabbrica":
    valore = int(input("Inserire valore: "))
    if not valore >= 5 and not isinstance(valore, int):
        print("Valore non valido o troppo alto.")
    else: 
        pickle.dump(valore, open("FabbricaLivello.dat", "wb"))
        print(f"Modificato {richiesta} a {valore}")

elif richiesta == "caniincasa":
    valore = int(input("Inserire valore: "))
    pickle.dump(valore, open("caniInCasa.dat", "wb"))
    print(f"Modificato {richiesta} a {valore}")

else:
    print(f'Richiesta "{richiesta}" non valida!')
    