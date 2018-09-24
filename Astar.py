from tkinter import *
import numpy as np

#This variable is changed depending on which part of assignment is to be run, since part 1 uses symbols and part 2 uses characters
#task = 1, for part 1
#task = 2, for part 2
task = 2

#constants used for parsing the boards
walkable = 0
wall = np.inf
start = 4
goal = 2
path = 3

#weights used when parsing the boards
water = 100
mountain = 50
forest = 10
grassland = 5
road = 1



class Enviorment:
    grid = []
    gridCellWeight = []
    width = 0
    height = 0
    goalCell = None  # goal cell
    startCell = None  # start cell

    # pathCost[,];
    # heuristic[,];

    #function: reads the board file and stores the grid depending on task 1 or task 2
    def gridParser(self, file):
        i = 0
        j = 0
        row = []

        #parsing the board file into a array
        with open(file) as fileObj:
            for fileLine in fileObj:
                self.grid.append([])
                self.gridCellWeight.append([])
                j = 0
                for char in fileLine:
                    #task 2 uses letters
                    if task == 2:
                        if "m" in char:
                            self.gridCellWeight[i].append(mountain)
                            self.grid[i].append(mountain)
                        elif "w" in char:
                            self.gridCellWeight[i].append(water)
                            self.grid[i].append(water)
                        elif "f" in char:
                            self.gridCellWeight[i].append(forest)
                            self.grid[i].append(forest)
                        elif "g" in char:
                            self.gridCellWeight[i].append(grassland)
                            self.grid[i].append(grassland)
                        elif "r" in char:
                            self.gridCellWeight[i].append(road)
                            self.grid[i].append(road)
                        elif "A" in char:
                            print("passInit")
                            self.startCell = (j, i)
                            self.grid[i].append(start)
                            self.gridCellWeight[i].append(start)
                        elif "B" in char:
                            self.goalCell = (j, i)
                            self.grid[i].append(goal)
                            self.gridCellWeight[i].append(goal)
                        else:
                            i += 1

                    #task 1 uses signs in the board files so this were we parse those
                    if task == 1:
                        if "#" is not char:
                            self.gridCellWeight[i].append(walkable)
                        else:
                            self.gridCellWeight[i].append(wall)

                        if "." in char:
                            self.grid[i].append(walkable)
                        elif "#" in char:
                            self.grid[i].append(wall)
                        elif "A" in char:
                            self.grid[i].append(start)
                            self.startCell = (j, i)
                        elif "B" in char:
                            self.grid[i].append(goal)
                            self.goalCell = (j, i)
                        else:
                            i += 1

                    j += 1
                self.width = j - 1
                self.height = i
    #prints the grid array in the console
    def printGrid(self):
        print(self.grid)

    #creates the visual window of environment
    def makeWindow(self, master):
        path = self.aStar()
        for p in path:
              if self.grid[p[1]][p[0]] == start:
                  self.grid[p[1]][p[0]] = start
              elif self.grid[p[1]][p[0]] == goal:
                  self.grid[p[1]][p[0]] = goal
              else:
                  self.grid[p[1]][p[0]] = path

        for y in range(0, self.height):
            for x in range(0, self.width):
                if task == 1:
                    if self.grid[y][x] == walkable:
                        e = Entry(master, bg="white", width=2)
                        e.grid(row=y, column=x)
                    elif self.grid[y][x] == wall:
                        e = Entry(master, bg="red", width=2)
                        e.grid(row=y, column=x)
                    elif self.grid[y][x] == start:
                        e = Entry(master, bg="green", width=2)
                        e.grid(row=y, column=x)
                    elif self.grid[y][x] == goal:
                        e = Entry(master, bg="black", width=2)
                        e.grid(row=y, column=x)
                    elif self.grid[y][x] == path:
                        e = Entry(master, bg="blue", width=2)
                        e.grid(row=y, column=x)
                if task == 2:
                    if self.grid[y][x] == mountain:
                        e = Entry(master, bg="gray", width=2)
                        e.grid(row=y, column=x)
                    elif self.grid[y][x] == water:
                        e = Entry(master, bg="blue", width=2)
                        e.grid(row=y, column=x)
                    elif self.grid[y][x] == road:
                        e = Entry(master, bg="tan4", width=2)
                        e.grid(row=y, column=x)
                    elif self.grid[y][x] == grassland:
                        e = Entry(master, bg="lightgreen", width=2)
                        e.grid(row=y, column=x)
                    elif self.grid[y][x] == forest:
                        e = Entry(master, bg="darkgreen", width=2)
                        e.grid(row=y, column=x)
                    elif self.grid[y][x] == start:
                        print("passColor")
                        e = Entry(master, bg="red", width=2)
                        e.grid(row=y, column=x)
                    elif self.grid[y][x] == goal:
                        e = Entry(master, bg="black", width=2)
                        e.grid(row=y, column=x)
                    elif self.grid[y][x] == path:
                        e = Entry(master, bg="yellow", width=2)
                        e.grid(row=y, column=x)

    #retraces the path taken and stores it in total_path array
    def makeShortestPath(self, cameFrom, current):
        total_path = [current]
        while current is not self.startCell:
            current = cameFrom[(current[1] * self.width) + current[0]]
            total_path.append(current)
        return total_path

    #calculates the heuristic value using manhattan distance
    def heuristicValue(self, start, goal):
        return (abs(start[0] - goal[0]) + abs(start[1] - goal[1]))

    #this function runs the astar algorithm
    def aStar(self):
        #infinityGrid = self.grid
        infinityValue = 1000

        closedSet = []  # grid cells already visited.
        cameFrom = [0 for i in range(0, self.width * self.height)]
        # cost from a cell to any other cell
        fScore = [1 for i in range(0, self.width * self.height)]

        openSet = [self.startCell]  # x,y start cell in grid.

        # Initializing variables for the path finding.
        # x,y grid cell and 0 for the cost for going from start to start.
        self.gridCellWeight[self.startCell[1]][self.startCell[0]] = 0

        self.gridCellWeight[self.startCell[1]][self.startCell[
            0]] = self.heuristicValue(self.startCell, self.goalCell)

        while len(openSet) is not 0:

            current = openSet[0]

            if current == self.goalCell:
                return self.makeShortestPath(cameFrom, current)

            openSet.remove(current)
            closedSet.append(current)

            # print(current)
            # Current cell neighbors.
            neighbor = [(current[0] - 1, current[1]),
                        (current[0], current[1] - 1),
                        (current[0] + 1, current[1]),
                        (current[0], current[1] + 1)]

            for n in neighbor:
                if (n[0] < 0 or n[0] > self.width - 1 or n[1] < 0 or n[1] > self.height - 1 or n in closedSet):
                    continue

                tentativeGscore = self.gridCellWeight[current[1]][current[0]] + self.gridCellWeight[n[1]][n[0]]
                if n not in openSet:
                    openSet.append(n)
                elif tentativeGscore >= self.gridCellWeight[n[1]][n[0]]:
                    continue
                cameFrom[(n[1] * self.width) + n[0]] = current
                self.gridCellWeight[n[1]][n[0]] = tentativeGscore
                fScore[(n[1] * self.width) + n[0]] = self.gridCellWeight[n[1]][n[0]] + self.heuristicValue(n, self.goalCell)

            openSet.sort(key=lambda e: self.gridCellWeight[e[1]][e[0]])
            # print(openSet)

#setup and initialization of the program
def main():
    env = Enviorment()
    master = Tk()
    master.geometry('700x300')
    master.configure(background='SteelBlue1')

    #change this variable depending on which board you want to parse
    env.gridParser("board-2-4.txt")
    # env.aStar()
    env.makeWindow(master)
    # env.printGrid();

    master.mainloop()


if __name__ == "__main__":
    main()
