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
        target = self.contentInNeighborhood[0]
        self.moveToDirection(self.positionToDirection(target))
        
        if(self.holdingItem):
            self.moveToBin()

        self.stop()

    def pickItem(self):
        if(self.holdingItem):
            print("mão cheia")
        else:
            print("pegar item", self.contentInPlace)
            item = self.contentInPlace
            
            self.holdingItem = item
            self.map.collectItem(item)

    def dropItem(self):
        self.bin.collectItem(self.holdingItem)
        self.holdingItem = None
        self.contentInNeighborhood = []

    def moveUp(self):
        newPosition = Position(self.position.row - 1, self.position.column)

        if self.map.isAValidPosition(newPosition):
            self.direction = "up"
            self.position = newPosition

            contentInPlace = self.map.content(self.position)
            self.contentInPlace = contentInPlace
            if(contentInPlace != None):
                self.pickItem()

            self.map.printMap()
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
                self.pickItem()

            self.map.printMap()
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
                self.pickItem()

            self.map.printMap()
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
                self.pickItem()

            self.map.printMap()
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
        if(self.position.column < 19):
            while(self.position.row < 19):
                self.moveDown()

            while(self.position.column < 18):
                self.moveRight()
        elif self.position.column == 19:
            while(self.position.row < 18):
                self.moveDown()
        
        if(self.inBinPosition()):
            self.dropItem()

    def inBinPosition(self):
        if(self.position.column == 18 and self.position.row == 19):
            return True
        if(self.position.row == 18):
            if(self.position.column == 18 or self.position.column == 19):
                return True
            
        return False

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

class SimpleAgent(Robot): 
    def __init__(self,name, position, direction):
        super().__init__(name, position, direction)

    
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
        
    
    def lookAround(self):
        directions = self.getDirections()

        for value in directions.values():
            if(self.map.isAValidPosition(value)):
                content = self.map.content(value)
                if(content != None and self.holdingItem == None):
                    self.contentInNeighborhood.append(content)
                    self.stop()

class AgentBasedInModel(Robot):
    itemsToCollect = []

    def __init__(self,name, position, direction):
        super().__init__(name, position, direction)
    
    def move(self):
        self.isStopped = False

        self.lookAround()

        if len(self.itemsToCollect) == 0:
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
            self.collectFromModel()
    
    def collectFromModel(self):
        self.moveToItem(self.itemsToCollect[0])

        if(self.holdingItem):
            self.moveToBin()
            if(self.inBinPosition()):
                self.dropItem()

        self.stop()

    def moveToItem(self, item):
        row = item.position.row - self.position.row
        column = item.position.column - self.position.column

        while self.holdingItem == None:
            # North or up
            if(row < 0 and column == 0):
                for i in range(row * -1):
                    self.moveUp()

            # West or left
            if(row == 0 and column < 0):
                for i in range(column * -1):
                    self.moveLeft()
            # East or right
            if(row == 0 and column > 0):
                for i in range(column):
                    self.moveRight()

            # South or down
            if(row > 0 and column == 0):
                for i in range(row):
                    self.moveDown()

            # SE
            if row > 0 and column > 0:
                for i in range (column):
                    print(i)
                    self.moveRight()
                
                for i in range(row):
                    print(i)
                    self.moveDown()
        
            # NW
            if(row < 0 and column < 0):
                for i in range(column * -1):
                    self.moveLeft()
                
                for i in range(row * -1):
                    self.moveUp() 

            # Sw
            if(row > 0 and column < 0):
                for i in range(column * -1):
                    self.moveLeft()
                
                for i in range(row):
                    self.moveDown()

            # SE
            if(row < 0 and column > 0):
                for i in range(column):
                    self.moveRight()

                for i in range(row * -1):
                    self.moveUp()

        self.stop()

    def moveToBin(self):
        if(self.position.column < 19):
            while(self.position.row < 19):
                self.lookAround()
                self.moveDown()

            while(self.position.column < 18):
                self.lookAround()
                self.moveRight()
        elif self.position.column == 19:
            while(self.position.row < 18):
                self.lookAround()
                self.moveDown()
        
        if(self.inBinPosition()):
            self.dropItem()
    
    def dropItem(self):
        for i in self.itemsToCollect:
            if i == self.holdingItem:
                self.itemsToCollect.remove(i)

        self.bin.collectItem(self.holdingItem)

        self.holdingItem = None
        self.contentInNeighborhood = []

    def lookAround(self):
        directions = self.getDirections()

        for value in directions.values():
            if(self.map.isAValidPosition(value)):
                content = self.map.content(value)
                if(content != None):
                    self.contentInNeighborhood.append(content)
                    self.itemsToCollect.append(content)
                    self.itemsToCollect = list(set(self.itemsToCollect))

                    self.stop()

class AgentBasedInObjective(AgentBasedInModel):
    def __init__(self,name, position, direction):
        super().__init__(name, position, direction)

    def searchObjective(self):
        self.itemsToCollect = self.map.getItems()

    def move(self): 
        self.searchObjective()

        if(self.holdingItem == None):
            self.collectFromObjective()
    
    def collectFromObjective(self):
        self.moveToItem(self.itemsToCollect[0])

        if(self.holdingItem != None):
            self.moveToBin()
            if(self.inBinPosition()):
                print("dropar item", self.holdingItem)
                self.dropItem() 

        self.stop()