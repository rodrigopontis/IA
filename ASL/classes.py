import os
import random
from typing import overload


def return_zero():
    print("Starting function return_zero()...")
    return 0


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


class Trash:
    def __init__(self, position):
        self.position = position


class Robo:
    value = "R"
    inTrashPosition = False
    position = Position(0, 0)
    contentInPlace = " "
    contentInNeighborhood = []
    trashPlace = Position(19, 19)
    holdingItem = "-"
    lookingItem = "-"
    canMove = True
    isCollecting = False
    directionRobot = ""

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def agent_simples():
        print("agente simples")

    def checkPosition(self, position, content):
        if position == self.trashPlace:
            self.dropGarbage()

        if content != "-" and self.isCollecting != True:
            self.lookingItem = content
            self.stop()
            return position

    # Movimento Robo

    def moveRight(self):
        if self.position.column < 20 and self.canMove == True:
            newPosition = Position(self.position.row, self.position.column + 1)
            self.position = newPosition
            self.directionRobot = "rigth"

            return newPosition
        else:
            return self.position

    def moveLeft(self):
        if self.position.column >= 0 and self.canMove == True:
            newPosition = Position(self.position.row, self.position.column - 1)
            self.position = newPosition
            self.directionRobot = "left"

            return newPosition
        else:
            return self.position

    def moveUp(self):
        if self.position.row >= 0 and self.canMove == True:
            newPosition = Position(self.position.row - 1, self.position.column)
            self.position = newPosition
            self.directionRobot = "up"

            return newPosition
        else:
            return self.position

    def moveDown(self):
        if self.position.row < 20 and self.canMove == True:
            newPosition = Position(self.position.row + 1, self.position.column)
            self.position = newPosition
            self.directionRobot = "down"

            return newPosition
        else:
            return self.position

    def stop(self):
        self.canMove = False

    def collecting(self):
        self.isCollecting = True
        self.canMove = True

    def lookAround(self, mapa):
        se = Position(mapa.robotPosition.row+1, mapa.robotPosition.column+1)
        if (mapa.isAValidPosition(se.row, se.column)):
            self.contentInNeighborhood.append(se)

    # Pegar Teles

    def pickGarbage(self, garbage):
        # se mao estiver vazia
        if self.holdingItem == "-":
            self.holdingItem = garbage
            print("cata lixo", garbage)

    def dropGarbage(self):
        if self.holdingItem != "-":
            self.inTrashPosition = True
            self.holdingItem = "-"
            self.isCollecting = False
            print("jogando lixo na lixeira")
        else:
            print("nao sujar o chão")


class Mapa:
    matrix = []

    def __init__(self, position, robotPosition):
        self.row = position.row
        self.column = position.column
        self.robotPosition = robotPosition
        self.matrix = [["-" for x in range(self.row)]
                       for y in range(self.column)]
        self.matrix[robotPosition.row][robotPosition.column] = "R"

    def positionValue(self, position):
        return self.matrix[position.row][position.column]

    def content(self, position):
        content = self.matrix[position.row][position.column]
        if (content != "-"):
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
            print(robo.contentInNeighborhood)
            for i in robo.contentInNeighborhood:
                if (i != "-"):
                    robo.stop()
                    return i

            # # PARA CIMA
            # if self.isAValidPosition(robo.position.row - 1, robo.position.column):
            #     newPosition = Position(robo.position.row - 1, robo.position.column)
            #     item = robo.checkPosition(
            #         newPosition, self.matrix[newPosition.row][newPosition.column]
            #     )
            # # PARA BAIXO
            # if self.isAValidPosition(robo.position.row + 1, robo.position.column):
            #     newPosition = Position(robo.position.row + 1, robo.position.column)
            #     item = robo.checkPosition(
            #         newPosition, self.matrix[newPosition.row][newPosition.column]
            #     )
            # # PRA ESQUERDA
            # if self.isAValidPosition(robo.position.row, robo.position.column - 1):
            #     newPosition = Position(robo.position.row, robo.position.column - 1)
            #     item = robo.checkPosition(
            #         newPosition, self.matrix[newPosition.row][newPosition.column]
            #     )
            # # PARA DIREITA
            # if self.isAValidPosition(robo.position.row, robo.position.column + 1):
            #     newPosition = Position(robo.position.row, robo.position.column + 1)
            #     item = robo.checkPosition(
            #         newPosition, self.matrix[newPosition.row][newPosition.column]
            #     )
            # # NW
            # if self.isAValidPosition(robo.position.row - 1, robo.position.column - 1):
            #     newPosition = Position(robo.position.row - 1, robo.position.column - 1)
            #     item = robo.checkPosition(
            #         newPosition, self.matrix[newPosition.row][newPosition.column]
            #     )
            # # NE
            # if self.isAValidPosition(robo.position.row - 1, robo.position.column + 1):
            #     newPosition = Position(robo.position.row - 1, robo.position.column + 1)
            #     item = robo.checkPosition(
            #         newPosition, self.matrix[newPosition.row][newPosition.column]
            #     )
            # # SW
            # if self.isAValidPosition(robo.position.row + 1, robo.position.column - 1):
            #     newPosition = Position(robo.position.row + 1, robo.position.column - 1)
            #     item = robo.checkPosition(
            #         newPosition, self.matrix[newPosition.row][newPosition.column]
            #     )
            # # SE
            # if self.isAValidPosition(robo.position.row + 1, robo.position.column + 1):
            #     newPosition = Position(robo.position.row + 1, robo.position.column + 1)
            #     item = robo.checkPosition(
            #         newPosition, self.matrix[newPosition.row][newPosition.column]
            #     )

            # if(item == "G" or item == "L"):
            #     return item

    def moveRobot(self, position, robo):
        if self.isAValidPosition(position.row, position.column):
            self.removeRobot()
            item = self.addRobot(position, robo)
            if (item != "-"):
                robo.pickGarbage(item)
            self.setRobotPerceptions(robo)
        else:
            print("movimento invalido")

    def collectGarbage(self, robo, garbagePosition):

        print("posicao garbage:", garbagePosition)
        if (self.matrix[garbagePosition.row][garbagePosition.column] != "-"):
            self.moveRobotToGarbage(robo, garbagePosition)

    def moveRobotToGarbage(self, robo, garbagePosition):
        # SW
        if garbagePosition.toArray() == [robo.position.row + 1, robo.position.column + 1]:
            robo.collecting()
            right = robo.moveRight()
            self.moveRobot(right, robo)

            down = robo.moveDown()
            self.moveRobot(down, robo)

    def takeRobotToGarbage(self, robo):
        while self.robotPosition.row < 19:
            down = robo.moveDown()
            self.moveRobot(down, robo)

        while self.robotPosition.column < 19 - 1:
            right = robo.moveRight()
            self.moveRobot(right, robo)

        robo.dropGarbage()

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

    def positionItems(self):
        random.seed(0)
        for i in range(10):
            self.addGarbage(
                Position(random.randint(0, 19), random.randint(0, 19)))

        for i in range(5):
            self.addRecyclable(
                Position(random.randint(0, 19), random.randint(0, 19)))


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
            self.mapa.printMapa()

        if (self.agente.canMove != True):
            self.mapa.collectGarbage(self.agente)
            self.mapa.printMapa()

        # self.mapa.takeRobotToGarbage(self.agente)
        # print(self.agente.directionRobot)
        # self.mapa.printMapa()

        # print(self.agente.canMove)

        # while self.agente.canMove:
        #     up = self.agente.moveUp()
        #     self.mapa.moveRobot(up, self.agente)

            # self.mapa.printMapa()

        # self.mapa.takeRobotToGarbage(self.agente)
        print(self.agente.directionRobot)
        self.mapa.printMapa()

    def start(self):
        self.robotSimpleMovement()
