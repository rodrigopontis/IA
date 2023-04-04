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
        return "V"

class Map:
    matrix = []

    def __init__(self, row, column, robot):
        self.row = row
        self.column = column
        self.robot = robot
        
    def printMap(self):
            print("\nMatrix:")
            self.matrix = [["-" for x in range(self.row)] for y in range(self.column)]
            self.matrix[self.robot.position.row][self.robot.position.column] = self.robot.value
            for term in self.matrix:
                print(term)


    def isAValidPosition(self, position):
            if position.row < 0 or position.row >= self.row:
                return False
            if  position.column < 0 or position.column >= self.column:
                return False

            return True