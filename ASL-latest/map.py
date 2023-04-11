import random
import os
import time

class Position:
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def toArray(self):
        return [self.row, self.column]

class CollectableObject:
    value = "G"

    def __init__(self, position):
        self.position = position
    
    def __eq__(self, comp):
        if comp != None:
            return self.position == comp.position

        return None
    
    def __lt__(self, comp):
        if comp != None:
            return self.position < comp.position
        
        return None

    def __hash__(self):
        return hash((self.value, self.position))

    def getPosition(self):
        return self.position

    def recyclable(self):
        self.value = "V"

class Map:
    matrix = []
    garbageItems = []

    def __init__(self, row, column):
        self.row = row
        self.column = column

    def setBin(self, bin):
        self.bin = bin

    def setAgent(self, robot):
        self.robot = robot

    def positionItems(self):
        #Organic 10
        g1 = CollectableObject(Position(1, 6))
        self.garbageItems.append(g1)
        
        g2 = CollectableObject(Position(2, 18))
        self.garbageItems.append(g2)

        g3 = CollectableObject(Position(3, 7))
        self.garbageItems.append(g3)

        g4 = CollectableObject(Position(6, 15))
        self.garbageItems.append(g4)

        g5 = CollectableObject(Position(7, 2))
        self.garbageItems.append(g5)
        g6 = CollectableObject(Position(9, 9))
        self.garbageItems.append(g6)

        g7 = CollectableObject(Position(13, 2))
        self.garbageItems.append(g7)

        g8 = CollectableObject(Position(14, 9))
        self.garbageItems.append(g8)

        g9 = CollectableObject(Position(16, 12))
        self.garbageItems.append(g9)

        g10 = CollectableObject(Position(18, 15))
        self.garbageItems.append(g10)

        #Recyclable 5
        g11 = CollectableObject(Position(1, 2))
        g11.recyclable()
        self.garbageItems.append(g11)

        g12 = CollectableObject(Position(5, 18))
        g12.recyclable()
        self.garbageItems.append(g12)

        g13 = CollectableObject(Position(12, 7))
        g13.recyclable()
        self.garbageItems.append(g13)

        g14 = CollectableObject(Position(8, 9))
        g14.recyclable()
        self.garbageItems.append(g14)
        
        g15 = CollectableObject(Position(19, 13))
        g15.recyclable() 
        self.garbageItems.append(g15)
        
    def getItems(self):
        return self.garbageItems

    def stringContent(self, position):
        return self.matrix[position.row][position.column]

    def content(self, position):
        for garbage in self.garbageItems:
            if garbage.position.toArray() == position.toArray():
                return garbage

    def printMap(self):
        time.sleep(0.1)
        os.system("cls")
        print("\nMatrix:")
        self.matrix = [["-" for x in range(self.row)] for y in range(self.column)]

        for garbage in self.garbageItems:
            self.matrix[garbage.position.row][garbage.position.column] = garbage.value
        
        self.matrix[self.bin.position.row][self.bin.position.column] = self.bin.value

        self.matrix[self.robot.position.row][
            self.robot.position.column
        ] = self.robot.value

        for term in self.matrix:
            print(term)
            
        print("\nQuantidade de lixo coletado:", len(self.bin.collectedItems))
        print()
        print("Comum:", self.bin.comum)
        print("Reciclavel:", self.bin.rec)


    def collectItem(self, item):
        for garbage in self.garbageItems:
            if item == garbage:
                self.garbageItems.remove(garbage)

    def isAValidPosition(self, position):
        if position.row < 0 or position.row >= self.row:
            return False
        if position.column < 0 or position.column >= self.column:
            return False
        if position.toArray() == self.bin.position.toArray():
            return False

        return True

    def printItems(self):
        aux = []
        for item in self.garbageItems:
            aux.append(item.position.toArray())

        print(aux) 