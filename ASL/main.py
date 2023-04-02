import os
import random

def return_zero():
    print('Starting function return_zero()...')
    return 0


class Position:
    def __init__(self, row, column):
        self.row = row
        self.column = column

class Trash:
    def __init__(self, position):
      self.position = position
    
class Robo:
    value = "R"
    inTrashPosition = False
    position = Position(0,0)
    contentInPlace = " "
    #contectInNeighborhood = 
    trashPlace = Position(19,19)
    holdingItem = " "

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def agent_simples():
        print("agente simples")

    def checkPosition(self, position, content):
      print(position)
      if(position==self.trashPlace):
        self.dropGarbage()
      if(content != "-"):
        self.pickGarbage(content)
       

    #Movimento Robo
    def moveRight(self, position):
      if(position.colunm < 20):
        self.position = position.column+1
      else:
        print("fora do limite direita")

    def moveLeft(self, position):
      if(position.colunm >= 0):
        self.position = position.colunm -1
      else:
        print("fora do limite esquerda")

    def moveUp(self, position):
      if(position.row >= 0):
        self.position = position.row-1
      else:
        print("fora do limite cima")

    def moveDown(self, position):
      if(position.row < 20):
        self.position = position.row +1
      else:
        print("fora do limite baixo")

    #Pegar Teles
    def pickGarbage(self, garbage):
      #se mao estiver vazia
      if(self.holdingItem == "-"):
        self.holdingItem = garbage
        print("cata lixo")
      else:
        print("mao cheia")
      
    def dropGarbage(self, position):
      if(self.holdingItem != "-" and Robo.position == self.trashPlace):
        self.inTrashPosition = True
        self.holdingItem = "-"
        Trash.removeGarbage(self.garbage)
        print("jogando lixo na lixeira")
      else:
        print("nao sujar o chão")
        


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
      if(self.isAValidPosition(position)):
        self.removeRobot(robo)
        self.addRobot(position, robo)
        garbage = self.matrix[position.row][position.column]
        robo.move(position)
        robo.checkPosition(position, garbage)
        if(robo.inTrashPosition):
          print("Chegou no lixo")
      else:
        print("posição invalida")

    def isAValidPosition(self, position):
      if(position.row < 0 or position.row > self.row):
        return False
      elif(position.column < 0 or position.column > self.column):
        return False
      return True

        
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
