class Spreadsheet:

    def __init__(self, rows: int):
        self.sheet = []
        for i in range(rows):
            self.sheet.append([])
            for _ in range(26):
                self.sheet[i].append(0)

    def setCell(self, cell: str, value: int) -> None:
        x = ord(cell[0]) - ord("A")
        y = int(cell[1:]) - 1
        self.sheet[y][x] = value

    def resetCell(self, cell: str) -> None:
        self.setCell(cell, 0)

    def getValue(self, formula: str) -> int:
        X = formula.split("+")[0][1:]
        Y = formula.split("+")[1]

        return self.getIntVal(X) + self.getIntVal(Y)
    
    def getIntVal(self, val: str) -> int:
        if "A" <= val[0] <= "Z":
            x = ord(val[0]) - ord("A")
            y = int(val[1:]) - 1

            return self.sheet[y][x]
        else:
            return int(val)

# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)