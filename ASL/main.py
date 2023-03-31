import os


def return_zero():
    print('Starting function return_zero()...')
    return 0


class Position:
    def __init__(self, row, column):
        self.row = row
        self.column = column


class Robo:
    value = 1
    inTrashPosition = False

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def agent_simples():
        print("agente simples")

    def move(self, position):
        self.position = position

    def checkPosition(self, position):
        if(position==Position(19,19)):
            self.inTrashPosition = True


class Mapa:
    matrix = []

    def __init__(self, position):
        self.row = position.row
        self.column = position.column
        self.matrix = [[0 for x in range(self.row)]
                       for y in range(self.column)]

    def positionValue(self, position):
        return self.matrix[position.row][position.column]
    
    def printMapa(self):
        print("Matriz: \n")
        for term in self.matrix:
            print(term)

    def moveRobot(self, position, robo):
        self.removeRobot(robo)
        self.addRobot(position, robo)
        robo.move(position)
        robo.checkPosition(position)
        if(robo.inTrashPosition):
          print("Chegou no lixo")

    def simpleMoveRobot(self, robo):
      #começando do [0][0]  
        
        while(robo.position.row < self.row-1):
            self.moveRobot(Position(robo.position.row+1,robo.position.column), robo)

        self.moveRobot(Position(robo.position.row, robo.position.column+1), robo)
        if(robo.inTrashPosition == True):
            return "chegou"

        while(robo.position.row > 0 ):
            self.moveRobot(Position(robo.position.row-1,robo.position.column), robo)
        
        self.moveRobot(Position(robo.position.row, robo.position.column+1), robo)

    def addRobot(self, position, robo):
        self.matrix[position.row][position.column] = robo.value

    def removeRobot(self, robo):
        self.matrix[robo.position.row][robo.position.column] = 0

    def addTrash(self, value):
        self.matrix[19][19] = value

    def addBin(self, value):
        self.matrix[0][0] = value


class Mundo:
    def __init__(self):
        self.agente = Robo("robo", Position(0, 0))
        self.mapa = Mapa(Position(20, 20))
        self.mapa.addRobot(Position(0, 0), self.agente)
        self.mapa.addTrash(3)

    def robotSimpleMovement(self):
      while(self.mapa.simpleMoveRobot(self.agente) != 'chegou'):
        self.mapa.simpleMoveRobot(self.agente)
        self.mapa.printMapa()

        
        #for i in range(100000):
          #self.mapa.addBin(0)
    def start(self):
        self.robotSimpleMovement()

        ############################################### RODANDO O PROJETO ################################################


mundo = Mundo()

mundo.start()
