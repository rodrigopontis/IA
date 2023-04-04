from map import Position
class Robot:
    value = "R"
    contentInPlace = None
    contentInNeighborhood = []
    holdingItem = None
    binPosition = Position(19,19)

    def __init__(self, name, position, direction):
        self.name = name
        self.position = position
        self.direction = direction
        print("hello world! my name is", self.name)
        self.isStopped = True

    def addMap(self, map):
        self.map = map

    def setBin(self, bin):
        self.bin = bin

    def move(self):
        self.isStopped = False

        self.lookAround()

        if(len(self.contentInNeighborhood) == 0):
            if self.direction == "up":
                self.moveUp()
            elif self.direction == "down":
                self.moveDown()
            elif self.direction == "left":
                self.moveLeft()
            elif self.direction == "right":
                self.moveRight()
            else:
                print("Invalid position")
                self.stop()
        else:
            self.collect()
        
    def crash(self, direction):
        if direction == "right":
            if self.position.row == 19 and self.position.column == 18:
                self.moveUp()
            else:
                self.moveDown()
                self.moveLeft()


        if direction == "left":
            if self.position.row != 19:
                self.moveDown()
                self.moveRight()
            else:
                self.moveUp()

        if direction == "up":
            self.moveRight()

        if direction == "down":
            if(self.position.column == 19):
                self.moveLeft()
            else:
                self.moveRight()
    
    def collect(self):
        self.pickItem()
        self.moveToBin()

        self.dropItem()

        self.stop()

    def pickItem(self):
        target = self.contentInNeighborhood[0]
        self.moveToDirection(self.positionToDirection(target))
        self.contentInNeighborhood = []

    def dropItem(self):
        self.bin.collectItem(self.holdingItem)
        self.holdingItem = None

    def moveUp(self):
        newPosition = Position(self.position.row - 1, self.position.column)

        if self.map.isAValidPosition(newPosition):
            self.direction = "up"
            self.position = newPosition

            contentInPlace = self.map.content(self.position)
            self.contentInPlace = contentInPlace
            if(contentInPlace != None):
                self.map.collectItem(contentInPlace)

            return newPosition
        else:
            self.crash("up")

    def moveDown(self):
        newPosition = Position(self.position.row + 1, self.position.column)

        if self.map.isAValidPosition(newPosition):
            self.direction = "down"
            self.position = newPosition

            contentInPlace = self.map.content(self.position)
            self.contentInPlace = contentInPlace
            if(contentInPlace != None):
                self.map.collectItem(contentInPlace)

            return newPosition
        else:
            self.crash("down")

    def moveLeft(self):
        newPosition = Position(self.position.row, self.position.column - 1)

        if self.map.isAValidPosition(newPosition):
            self.direction = "left"
            self.position = newPosition

            contentInPlace = self.map.content(self.position)
            self.contentInPlace = contentInPlace
            if(contentInPlace != None):
                self.map.collectItem(contentInPlace)

            return newPosition
        else:
            print("bateu")
            self.crash("left")

    def moveRight(self):
        newPosition = Position(self.position.row, self.position.column + 1)

        if self.map.isAValidPosition(newPosition) and newPosition.column < 19:
            self.direction = "right"
            self.position = newPosition

            contentInPlace = self.map.content(self.position)
            self.contentInPlace = contentInPlace
            if(contentInPlace != None):
                self.map.collectItem(contentInPlace)

            return newPosition
        else:
            print("bateu")
            self.crash("right")

    def moveToDirection(self, direction):
        if direction == "north":
            self.moveUp()

        elif direction == "south":
            self.moveDown()

        elif direction == "east":
            self.moveRight()

        elif direction == "west":
            self.moveLeft()
        
        elif direction == "southeast":
            self.moveDown()
            self.moveRight()
        
        elif direction == "southwest":
            self.moveDown()
            self.moveLeft()
        
        elif direction == "northwest":
            self.moveUp()
            self.moveLeft()
        
        elif direction == "northeast":
            self.moveUp()
            self.moveRight()
        
    def moveToBin(self):
        if(self.position.column < 18):
            while(self.position.row < 19):
                self.moveDown()

            while(self.position.column < 18):
                self.moveRight()
        elif self.position.column == 19:
            while(self.position.row < 18):
                self.moveDown()

    def inBinPosition(self):
        if(self.position.column == 18 and self.position.row == 19):
            return True
        if(self.position.row == 18):
            if(self.position.column == 18 or self.position.column == 19):
                return True
            
        return False

    def lookAround(self):
        directions = self.getDirections()

        for value in directions.values():
            if(self.map.isAValidPosition(value)):
                content = self.map.content(value)
                if(content != None and self.holdingItem == None):
                    self.contentInNeighborhood.append(content)
                    self.stop()

    def positionToDirection(self, item):
        directions = self.getDirections()

        for key in directions.keys():
            if(directions[key].toArray() == item.position.toArray()):
                return key

    def getDirections(self):
        return {
            "north": Position(self.position.row - 1, self.position.column),
            "south": Position(self.position.row + 1, self.position.column),
            "east": Position(self.position.row, self.position.column + 1),
            "west": Position(self.position.row, self.position.column - 1),
            "northeast":Position(self.position.row - 1, self.position.column + 1),
            "northwest": Position(self.position.row - 1, self.position.column - 1),
            "southeast": Position(self.position.row + 1, self.position.column + 1),
            "southwest": Position(self.position.row + 1, self.position.column - 1),
        }

    def stop(self):
        self.position = self.position
        self.isStopped = True
