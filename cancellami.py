class Sprite:
    """NUOVO SPRITE ASGARRA
    argomenti: x, y, velocità"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def printaggio(self):
        print(self.x, self.y)

class Spada(Sprite):
    def imposta_materiale(self, materiale):
        self.materiale = materiale

class Pugnale(Spada):
    def imposta_danno(self, danno):
        self.danno = danno
    

A = Sprite(1,2)
A.printaggio()

B = Spada(2,3)
B.imposta_materiale("banana")
B.printaggio()
print(B.materiale)