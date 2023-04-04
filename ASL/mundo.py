from map import Position, Map
from robot import Robot


class Bin:
    value = "B"
    collectedItems = []

    def __init__(self, position):
        self.position = position

    def collectItem(self, item):
        self.collectedItems.append(item)


class Mundo:
    # qtd lixo
    recyclable = 5
    garbage = 10
    bin = Bin(Position(19, 19))

    def __init__(self):
        self.agent = Robot("garibo", Position(0, 0), "right")
        self.map = Map(20, 20, self.agent)
        self.agent.addMap(self.map)
        self.agent.setBin(self.bin)
        self.map.setBin(self.bin)
        self.map.positionItems()

    def robotSimpleMovement(self):
        self.map.printMap()
        self.moveAgent()
        print(self.bin.collectedItems)

    def moveAgent(self):
        self.agent.isStopped = False
        while len(self.map.garbageItems) > 0 :
            self.agent.move()
            self.map.printMap()

    def start(self):
        self.robotSimpleMovement()
