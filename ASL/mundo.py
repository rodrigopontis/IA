from map import Position, Map
from robot import Robot


class Trash:
    def __init__(self, position):
        self.position = position


class Mundo:
    # qtd lixo
    recyclable = 5
    garbage = 10

    def __init__(self):
        self.agent = Robot("garibo", Position(0, 0), "right")
        self.map = Map(20, 20, self.agent)
        self.agent.addMap(self.map)
        # self.mapa.addTrash(Position(19, 19))
        self.map.positionItems()

    def robotSimpleMovement(self):
        self.map.printMap()
        # self.moveAgent()

    def moveAgent(self):
        self.agent.isStopped = False
        while(self.agent.isStopped != True):
            self.agent.move()
            self.map.printMap()

    def start(self):
        self.robotSimpleMovement()