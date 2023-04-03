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


class Mapa:
    matrix = []

    def __init__(self, position, robotPosition):
        self.row = position.row
        self.column = position.column
        self.robotPosition = robotPosition
        self.matrix = [["-" for x in range(self.row)] for y in range(self.column)]
        self.matrix[robotPosition.row][robotPosition.column] = "R"
        self.itemToCollect = Position(0,0)

    def positionValue(self, position):
        return self.matrix[position.row][position.column]

    def content(self, position):
        content = self.matrix[position.row][position.column]
        if content != "-":
            return CollectableObject(position)

    def printMapa(self):
        print("Matrix: \n")
        for term in self.matrix:
            print(term)

    def setRobotPerceptions(self, robo):
        if robo.holdingItem != "-":
            return
        else:
            robo.lookAround(self)

    def moveRobot(self, position, robo):
        if self.isAValidPosition(position.row, position.column):
            self.removeRobot()
            item = self.addRobot(position, robo)
            self.printMapa()
            if item != "-":
                robo.pickGarbage(item)
                robo.stop()

            self.setRobotPerceptions(robo)
        else:
            print("movimento invalido")
            robo.undoMove(self.robotPosition)

    def collectGarbage(self, robo, position):
        robo.collecting()
        if robo.directionRobot == "right":
            if robo.direction(position) == "se":
                right = robo.moveRight()
                print(right.toArray())
                self.moveRobot(right, robo)

                print(robo.canMove)
                down = robo.moveDown()
                print(robo.canMove)
                self.moveRobot(down, robo)

    def moveRobotToBin(self, robo):
        if(robo.holdingItem != "-"):
            robo.move()
            if(robo.direction == "down" or robo.direction == "right"):  
                if(self.robotPosition.column == 19): 
                    while(self.robotPosition.row < 18):
                        down = robo.moveDown()
                        self.moveRobot(down, robo)
                else:
                    while(self.robotPosition.row < 19):
                        down = robo.moveDown()
                        self.moveRobot(down, robo)

                if(self.robotPosition.row == 19): 
                    while(self.robotPosition.column < 18):
                        right = robo.moveRight()
                        self.moveRobot(right, robo)
                else:
                    while(self.robotPosition.column < 19):
                        right = robo.moveRight()
                        self.moveRobot(right, robo)
                    

            robo.dropGarbage()
            robo.stop()

    def isAValidPosition(self, row, column):
        if row < 0 or row >= self.row:
            return False
        elif column < 0 or column >= self.column:
            return False

        return True

    def addRobot(self, position, robo):
        item = self.matrix[position.row][position.column]

        self.robotPosition = position
        self.matrix[position.row][position.column] = robo.value

        return item

    def removeRobot(self):
        self.matrix[self.robotPosition.row][self.robotPosition.column] = "-"

    def addTrash(self, position):
        self.matrix[position.row][position.column] = "T"

    def addGarbage(self, position):
        newGarbage = CollectableObject(position)
        self.matrix[position.row][position.column] = newGarbage.value

    def addRecyclable(self, position):
        newRecyclable = CollectableObject(position)
        self.matrix[position.row][position.column] = newRecyclable.recyclable()

    def addItemToCollect(self, robo, direction):
        self.itemToCollect = direction
        if(robo.isCollecting != True):
            robo.stop()

    def positionItems(self):
        random.seed(0)
        for i in range(10):
            self.addGarbage(Position(random.randint(0, 19), random.randint(0, 19)))

        for i in range(5):
            self.addRecyclable(Position(random.randint(0, 19), random.randint(0, 19)))
