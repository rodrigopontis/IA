import os
import random

def return_zero():
    print('Starting function return_zero()...')
    return 0


class Position:
    def __init__(self, row, column):
        self.row = row
        self.column = column

class Robo:
    value = "R"
    inTrashPosition = False
    holdingItem = ""
    memory = []

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def agent_simples():
        print("agente simples")

    def move(self, position):
        self.position = position

    def checkPosition(self, value):
        print("Checking position", value)

        if(value == "L"):
            print("Trash position")
            self.inTrashPosition = True


class Mapa:
    matrix = []

    def __init__(self, position):
        self.row = position.row
        self.column = position.column
        self.matrix = [["-" for x in range(self.row)]
                       for y in range(self.column)]

    def positionValue(self, position):
        return self.matrix[position.row][position.column]
    
    def printMapa(self):
        print("Matriz: \n")
        for term in self.matrix:
            print(term)

    def moveRobot(self, position, robo):
        if(robo.inTrashPosition != True):
            self.removeRobot(robo)
            self.addRobot(position, robo)

            robo.move(position)
            robo.checkPosition(self.matrix[position.row][position.column])
            
            if(robo.inTrashPosition):
                print("Chegou no lixo")

    def simpleMoveRobot(self, robo):
      #começando do [0][0]  
        os.system("cls")
        self.printMapa()
        if(robo.inTrashPosition == False):
            while(robo.position.row < self.row-1):
                self.moveRobot(Position(robo.position.row+1,robo.position.column), robo)

            if(robo.inTrashPosition == False):
                os.system("cls")
                self.printMapa()

            if(robo.position.column + 1 < self.column):
                self.moveRobot(Position(robo.position.row, robo.position.column+1), robo)

            if(robo.inTrashPosition == False):
                os.system("cls")
                self.printMapa()

            while(robo.position.row > 0 and robo.inTrashPosition == False):
                self.moveRobot(Position(robo.position.row-1,robo.position.column), robo)
            
            if(robo.inTrashPosition == False):
                os.system("cls")
                self.printMapa()

            if(robo.position.column + 1 < self.column):
                self.moveRobot(Position(robo.position.row, robo.position.column+1), robo)
        else:
            # Sair da lixeira
            # ir para o primeiro
            # item da memoria
            print("Chegou na lixeira")
    
    def addRobot(self, position, robo):
        self.matrix[position.row][position.column] = robo.value

    def removeRobot(self, robo):
        if(self.matrix[robo.position.row][robo.position.column] == "G" and self.matrix[robo.position.row][robo.position.column] == "L"):
            print("Lixo coletado")
        else: 
            self.matrix[robo.position.row][robo.position.column] = "x"

    def addTrash(self, position):
        self.matrix[position.row][position.column] = "T"

    def addGarbage(self, position):
        self.matrix[position.row][position.column] = "G"

    def addRecyclable(self, position):
        self.matrix[position.row][position.column] = "L"
        
    def positionItems(self):
        random.seed(0)
        for i in range(10):
            self.addGarbage(Position(random.randint(0, 19), random.randint(0, 19)))

        for i in range(5):
            self.addRecyclable(Position(random.randint(0, 19), random.randint(0, 19)))
            
class Mundo:
    recyclable = 5
    garbage = 10

    def __init__(self):
        self.agente = Robo("robo", Position(0, 0))
        self.mapa = Mapa(Position(20, 20))
        self.mapa.addRobot(Position(0, 0), self.agente)
        self.mapa.addTrash(Position(19, 19))
        self.mapa.positionItems()

    def robotSimpleMovement(self):
        self.mapa.printMapa()

        while(self.recyclable + self.garbage > 0):
            self.mapa.simpleMoveRobot(self.agente)
        #for i in range(100000):
          #self.mapa.addBin(0)

    
    def start(self):
        self.robotSimpleMovement()

##################################################### RODANDO O PROJETO ################################################
mundo = Mundo()

mundo.start()
