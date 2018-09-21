from tkinter import *
import numpy as np
walkable = 0
wall = np.inf
start = 1
goal = 2
path = 3


task1 = True


class Enviorment:
    grid = []
    gridCellWeight = []
    width = 0
    height = 0
    goalCell = None  # goal cell
    startCell = None  # start cell

    # pathCost[,];
    # heuristic[,];

    def gridParser(self, file):
        i = 0
        j = 0
        row = []
        with open(file) as fileObj:
            for fileLine in fileObj:
                self.grid.append([])
                self.gridCellWeight.append([])
                j = 0
                for char in fileLine:
                    if task1 and "#" is not char:
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

    def printGrid(self):
        print(self.grid)

    def makeWindow(self, master):
        path = self.aStar()
        for p in path:
          if self.grid[p[1]][p[0]] == self.startCell :
            self.grid[p[1]][p[0]] = start;
          else :
            self.grid[p[1]][p[0]] = path;
        
        for y in range(0, self.height):
            for x in range(0, self.width):
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

    def makeShortestPath(self, cameFrom, current):
        total_path = [current]
        while current is not self.startCell:
            current = cameFrom[(current[1] * self.width) + current[0]]
            total_path.append(current)
        return total_path

    def heuristicValue(self, start, goal):
        return (abs(start[0] - goal[0]) + abs(start[1] - goal[1]))

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

        self.gridCellWeight[self.startCell[1]][self.startCell[0]] = self.heuristicValue(self.startCell, self.goalCell)

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
                if (n[0] < 0 or n[0] > self.width - 1 or
                    n[1] < 0 or n[1] > self.height - 1 or n in closedSet):
                    continue

                tentativeGscore = self.gridCellWeight[current[1]][
                    current[0]] + self.gridCellWeight[n[1]][n[0]]
                if n not in openSet:
                    openSet.append(n)
                elif tentativeGscore >= self.gridCellWeight[n[1]][n[0]]:
                    continue
                cameFrom[(n[1] * self.width) + n[0]] = current
                self.gridCellWeight[n[1]][n[0]] = tentativeGscore
                fScore[(n[1] * self.width) + n[0]] = self.gridCellWeight[n[1]
                                                                         ][n[0]] + self.heuristicValue(n, self.goalCell)

            openSet.sort(key=lambda e: self.gridCellWeight[e[1]][e[0]])
            ##print(openSet)


def main():
    env = Enviorment()
    master = Tk()
    master.geometry('500x500')
    master.configure(background='SteelBlue1')

    env.gridParser("board-1-3.txt")
    #env.aStar()
    env.makeWindow(master)
    #env.printGrid();

    master.mainloop()


if __name__ == "__main__":
    main()
