import random


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

    def getPosition(self):
        return self.position

    def recyclable(self):
        self.value = "V"


class Map:
    matrix = []
    garbageItems = []

    def __init__(self, row, column, robot):
        self.row = row
        self.column = column
        self.robot = robot

    def setBin(self, bin):
        self.bin = bin

    def positionItems(self):
        g1 = CollectableObject(Position(1, 19))
        self.garbageItems.append(g1)

    def stringContent(self, position):
        return self.matrix[position.row][position.column]

    def content(self, position):
        for garbage in self.garbageItems:
            if garbage.position.toArray() == position.toArray():
                return garbage

    def printMap(self):
        print("\nMatrix:")
        self.matrix = [["-" for x in range(self.row)] for y in range(self.column)]

        self.matrix[self.bin.position.row][self.bin.position.column] = self.bin.value

        self.matrix[self.robot.position.row][
            self.robot.position.column
        ] = self.robot.value
        for garbage in self.garbageItems:
            self.matrix[garbage.position.row][garbage.position.column] = garbage.value

        for term in self.matrix:
            print(term)

    def collectItem(self, item):
        for garbage in self.garbageItems:
            if item == garbage:
                self.garbageItems.remove(garbage)

    def isAValidPosition(self, position):
        if position.row < 0 or position.row >= self.row:
            return False
        if position.column < 0 or position.column >= self.column:
            return False

        return True
