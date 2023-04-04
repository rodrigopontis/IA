from map import Position


class Robot:
    value = "R"

    def __init__(self, name, position, direction):
        self.name = name
        self.position = position
        self.direction = direction
        print("hello world! my name is", self.name)
        self.isStopped = True

    def addMap(self, map):
        self.map = map

    def move(self):
        self.isStopped = False

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

    def crash(self, direction):
        if(direction == "right"):
            if self.position.row > 19:
                self.moveUp()
            else:
                self.moveDown()

            self.moveLeft()

        if(direction == "left"):
            if(self.position.row != 19):
                self.moveDown()
                self.moveRight()
            else: 
                self.moveUp()

        if(direction == "up"):
            self.moveRight()


    def moveUp(self):
        newPosition = Position(self.position.row - 1, self.position.column)

        if self.map.isAValidPosition(newPosition):
            self.direction = "up"
            self.position = newPosition
            
            return newPosition
        else:
            self.crash("up")

    def moveDown(self):
        newPosition = Position(self.position.row + 1, self.position.column)

        if self.map.isAValidPosition(newPosition):
            self.direction = "down"
            self.position = newPosition
            
            return newPosition
        else:
            self.crash("down")

    def moveLeft(self):
        newPosition = Position(self.position.row, self.position.column - 1)

        if self.map.isAValidPosition(newPosition):
            self.direction = "left"
            self.position = newPosition
            
            return newPosition
        else:
            print("bateu")
            self.crash("left")

    def moveRight(self):
        newPosition = Position(self.position.row, self.position.column + 1)

        if self.map.isAValidPosition(newPosition):
            self.direction = "right"
            self.position = newPosition

            return newPosition
        else:
            print("bateu")
            self.crash("right")
    
    def stop(self):
        self.position = self.position
        self.isStopped = True
