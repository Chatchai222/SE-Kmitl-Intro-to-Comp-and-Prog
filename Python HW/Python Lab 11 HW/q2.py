import turtle
import math

def RobotBattle():
    # robotList stores the list of robots in the battle
    robotList = []

    while True:
        # Clear the screen and draw the robots
        turtle.clear()
        turtle.screensize(2000, 2000)
        turtle.speed(10)
        for robot in robotList:
            robot.draw()

        # Display the status of each robot
        print("==== Robots ====")
        i = 0
        for robot in robotList:
            print(i, " : ")
            robot.displayStatus()
            i += 1
        print("================")

        # Ask user which robot to command or the create a new robot
        choice = input("Enter which robot to order, 'c' to create a new robot, 'q' to quit:")
        if choice == "q":
            break
        elif choice == "c":
            print("Enter which type of robots to create")
            robotType = input("'r' for Robot, 'm' for MedicBot, 's' for StrikerBot:")
            if robotType == "r":
                newRobot = Robot()
            elif robotType == "m":
                newRobot = MedicBot()
            elif robotType == "s":
                newRobot = StrikerBot()
            robotList = robotList + [newRobot]
        else:
            n = int(choice)
            robotList[n].command(robotList)

        # Delete all the robots with health <= 0 from the list
        i = 0
        for robot in robotList:
            if robot.health <= 0:
                del robotList[i]
            i += 1

class Robot(object):
    def __init__(self):
        self.x = 100
        self.y = 100
        self.health = 100
        self.energy = 100
        self.radius = 50

    def move(self, x, y):
        if self.energy > 0:
            self.x = x
            self.y = y
            self.energy -= 10
        if self.energy <= 0:
            pass

    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y - self.radius)
        turtle.pendown()
        turtle.circle(self.radius)

    def displayStatus(self):
        print("x=", self.x, "y=", self.y, "health=", self.health, "energy=", self.energy)

    def command(self, robotList):
        print("Possible actions: move")
        newX = int(input("Enter new x-coordinate: "))
        newY = int(input("Enter new y-coordinate: "))
        self.move(newX, newY)

class MedicBot(Robot):
    def __init__(self):
        super().__init__()

    def draw(self):
        super().draw()
        turtle.backward(self.radius * 0.1)
        turtle.left(90)
        turtle.penup()
        turtle.forward(self.radius * 1.2)
        turtle.pendown()
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(self.radius/3)
            turtle.right(90)
            turtle.forward(self.radius/3)
            turtle.right(90)
            turtle.forward(self.radius/3)
            turtle.left(90)
        turtle.end_fill()

    def getDistance(self, r):
        return math.sqrt((self.x - r.x) ** 2 - (self.y - r.y) ** 2)

    def heal(self, r):
        if self.energy >= 20 and self.getDistance(r) <= 10:
            self.energy -= 10
            r.health += 10

    def command(self, robotList):
        print("Possible action: move(m), heal(h)")
        choice = input("Please enter action: ")
        if choice == "m":
            newX = int(input("Enter new x-coordinate: "))
            newY = int(input("Enter new y-coordinate: "))
            super().move(newX, newY)
        if choice == "h":
            botToHeal = int(input("Which bot do you want to heal?:"))
            self.heal(robotList[botToHeal])

class StrikerBot(Robot):
    def __init__(self):
        super().__init__()
        self.missile = 5

    def draw(self):
        super().draw()
        turtle.left(90)
        turtle.penup()
        turtle.forward(self.radius * 0.2)
        turtle.right(45)
        turtle.pendown()
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(self.radius * 1)
            turtle.left(90)
        turtle.left(45)
        turtle.end_fill()

    def getDistance(self, r):
        return math.sqrt((self.x - r.x) ** 2 - (self.y - r.y) ** 2)

    def strike(self, r):
        if self.energy >= 20 and self.missile > 0 and self.getDistance(r) <= 10:
            self.energy -= 20
            self.missile -= 1
            r.health -= 50

    def displayStatus(self):
        print("x=", self.x, "y=", self.y, "health=", self.health, "energy=", self.energy, "missile=", self.missile)

    def command(self, robotList):
        print("Possible action: move(m), strike(s)")
        choice = input("Please enter action: ")
        if choice == "m":
            newX = int(input("Enter new x-coordinate: "))
            newY = int(input("Enter new y-coordinate: "))
            super().move(newX, newY)
        if choice == "s":
            botToStrike = int(input("Which bot do you want to strike?:"))
            self.strike(robotList[botToStrike])

RobotBattle()