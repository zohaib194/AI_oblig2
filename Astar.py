from tkinter import *


f = open("board-1-1.txt", "r")
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
						i += 1;

	#def makeGridWindow(self):


	def printGrid(self):
		print(self.grid);

	def makeWindow(self, master):
		for x in range(0,7):
			for y in range(0,20):
				if self.grid[x][y] == 0 :
					e = Entry(master, text="A", bg ="white", width=2)
					e.grid(row=x, column=y)
				elif self.grid[x][y] == -1 :
					e = Entry(master, bg ="red", width=2)
					e.grid(row=x, column=y)
				elif self.grid[x][y] == 1 :
					e = Entry(master, bg ="green", width=2)
					e.grid(row=x, column=y)
				elif self.grid[x][y] == 2 :
					e = Entry(master, text="A", bg ="black", width=2)
					e.grid(row=x, column=y)




def main():
	env = Enviorment();
	master = Tk()
	master.geometry('500x500')
	master.configure(background='SteelBlue1')

	env.gridParser("board-1-3.txt");
	env.printGrid();
	env.makeWindow(master);
	

	master.mainloop()



if __name__ == "__main__":
	main();