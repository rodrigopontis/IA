from map import Position, Map
from robot import *
from time import time

class Bin:
    value = "B"
    collectedItems = []
    itemsToCollect = []

    def __init__(self, position):
        self.position = position

    def collectItem(self, item):
        if item:
            self.collectedItems.append(item)
        
    def setItemsToCollect(self, items):
        self.itemsToCollect = items


    def printItems(self):
        aux = []

        for item in self.collectedItems:
            aux.append(item.position.toArray())

        print(aux)

class Mundo:
    # qtd lixo
    recyclable = 5
    garbage = 10
    bin = Bin(Position(19, 19))

    def __init__(self):
        self.agent = AgentBasedInRewards("garibo", Position(0, 0), "right")
        self.map = Map(20, 20, self.agent)
        self.agent.addMap(self.map)
        self.agent.setBin(self.bin)
        self.map.setBin(self.bin)
        self.map.positionItems()

    def robotSimpleMovement(self):
        cronStart = time()

        self.map.printMap()
        # self.map.printItems()
        self.moveAgent()
        self.map.printItems()
        self.bin.printItems()

        cronEnd = time()

        return (cronEnd - cronStart)

    def moveAgent(self):
        self.agent.isStopped = False
        self.agent.searchObjective()

        while len(self.bin.collectedItems) < 15:
        # while self.agent.isStopped != True:
            self.agent.move()

    def start(self):
        tempo = self.robotSimpleMovement()

        print(f'\nTempo de execução: {tempo:,.2f}')
