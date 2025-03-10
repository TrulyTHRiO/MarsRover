class Plateau:
    def __init__(self, x, y):
        self.boundingRect = [0,0,int(x),int(y)] # x1, y1, x2, y2 (not x1, y1, w, h)

    rovers = []

    def CreateNewRover(self):
        info = input("Please enter the rover's starting coordinates followed by the initial direction it is facing.\n").split(" ")
        try:
            if len(info) > 3: raise Exception()
            rover = self.InitialiseRover(info[0], info[1], info[2])
            return rover
        except:
            return self.CreateNewRover()

    def InitialiseRover(self, x, y, cardinal):
        rover = Rover(x, y, cardinal, self)
        self.rovers.append(rover)
        return rover



class Rover:
    def __init__(self, x, y, cardinal, plateau):
        try:
            self.plateau = plateau
            self.coordinates = [int(x),int(y)]
            self.cardinal = ["N", "E", "S", "W"].index(cardinal.upper())
        except:
            self.Reset("Please enter the rover's starting coordinates followed by the initial direction it is facing.", False)
        
    def UpdateCoordinates(self):
        movement = input().upper().split("M")
        for instruction in movement[0:-1]:
            self.Rotate(instruction)
            if not self.Move():
                self.Reset("The rover leaves the plateau. Please enter a new starting position and movement command.", True)
                return
        self.Rotate(movement[-1])

    def Rotate(self, instruction):
        for rotation in instruction:
            if rotation == "R":
                self.cardinal += 1
            elif rotation == "L":
                self.cardinal -= 1
        self.cardinal = self.cardinal % 4
    
    def Move(self):
        match self.cardinal:
            case 0:
                self.coordinates[1] += 1
            case 1:
                self.coordinates[0] += 1
            case 2:
                self.coordinates[1] -= 1
            case 3:
                self.coordinates[0] -= 1
        return self.CheckPosition()

    def CheckPosition(self):
        if self.coordinates[0] < self.plateau.boundingRect[0] or self.coordinates[0] > self.plateau.boundingRect[2]:
            return False
        if self.coordinates[1] < self.plateau.boundingRect[1] or self.coordinates[1] > self.plateau.boundingRect[3]:
            return False
        return True
    
    def Reset(self, error, updateCoords):
        info = input(error+"\n").split(" ")
        try:
            if len(info) > 3: raise Exception()
            self.__init__(info[0], info[1], info[2], self.plateau)
            if updateCoords == True:
                self.UpdateCoordinates()
            return self
        except:
            return self.Reset(error, updateCoords)



def InitialisePlateau(out):
    info = input(out+"\n").split(" ")
    try:
        if len(info) > 2: raise Exception()
        return Plateau(info[0], info[1])
    except:
        return InitialisePlateau("Plateau coordinates must be 2 integers.")


plateau = InitialisePlateau("Please enter coordinates for the 2nd point of the plateau.")
for i in range(2):
    plateau.CreateNewRover().UpdateCoordinates()

for rover in plateau.rovers:
    print(rover.coordinates[0], rover.coordinates[1], ["N", "E", "S", "W"][rover.cardinal])