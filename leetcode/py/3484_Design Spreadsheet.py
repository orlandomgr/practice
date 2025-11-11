class Spreadsheet:

    def getRowColumn(self, cell: str):
        row = int(cell[1:]) 
        column = ord(cell[0]) - 65
        # print("row: %s col: %s" %(row, column))
        return row, column

    def __init__(self, rows: int):
        self.rows = [] * (rows + 1)
        for i in range(rows):
            self.rows.append([0] * 26)
        # print(self.rows)

    def setCell(self, cell: str, value: int) -> None:
        row, column = self.getRowColumn(cell)
        # print("row: %s col: %s" %(row, column))
        # print(self.rows[row][column])
        self.rows[row][column] = value
        # print(self.rows[row][column])
        # print(self.rows)


    def resetCell(self, cell: str) -> None:
        self.setCell(cell, 0)

    def isCellValue(self, cell: str) -> bool:
        column = ord(cell[0])
        size = len(cell)
        if column >= 65 and column <= 90 and size > 1:
            return True
        return False

    def getValue(self, formula: str) -> int:
        formula = formula[1:]
        args = formula.split("+")
        x = args[0]
        y = args[1]
        # print(self.rows)
        if self.isCellValue(x):
            # print(x)
            row, column = self.getRowColumn(x)
            # print("row: %s" %row)
            # print("col: %s" %column)
            x = self.rows[row][column]
            # print(x)
        else:
            x = int(x)
        if self.isCellValue(y):
            # print(y)
            row, column = self.getRowColumn(y)
            # print("row: %s" %row)
            # print("col: %s" %column)
            y = self.rows[row][column]
            # print(y)
        else:
            y = int(y)
        # print(x + y)
        return x + y

spreadsheet = Spreadsheet(657)
# spreadsheet.setCell("U558", 17217)
# spreadsheet.getValue("=59437+H286")
# spreadsheet.setCell("C164", 67231)
spreadsheet.setCell("Y294", 75466)
spreadsheet.getValue("=Y169+Y294")
# spreadsheet.resetCell("F154")

# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
# obj = Spreadsheet(10)
# print(obj.rows)

# Input:
# ["Spreadsheet", "getValue", "setCell", "getValue", "setCell", "getValue", "resetCell", "getValue"]
# [[3], ["=5+7"], ["A1", 10], ["=A1+6"], ["B2", 15], ["=A1+B2"], ["A1"], ["=A1+B2"]]

# Output:
# [null, 12, null, 16, null, 25, null, 15]


# spreadsheet = Spreadsheet(3); # Initializes a spreadsheet with 3 rows and 26 columns
# spreadsheet.getValue("=5+7"); # returns 12 (5+7)
# spreadsheet.setCell("A1", 10); # sets A1 to 10
# spreadsheet.getValue("=A1+6"); # returns 16 (10+6)
# spreadsheet.setCell("B2", 15); # sets B2 to 15
# spreadsheet.getValue("=A1+B2"); # returns 25 (10+15)
# spreadsheet.resetCell("A1"); # resets A1 to 0
# spreadsheet.getValue("=A1+B2"); # returns 15 (0+15)


# [[159],["=17904+30717"],["=Z37+38471"]]
# spreadsheet = Spreadsheet(159); # Initializes a spreadsheet with 3 rows and 26 columns
# spreadsheet.getValue("=17904+30717"); # returns 12 (5+7)
# spreadsheet.getValue("=Z37+38471"); # returns 12 (5+7)





# [null,null,59437,null,null,150932,null]
# [null,null,59437,null,null,75466,null] ok
