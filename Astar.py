f = open("board-1-2.txt", "r")
print(f.read())

class Enviorment:
	grid = [];
	#pathCost[,];
	#heuristic[,];

	def gridParser(self, file):
		i=0;
		row =[];
		with open(file) as fileObj:
			for fileLine in fileObj:
				##string = fileLine.split();
				##print(string);
				self.grid.append([]);
				##self.grid[i].append([(int x) for x in fileLine.split()])


				for char in fileLine.split('\n'):
					##print(char);
					if "." in char:
						row.append(0);
					elif "#" in char:
						row.append(-1);
					elif "A" in char:
						row.append(1);
					elif "B" in char:
						row.append(2);
					else :
						self.grid[i].append(row);
						i += 1;

		##print(row);
		print(self.grid);


env = Enviorment();
env.gridParser("board-1-2.txt");
#print(len(open("board-1-2.txt").readlines(  )));