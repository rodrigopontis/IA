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

  def __init__(self, name, position):
    self.name = name 
    self.position = position

  def agent_simples():
    print("agente simples")

  def move(self, position):
    self.position = position



class Mapa:
  matrix = []

  def __init__(self, position):
    self.row = position.row
    self.column = position.column
    self.matrix = [[0 for x in range(self.row)] for y in range(self.column)] 

  def printMapa(self):
    print("Matriz: \n")
    for term in self.matrix:
      print(term)

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
    self.agente = Robo("robo", Position(0,0))
    self.mapa = Mapa(Position(20,20))
    self.mapa.addRobot(Position(0,0), self.agente)
    self.mapa.addTrash(3)

  def simpleMoveRobot(self):
    while(self.agente.position.row+1 < self.mapa.row):
      self.mapa.printMapa()

      self.mapa.removeRobot(self.agente)
      self.mapa.addRobot(Position(self.agente.position.row+1,0), self.agente)
      self.agente.move(Position(self.agente.position.row+1,0))

      for i in range(10000000):
        self.mapa.addBin(0)
      
    
      os.system('cls')

      

  def start(self):
    self.simpleMoveRobot()

    ############################################### RODANDO O PROJETO ################################################

mundo = Mundo()

mundo.start()