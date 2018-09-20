from tkinter import *

walkable = 0
wall = -1
start = 1
goal = 2
path = 3


task1 = True

class Enviorment:
        grid = [];
        gridCellWeight = []
        width = 0;
        height = 0;

        #pathCost[,];
        #heuristic[,];

        def gridParser(self, file):
               i=0;
               j=0;
               row = [];
               with open(file) as fileObj:
                     for fileLine in fileObj:
                          self.grid.append([]);
                          self.gridCellWeight.append([]);
                          j = 0;
                          for char in fileLine:
                              j += 1;
                              if task1 and "#" is not char:
                                 self.gridCellWeight.append(1);

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

                          self.width = i;
                          self.height = j - 1;
               print(self.height)

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
        def aStar(self):
                

def main():
        env = Enviorment();
        master = Tk()
        master.geometry('500x500')
        master.configure(background='SteelBlue1')

        env.gridParser("board-1-1.txt");
        env.aStar();
        env.printGrid();
        env.makeWindow(master);
        


        master.mainloop()



if __name__ == "__main__":
        main();

