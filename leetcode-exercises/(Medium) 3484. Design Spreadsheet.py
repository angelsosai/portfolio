# A spreadsheet is a grid with 26 columns (labeled from 'A' to 'Z') and a given number of rows. Each cell in the spreadsheet can hold an integer value between 0 and 105.

# Implement the Spreadsheet class:

# Spreadsheet(int rows) Initializes a spreadsheet with 26 columns (labeled 'A' to 'Z') and the specified number of rows. All cells are initially set to 0.
# void setCell(String cell, int value) Sets the value of the specified cell. The cell reference is provided in the format "AX" (e.g., "A1", "B10"), where the letter represents the column (from 'A' to 'Z') and the number represents a 1-indexed row.
# void resetCell(String cell) Resets the specified cell to 0.
# int getValue(String formula) Evaluates a formula of the form "=X+Y", where X and Y are either cell references or non-negative integers, and returns the computed sum.
# Note: If getValue references a cell that has not been explicitly set using setCell, its value is considered 0.

class Spreadsheet:

    def __init__(self, rows: int):
        self.lista = [[0]*26 for _ in range(rows)] 
        # self.lista=[[0]*26]*rows
        self.dic={"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,"K":10,"L":11,"M":12,"N":13,"O":14,"P":15,"Q":16,"R":17,"S":18,"T":19,"U":20,"V":21,"W":22,"X":23,"Y":24,"Z":25}
        # print(self.lista)

    def setCell(self, cell: str, value: int) -> None:
        # print(cell)
        # print(cell[0],cell[1:],value)
        self.lista[int(cell[1:])-1][self.dic[cell[0]]]=value
    def resetCell(self, cell: str) -> None:
        
        self.lista[int(cell[1:])-1][self.dic[cell[0]]]=0

    def getValue(self, formula: str) -> int:
        j = formula.find("+")  # primer '+' después de '='
        X = formula[1:j]
        y = formula[j+1:]
        # print(X,y)
        try:
            valor1=int(X)
        except:
            # print(X[1:],self.lista[int(X[1:])-1][self.dic[X[0]]])
            valor1=self.lista[int(X[1:])-1][self.dic[X[0]]]
        try:
            valor2=int(y)
        except:
            # print(y[1:])
            valor2=self.lista[int(y[1:])-1][self.dic[y[0]]]
        # print(valor1,valor2)
        return valor1+valor2


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)