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

    def clear(self):
        self.collectedItems = []

    def printItems(self):
        aux = []

        for item in self.collectedItems:
            aux.append([item.position.toArray(), item.value])

        print(aux)

class Mundo:
    bin = Bin(Position(19, 19))

    def __init__(self):
        self.map = Map(20, 20)
        self.map.setBin(self.bin)
    
    def setup(self):
        self.map.positionItems()
        self.bin.clear()

    # em media 37 segundos
    def simpleAgent(self):
        self.setup()

        cronStart = time()

        agent = SimpleAgent("garibo", Position(0, 0), "right")
        self.map.setAgent(agent)

        agent.addMap(self.map)
        agent.setBin(self.bin)

        self.map.printMap()

        agent.isStopped = False
        while len(self.bin.collectedItems) < 15:
            agent.move()
        
        self.map.printItems()
        self.bin.printItems()

        cronEnd = time()

        agent = None
        return (cronEnd - cronStart)

    def modelBasedAgent(self):
        print("agente baseado em modelo")

    # em media 10 segundos
    def objectiveBasedAgent(self):
        self.setup()

        cronStart = time()

        agent = AgentBasedInObjective("garibo", Position(0, 0), "right")
        self.map.setAgent(agent)

        agent.addMap(self.map)
        agent.setBin(self.bin)

        self.map.printMap()

        agent.isStopped = False
        while len(self.bin.collectedItems) < 15:
            agent.move()
        
        self.map.printItems()
        self.bin.printItems()

        cronEnd = time()

        agent = None
        return (cronEnd - cronStart)

    def rewardBasedAgent(self):
        print("agente baseado em recompensa")

    def start(self):

        menu = -1
        while(menu != 0):
            menu = int(input("Escolha um agente para realizar o teste: \n1: Simples \n2: Baseado em modelo \n3: Baseado em objetivo \n4: Baseado em recompensa \nEscolha uma opção ou digite 0 para sair: "))
            print()

            if(menu == 1):
                tempo = self.simpleAgent()
                print(f'\nTempo de execução: {tempo:,.2f}')
            elif(menu == 2):
                tempo = self.modelBasedAgent()
                # print(f'\nTempo de execução: {tempo:,.2f}')
            elif(menu == 3):
                tempo = self.objectiveBasedAgent()

                print(f'\nTempo de execução: {tempo:,.2f}\n')
            elif(menu == 4):
                tempo = self.rewardBasedAgent()
                # print(f'\nTempo de execução: {tempo:,.2f}')
            else:
                print("Selecione uma opção válida ou digite 0 para sair...\n")

        print("Até logo!")
