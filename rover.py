class Plateau:
    def __init__(self, x, y):
        self.boundingRect = [0,0,x,y]

    rovers = []

    def CreateNewRover(self):
        info = input().split(" ")
        rover = self.InitialiseRover(info[0], info[1], info[2])
        return rover

    def InitialiseRover(self, x, y, cardinal):
        rover = Rover(x, y, cardinal)
        self.rovers.append(rover)
        return rover



class Rover:
    def __init__(self, x, y, cardinal):
        self.coordinates = [int(x),int(y)]
        self.cardinal = ["N", "E", "S", "W"].index(cardinal)
        
    def UpdateCoordinates(self):
        movement = input().split("M")
        for instruction in movement[0:-1]:
            self.Rotate(instruction)
            self.Move()
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


def InitialisePlateau():
    info = input().split(" ")
    return Plateau(info[0], info[1])

plateau = InitialisePlateau()
for i in range(2):
    plateau.CreateNewRover().UpdateCoordinates()

for rover in plateau.rovers:
    print(rover.coordinates[0], rover.coordinates[1], ["N", "E", "S", "W"][rover.cardinal])