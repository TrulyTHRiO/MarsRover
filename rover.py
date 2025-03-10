class Plateau:
    def __init__(self, x, y):
        self.boundingRect = [0,0,int(x),int(y)] # x1, y1, x2, y2 (not x1, y1, w, h)

    rovers = []

    def CreateNewRover(self):
        info = input().split(" ")
        rover = self.InitialiseRover(info[0], info[1], info[2])
        return rover

    def InitialiseRover(self, x, y, cardinal):
        rover = Rover(x, y, cardinal, self)
        self.rovers.append(rover)
        return rover



class Rover:
    def __init__(self, x, y, cardinal, plateau):
        self.coordinates = [int(x),int(y)]
        self.cardinal = ["N", "E", "S", "W"].index(cardinal)
        self.plateau = plateau
        
    def UpdateCoordinates(self):
        movement = input().split("M")
        for instruction in movement[0:-1]:
            self.Rotate(instruction)
            if not self.Move():
                self.Reset("The rover leaves the plateau. Please enter a new starting position and movement command.")
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
    
    def Reset(self, error):
        info = input(error+"\n").split(" ")
        self.__init__(info[0], info[1], info[2], self.plateau)
        self.UpdateCoordinates()



def InitialisePlateau():
    info = input().split(" ")
    return Plateau(info[0], info[1])

plateau = InitialisePlateau()
for i in range(2):
    plateau.CreateNewRover().UpdateCoordinates()

for rover in plateau.rovers:
    print(rover.coordinates[0], rover.coordinates[1], ["N", "E", "S", "W"][rover.cardinal])