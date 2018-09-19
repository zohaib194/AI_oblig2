f = open("board-1-2.txt", "r")
print(f.read())

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
						self.grid[i].append(0);
					elif "#" in char:
						self.grid[i].append(-1);
					elif "A" in char:
						self.grid[i].append(1);
					elif "B" in char:
						self.grid[i].append(2);
					else :
						i+=1;

	def printGrid(self):
		print(self.grid);


env = Enviorment();
env.gridParser("board-1-2.txt");
env.printGrid();
