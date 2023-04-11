from map import Position, Map
from robot import *
from time import time

class Bin:
    value = "B"
    collectedItems = []
    comum = 0
    rec = 0
    itemsToCollect = []

    def __init__(self, position):
        self.position = position

    def collectItem(self, item):
        if item:
            if item.value == "G":
                print("Coletando lixo comum")
                self.comum += 1
            else: 
                print("Coletando reciclavel")
                self.rec += 1
                
            self.collectedItems.append(item)
        
    def setItemsToCollect(self, items):
        self.itemsToCollect = items
        self.comum = 0
        self.rec = 0

    def clear(self):
        self.collectedItems = []
        self.comum = 0
        self.rec= 0

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
        self.setup()

        cronStart = time()

        agent = AgentBasedInModel("garibo", Position(0, 0), "right")
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
        self.setup()

        cronStart = time()

        agent = AgentBasedInRewards("garibo", Position(0, 0), "right")
        self.map.setAgent(agent)

        agent.addMap(self.map)
        agent.setBin(self.bin)

        self.map.printMap()

        agent.isStopped = False
        agent.searchObjective()
        while len(self.bin.collectedItems) < 15:
            agent.move()
        
        self.map.printItems()
        self.bin.printItems()

        cronEnd = time()

        agent = None
        return (cronEnd - cronStart)

    def start(self):

        menu = -1
        while(menu != 0):
            menu = int(input("Escolha um agente para realizar o teste: \n1: Simples \n2: Baseado em modelo \n3: Baseado em objetivo \n4: Baseado em recompensa \nEscolha uma opção ou digite 0 para sair: "))
            print()

            if(menu == 1):
                tempo = self.simpleAgent()
                print(f'\nTempo de execução: {tempo:,.2f}\n')
            elif(menu == 2):
                tempo = self.modelBasedAgent()
                print(f'\nTempo de execução: {tempo:,.2f}\n')
            elif(menu == 3):
                tempo = self.objectiveBasedAgent()

                print(f'\nTempo de execução: {tempo:,.2f}\n')
            elif(menu == 4):
                tempo = self.rewardBasedAgent()
                print(f'\nTempo de execução: {tempo:,.2f}\n')
            else:
                print("Selecione uma opção válida ou digite 0 para sair...\n")

        print("Até logo!")