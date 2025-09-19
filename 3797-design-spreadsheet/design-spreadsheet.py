class Spreadsheet:

    def __init__(self, rows: int):
        self.sheet = {}
        for i in range(26):
            self.sheet[chr(ord('A')+i)] = [0]*(rows+1)

    def setCell(self, cell: str, value: int) -> None:
        col, row = self.evaluate(cell)
        self.sheet[col][row] = value
        

    def resetCell(self, cell: str) -> None:
        self.setCell(cell,0)

    def getValue(self, formula: str) -> int:
        cell1, cell2 = formula[1:].split('+')
        if self.isCell(cell1):
            c1,r1 = self.evaluate(cell1)
            v1 = self.sheet[c1][r1]
        else:
            v1 = int(cell1)
        if self.isCell(cell2):
            c2,r2 = self.evaluate(cell2)
            v2 = self.sheet[c2][r2]
        else:
            v2 = int(cell2)
        return v1+v2
    def evaluate(self,address):
        return address[0], int(address[1:])
    
    def isCell(self,address):
        if address[0].isalpha():
            return True

# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)