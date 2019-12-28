import pickle

# punti = 0
# banane = 2

# print("Asgarra")

# punti = 10
# print("Punti:", punti)
# print("Banane:", banane)

# pickle.dump(punti, open("punti.dat", "wb"))
# pickle.dump(banane, open("banane.dat", "wb"))


# print("persi 5 punti") 
# punti = 5
# banane = 999999
# print("Punti:", punti)
# print("Banane:", banane)

# print("scherzetto")
punti = pickle.load(open("punti.dat", "rb"))
banane = pickle.load(open("banane.dat","rb"))

print("Punti:", punti)
print("Banane:", banane)





