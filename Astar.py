from tkinter import *

walkable = 0
wall = -1
start = 1
goal = 2
path = 3

class Enviorment:
	grid = [];
	#pathCost[,];
	#heuristic[,];

	def gridParser(self, file):
		i=0;
		row = [];
		with open(file) as fileObj:
			for fileLine in fileObj:
				self.grid.append([]);
				row.clear()
				for char in fileLine:
					if "." in char:
						self.grid[i].append(walkable);
					elif "#" in char:
						self.grid[i].append(wall);
					elif "A" in char:
						self.grid[i].append(start);
					elif "B" in char:
						self.grid[i].append(goal);
					else :
						i += 1;

	def printGrid(self):
		print(self.grid);

	def makeWindow(self, master):
		for x in range(0,7):
			for y in range(0,20):
				if self.grid[x][y] == walkable :
					e = Entry(master, bg ="white", width=2)
					e.grid(row=x, column=y)
				elif self.grid[x][y] == wall :
					e = Entry(master, bg ="red", width=2)
					e.grid(row=x, column=y)
				elif self.grid[x][y] == start :
					e = Entry(master, bg ="green", width=2)
					e.grid(row=x, column=y)
				elif self.grid[x][y] == goal :
					e = Entry(master, bg ="black", width=2)
					e.grid(row=x, column=y)
				elif self.grid[x][y] == path :
					e = Entry(master, bg ="blue", width=2)
					e.grid(row=x, column=y)
	def aStar(self) :
                def reconstructPath(cameFrom, current):
                        total_path = [current]
                        while current in cameFrom.Keys:
                                current = cameFrom[current]
                                total_path.append(current)
                                return total_path
                        
                def A_Star(start, goal):
                        emptyGrid = self.grid
                        infinityGrid = self.grid
                        infinityValue = 1000
                        for x in range(0, 7):
                                for y in range(0, 20):
                                        emptyGrid[x][y] = 0

                        for x in range(0, 7):
                                for y in range(0, 20):
                                        infinityGrid[x][y] = infinityValue
                                        
                        closedSet = []
                        openSet = [start]
                        cameFrom = emptyGrid
                        gScore = infinityGrid
                        gScore[start] = 0
                        fScore = infinityGrid
                        fScore[start] = heuristic_cost_estimate(start, goal)

                                while openSet: 
                                        lowestCurrentValue = infinityValue
                                        for x in range(0, 7):
                                                for y in range(0, 20):
                                                        if 
                                                        temp[x][y] = 0

                                        current = the node in openSet having the lowest fScore[] value
                                        if current == goal:
                                                return reconstruct_path(cameFrom, current)

                                        openSet.Remove(current)
                                        closedSet.Add(current)

                                        for neighbor of current:
                                                if neighbor in closedSet
                                                continue

                                        tentative_gScore = gScore[current] + dist_between(current, neighbor)

                                        if neighbor not in openSet
                                        openSet.Add(neighbor)
                                        else if tentative_gScore >= gScore[neighbor]
                                        continue	

                                cameFrom[neighbor] = current
                                gScore[neighbor] = tentative_gScore
                                fScore[neighbor] = gScore[neighbor] + heuristic_cost_estimate(neighbor, goal)
                
def main():
	env = Enviorment();
	master = Tk()
	master.geometry('500x500')
	master.configure(background='SteelBlue1')

	env.gridParser("board-1-4.txt");
	env.printGrid();
	env.aStar();
	env.makeWindow(master);
	


	master.mainloop()



if __name__ == "__main__":
	main();
