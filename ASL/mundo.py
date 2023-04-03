from robo import Robo
from mapa import Position, Mapa


class Trash:
    def __init__(self, position):
        self.position = position


class Mundo:
    # qtd lixo
    recyclable = 5
    garbage = 10

    def __init__(self):
        self.agente = Robo("robo", Position(0, 0))
        self.mapa = Mapa(Position(20, 20), self.agente.position)
        self.mapa.addTrash(Position(19, 19))
        self.mapa.positionItems()

    def robotSimpleMovement(self):
        self.mapa.printMapa()
        self.mapa.setRobotPerceptions(self.agente)

        while self.agente.canMove:
            right = self.agente.moveRight()
            self.mapa.moveRobot(right, self.agente)
        
            if self.mapa.itemToCollect != Position(0,0):
                self.mapa.collectGarbage(self.agente, self.mapa.itemToCollect)

            if(self.agente.holdingItem != "-"):
                self.mapa.moveRobotToBin(self.agente)
            
        
        # self.mapa.takeRobotToBin(self.agente)
        # print(self.agente.directionRobot)
        # self.mapa.printMapa()

        # print(self.agente.canMove)

        # while self.agente.canMove:
        #     up = self.agente.moveUp()
        #     self.mapa.moveRobot(up, self.agente)

        # self.mapa.printMapa()

        # self.mapa.takeRobotToGarbage(self.agente)
        self.mapa.printMapa()
        print(self.agente.holdingItem)
        print(self.agente.directionRobot)

    def start(self):
        self.robotSimpleMovement()
