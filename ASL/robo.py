from mapa import Position


class Robo:
    value = "R"
    inTrashPosition = False
    position = Position(0, 0)
    contentInPlace = " "
    neighborhoodPositions = []
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

    def direction(self, position):
        if (
            position.row == self.position.row + 1
            and position.column == self.position.column + 1
        ):
            return "se"

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
            self.directionRobot = "right"

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

    def move(self):
        self.canMove = True

    def collecting(self):
        self.isCollecting = True
        self.canMove = True

    def lookAround(self, mapa):
        # North
        north = Position(mapa.robotPosition.row - 1, mapa.robotPosition.column)

        if mapa.isAValidPosition(north.row, north.column):
            self.neighborhoodPositions.append(north)
            if mapa.content(north):
                mapa.addItemToCollect(self, self, north)

        # South
        south = Position(mapa.robotPosition.row + 1, mapa.robotPosition.column)

        if mapa.isAValidPosition(south.row, south.column):
            self.neighborhoodPositions.append(south)
            if mapa.content(south):
                mapa.addItemToCollect(self, south)
        # East
        east = Position(mapa.robotPosition.row, mapa.robotPosition.column + 1)

        if mapa.isAValidPosition(east.row, east.column):
            self.neighborhoodPositions.append(east)
            if mapa.content(east):
                mapa.addItemToCollect(self, east)
        # West
        west = Position(mapa.robotPosition.row, mapa.robotPosition.column - 1)

        if mapa.isAValidPosition(west.row, west.column):
            self.neighborhoodPositions.append(west)
            if mapa.content(west):
                mapa.addItemToCollect(self, west)
        # Northeast
        ne = Position(mapa.robotPosition.row - 1, mapa.robotPosition.column + 1)

        if mapa.isAValidPosition(ne.row, ne.column):
            self.neighborhoodPositions.append(ne)
            if mapa.content(ne):
                mapa.addItemToCollect(self, ne)
        # Northwest
        nw = Position(mapa.robotPosition.row - 1, mapa.robotPosition.column - 1)

        if mapa.isAValidPosition(nw.row, nw.column):
            self.neighborhoodPositions.append(nw)
            if mapa.content(nw):
                mapa.addItemToCollect(self, nw)
        # Southeast
        se = Position(mapa.robotPosition.row + 1, mapa.robotPosition.column + 1)

        if mapa.isAValidPosition(se.row, se.column):
            self.neighborhoodPositions.append(se)
            if mapa.content(se):
                mapa.addItemToCollect(self, se)
        # Southwest
        sw = Position(mapa.robotPosition.row + 1, mapa.robotPosition.column - 1)

        if mapa.isAValidPosition(sw.row, sw.column):
            self.neighborhoodPositions.append(sw)
            if mapa.content(sw):
                mapa.addItemToCollect(self, sw)
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
