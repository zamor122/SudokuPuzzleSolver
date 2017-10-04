from threading import Thread
from Queue import *
"""
function to welcome the user and obtain the file path
if file path not valid get a valid file path or 0 to quit
"""
def welcomeSudoku():
    print "Welcome to Sudoku Solver"
    FilePath = str(raw_input("Please enter the file path: "))
    while True:
        try:
            if(FilePath == '0'):
                print "Thank you for using Sudoku Solver, Goodbye"
                exit(0)
            file = open(FilePath, "r")
            file.close()
            return FilePath
        except IOError:
            print "File Could not be opened please try again"
            FilePath = str(raw_input("Please enter the file path: "))
##END welcomeSudoku()


"""
FUNCTION THAT RETURNS A 1D LIST OF EVERYTHING IN THE GRID
"""
def getRowsOfNumbers(FilePath,results):
    newList = []
    try:
        with open(FilePath, "r") as file:
            for line in file:
                for i in line:
                    if i == "," or i == "\n":
                        pass
                    else:
                        newList.append(int(i))
        return results.put(newList)
    except IOError:
        "Error, file could not be opened. Please reset program and try again."
        return 0

"""
FUNCTION TO SLICE THE LIST INTO 9 COLUMNS
"""
def slice_for_columns(source):
    columnList = [source[i::9] for i in range(9)]
    columnTuple = tuple(columnList)
    return columnTuple
"""
FUNCTION TO SLICE THE LIST INTO 9 ROWS
"""
def slice_for_rows(source):
    rowList = [source[i:i + 9] for i in xrange(0, len(source), 9)]
    rowTuple = tuple(rowList)
    return rowTuple
"""
RETURN THE COLUMNS
"""
def getColumns(newList,results):
    columnList = slice_for_columns(newList)
    columns = tuple(columnList)
    return results.put(columns)
"""
RETURN THE ROWS
"""
def getRows(newList,results):
    rowList = slice_for_rows(newList)
    rows = tuple(rowList)
    return results.put(rows)
"""
FUNCTION TO CHECK GRID 1
"""

def checkIfEqual(line):
    return (len(line) == 9 and sum(line) == sum(set(line)))

def getBadRows(grid,results):
    bad_rows = [row for row in grid if not checkIfEqual(row)]
    if bad_rows == []:
        return results.put(0)
    else:
        return results.put(bad_rows)
def getBadColumns(grid,results):
    grid = list(zip(*grid))
    bad_cols = [col for col in grid if not checkIfEqual(col)]
    if bad_cols == []:
        return results.put(0)
    else:
        return results.put(bad_cols)
def getRowAndColumnNumber(Rows,Columns,badRow,badCol,results):

    newBadRow = []
    newBadCol = []
    locationList = []
    for i in range(1):
        for j in range(0,9):
            newBadRow.append(badRow[i][j])
    for i in range(1):
        for j in range(0,9):
            newBadCol.append(badCol[i][j])
    for i in range(0,9):
        if Rows[i] == newBadRow:
            locationList.append(i)
        else:
            pass
    for j in range(0,9):
        if Columns[j] == newBadCol:
            locationList.append(j)
        else:
            pass
    Location = tuple(locationList)
    return results.put(Location)

"""
FUNCTION TO GET THE CORRECT ANSWER
"""
#LARGE FUNCTION THAT TAKES IN THE ROWS, COLUMNS, TUPLE OF LOCATION OF ERROR AND RETURNS THE CORRECT ANSWER
def getAnswer(rows, columns, errorTuple,results):
    #THE FIRST HALF OF THE FUNCTION TURNS THE ROWS AND COLUMNS INTO TUPLES AND THEN ADDS THEM TO A SET
    currentGrid = []
    rowNumber = errorTuple[0]
    colNumber = errorTuple[1]
    rowWithError = set()
    rowNumberTuple = tuple(rows[rowNumber])
    rowWithError.add(rowNumberTuple)
    columnWithError =  set()
    columnWithTuple = tuple(columns[colNumber])
    columnWithError.add(columnWithTuple)
    ##THE SECOND HALF OF THE FUNCTION FINDS THE CORRECT GRID FOR THE ERROR AND SOLVES FOR THE CORRECT ANSWER
    #GRID 1
    if rowNumber <= 1 and colNumber <=2:
        grid = []
        gridValues = set()
        for i in range(0, 3):
            for j in range(0, 3):
                grid.append(rows[i][j])
        gridWithTuple = tuple(grid)
        gridValues.add(gridWithTuple)
        if 1 not in rowWithError and 1 not in columnWithError and 1 not in gridWithTuple:
            return results.put(1)
        if 2 not in rowWithError and 2 not in columnWithError and 2 not in gridWithTuple:
            return results.put(2)
        if 3 not in rowWithError and 3 not in columnWithError and 3 not in gridWithTuple:
            return results.put(3)
        if 4 not in rowWithError and 4 not in columnWithError and 4 not in gridWithTuple:
            return results.put(4)
        if 5 not in rowWithError and 5 not in columnWithError and 5 not in gridWithTuple:
            return results.put(5)
        if 6 not in rowWithError and 6 not in columnWithError and 6 not in gridWithTuple:
            return results.put(6)
        if 7 not in rowWithError and 7 not in columnWithError and 7 not in gridWithTuple:
            return results.put(7)
        if 8 not in rowWithError and 8 not in columnWithError and 8 not in gridWithTuple:
            return results.put(8)
        if 9 not in rowWithError and 9 not in columnWithError and 9 not in gridWithTuple:
            return results.put(9)
    #GRID 2
    if rowNumber <= 2 and 3 <= colNumber <=5:
        grid = []
        gridValues = set()
        for i in range(0, 3):
            for j in range(3, 6):
                grid.append(rows[i][j])
        gridWithTuple = tuple(grid)
        gridValues.add(gridWithTuple)
        if 1 not in rowWithError and 1 not in columnWithError and 1 not in gridWithTuple:
            return results.put(1)
        if 2 not in rowWithError and 2 not in columnWithError and 2 not in gridWithTuple:
            return results.put(2)
        if 3 not in rowWithError and 3 not in columnWithError and 3 not in gridWithTuple:
            return results.put(3)
        if 4 not in rowWithError and 4 not in columnWithError and 4 not in gridWithTuple:
            return results.put(4)
        if 5 not in rowWithError and 5 not in columnWithError and 5 not in gridWithTuple:
            return results.put(5)
        if 6 not in rowWithError and 6 not in columnWithError and 6 not in gridWithTuple:
            return results.put(6)
        if 7 not in rowWithError and 7 not in columnWithError and 7 not in gridWithTuple:
            return results.put(7)
        if 8 not in rowWithError and 8 not in columnWithError and 8 not in gridWithTuple:
            return results.put(8)
        if 9 not in rowWithError and 9 not in columnWithError and 9 not in gridWithTuple:
            return results.put(9)
    #GRID 3
    if rowNumber <= 2 and 6 <= colNumber <= 9:
        grid = []
        gridValues = set()
        for i in range(0,3):
            for j in range(6,9):
                grid.append(rows[i][j])
        gridWithTuple = tuple(grid)
        gridValues.add(gridWithTuple)
        if 1 not in rowWithError and 1 not in columnWithError and 1 not in gridWithTuple:
            return results.put(1)
        if 2 not in rowWithError and 2 not in columnWithError and 2 not in gridWithTuple:
            return results.put(2)
        if 3 not in rowWithError and 3 not in columnWithError and 3 not in gridWithTuple:
            return results.put(3)
        if 4 not in rowWithError and 4 not in columnWithError and 4 not in gridWithTuple:
            return results.put(4)
        if 5 not in rowWithError and 5 not in columnWithError and 5 not in gridWithTuple:
            return results.put(5)
        if 6 not in rowWithError and 6 not in columnWithError and 6 not in gridWithTuple:
            return results.put(6)
        if 7 not in rowWithError and 7 not in columnWithError and 7 not in gridWithTuple:
            return results.put(7)
        if 8 not in rowWithError and 8 not in columnWithError and 8 not in gridWithTuple:
            return results.put(8)
        if 9 not in rowWithError and 9 not in columnWithError and 9 not in gridWithTuple:
            return results.put(9)
    #GRID 4
    if 3<= rowNumber <= 5 and colNumber <= 2:
        grid = []
        gridValues = set()
        for i in range(3, 6):
            for j in range(0,3):
                grid.append(rows[i][j])
        gridWithTuple = tuple(grid)
        gridValues.add(gridWithTuple)
        if 1 not in rowWithError and 1 not in columnWithError and 1 not in gridWithTuple:
            return results.put(1)
        if 2 not in rowWithError and 2 not in columnWithError and 2 not in gridWithTuple:
            return results.put(2)
        if 3 not in rowWithError and 3 not in columnWithError and 3 not in gridWithTuple:
            return results.put(3)
        if 4 not in rowWithError and 4 not in columnWithError and 4 not in gridWithTuple:
            return results.put(4)
        if 5 not in rowWithError and 5 not in columnWithError and 5 not in gridWithTuple:
            return results.put(5)
        if 6 not in rowWithError and 6 not in columnWithError and 6 not in gridWithTuple:
            return results.put(6)
        if 7 not in rowWithError and 7 not in columnWithError and 7 not in gridWithTuple:
            return results.put(7)
        if 8 not in rowWithError and 8 not in columnWithError and 8 not in gridWithTuple:
            return results.put(8)
        if 9 not in rowWithError and 9 not in columnWithError and 9 not in gridWithTuple:
            return results.put(9)
    # GRID 5
    if 3 <= rowNumber <= 5 and 3 <=colNumber <= 5:
        grid = []
        gridValues = set()
        for i in range(3,6):
            for j in range(3,6):
                grid.append(rows[i][j])
        gridWithTuple = tuple(grid)
        gridValues.add(gridWithTuple)
        if 1 not in rowWithError and 1 not in columnWithError and 1 not in gridWithTuple:
            return results.put(1)
        if 2 not in rowWithError and 2 not in columnWithError and 2 not in gridWithTuple:
            return results.put(2)
        if 3 not in rowWithError and 3 not in columnWithError and 3 not in gridWithTuple:
            return results.put(3)
        if 4 not in rowWithError and 4 not in columnWithError and 4 not in gridWithTuple:
            return results.put(4)
        if 5 not in rowWithError and 5 not in columnWithError and 5 not in gridWithTuple:
            return results.put(5)
        if 6 not in rowWithError and 6 not in columnWithError and 6 not in gridWithTuple:
            return results.put(6)
        if 7 not in rowWithError and 7 not in columnWithError and 7 not in gridWithTuple:
            return results.put(7)
        if 8 not in rowWithError and 8 not in columnWithError and 8 not in gridWithTuple:
            return results.put(8)
        if 9 not in rowWithError and 9 not in columnWithError and 9 not in gridWithTuple:
            return results.put(9)
    # GRID 6
    if 3 <= rowNumber <= 5 and 6 <= colNumber <= 9:
        grid = []
        gridValues = set()
        for i in range(3,6):
            for j in range(6, 9):
                grid.append(rows[i][j])
        gridWithTuple = tuple(grid)
        gridValues.add(gridWithTuple)
        if 1 not in rowWithError and 1 not in columnWithError and 1 not in gridWithTuple:
            return results.put(1)
        if 2 not in rowWithError and 2 not in columnWithError and 2 not in gridWithTuple:
            return results.put(2)
        if 3 not in rowWithError and 3 not in columnWithError and 3 not in gridWithTuple:
            return results.put(3)
        if 4 not in rowWithError and 4 not in columnWithError and 4 not in gridWithTuple:
            return results.put(4)
        if 5 not in rowWithError and 5 not in columnWithError and 5 not in gridWithTuple:
            return results.put(5)
        if 6 not in rowWithError and 6 not in columnWithError and 6 not in gridWithTuple:
            return results.put(6)
        if 7 not in rowWithError and 7 not in columnWithError and 7 not in gridWithTuple:
            return results.put(7)
        if 8 not in rowWithError and 8 not in columnWithError and 8 not in gridWithTuple:
            return results.put(8)
        if 9 not in rowWithError and 9 not in columnWithError and 9 not in gridWithTuple:
            return results.put(9)
    # GRID 7
    if 6 <= rowNumber <= 9 and colNumber <= 2:
        grid = []
        gridValues = set()
        for i in range(6,9):
            for j in range(0,3):
                grid.append(rows[i][j])
        gridWithTuple = tuple(grid)
        gridValues.add(gridWithTuple)
        if 1 not in rowWithError and 1 not in columnWithError and 1 not in gridWithTuple:
            return results.put(1)
        if 2 not in rowWithError and 2 not in columnWithError and 2 not in gridWithTuple:
            return results.put(2)
        if 3 not in rowWithError and 3 not in columnWithError and 3 not in gridWithTuple:
            return results.put(3)
        if 4 not in rowWithError and 4 not in columnWithError and 4 not in gridWithTuple:
            return results.put(4)
        if 5 not in rowWithError and 5 not in columnWithError and 5 not in gridWithTuple:
            return results.put(5)
        if 6 not in rowWithError and 6 not in columnWithError and 6 not in gridWithTuple:
            return results.put(6)
        if 7 not in rowWithError and 7 not in columnWithError and 7 not in gridWithTuple:
            return results.put(7)
        if 8 not in rowWithError and 8 not in columnWithError and 8 not in gridWithTuple:
            return results.put(8)
        if 9 not in rowWithError and 9 not in columnWithError and 9 not in gridWithTuple:
            return results.put(9)
    # GRID 8
    if 6 <= rowNumber <= 9 and 3 <= colNumber <= 5:
        grid = []
        gridValues = set()
        for i in range(6,9):
            for j in range(3,6):
                grid.append(rows[i][j])
        gridWithTuple = tuple(grid)
        gridValues.add(gridWithTuple)
        if 1 not in rowWithError and 1 not in columnWithError and 1 not in gridWithTuple:
            return results.put(1)
        if 2 not in rowWithError and 2 not in columnWithError and 2 not in gridWithTuple:
            return results.put(2)
        if 3 not in rowWithError and 3 not in columnWithError and 3 not in gridWithTuple:
            return results.put(3)
        if 4 not in rowWithError and 4 not in columnWithError and 4 not in gridWithTuple:
            return results.put(4)
        if 5 not in rowWithError and 5 not in columnWithError and 5 not in gridWithTuple:
            return results.put(5)
        if 6 not in rowWithError and 6 not in columnWithError and 6 not in gridWithTuple:
            return results.put(6)
        if 7 not in rowWithError and 7 not in columnWithError and 7 not in gridWithTuple:
            return results.put(7)
        if 8 not in rowWithError and 8 not in columnWithError and 8 not in gridWithTuple:
            return results.put(8)
        if 9 not in rowWithError and 9 not in columnWithError and 9 not in gridWithTuple:
            return results.put(9)
    # GRID 9
    if 6 <= rowNumber <= 9 and 6 <= colNumber <= 9:
        grid = []
        gridValues = set()
        for i in range(6,9):
            for j in range(6, 9):
                grid.append(rows[i][j])
        gridWithTuple = tuple(grid)
        gridValues.add(gridWithTuple)
        if 1 not in rowWithError and 1 not in columnWithError and 1 not in gridWithTuple:
            return results.put(1)
        if 2 not in rowWithError and 2 not in columnWithError and 2 not in gridWithTuple:
            return results.put(2)
        if 3 not in rowWithError and 3 not in columnWithError and 3 not in gridWithTuple:
            return results.put(3)
        if 4 not in rowWithError and 4 not in columnWithError and 4 not in gridWithTuple:
            return results.put(4)
        if 5 not in rowWithError and 5 not in columnWithError and 5 not in gridWithTuple:
            return results.put(5)
        if 6 not in rowWithError and 6 not in columnWithError and 6 not in gridWithTuple:
            return results.put(6)
        if 7 not in rowWithError and 7 not in columnWithError and 7 not in gridWithTuple:
            return results.put(7)
        if 8 not in rowWithError and 8 not in columnWithError and 8 not in gridWithTuple:
            return results.put(8)
        if 9 not in rowWithError and 9 not in columnWithError and 9 not in gridWithTuple:
            return results.put(9)

##############################################################################
#                                                                            #
#                                                                            #
#                                MAIN FUNCTION                               #
#                                                                            #
##############################################################################
"""
MAIN
"""
if __name__ == '__main__':
    results = Queue()
    filePath = welcomeSudoku()
    #grid = getRowsOfNumbers(filePath)
    #rows = getRows(grid)
    #columns = getColumns(grid)
    #badRows = getBadRows(rows)
    #badColumns = getBadColumns(rows)
    #if badRows == 0 and badColumns == 0:
        #print "There are no errors in this puzzle!"
        #exit(0)
    #print "\n"
    #Location = getRowAndColumnNumber(rows,columns,badRows,badColumns)
    #print "There is an error in your code in Row", Location[0]+1, "and Column", Location[1]+1,". The correct answer is: " , getAnswer(rows,columns,Location)
    thread1 = Thread(target=getRowsOfNumbers,args=(filePath,results))
    thread1.start()
    grid = results.get()
    thread2 = Thread(target=getRows,args=(grid,results))
    thread2.start()
    rows = results.get()
    thread3 = Thread(target=getColumns,args=(grid,results))
    thread3.start()
    columns = results.get()
    thread4 = Thread(target=getBadRows,args=(rows,results))
    thread4.start()
    badRows = results.get()
    thread5 = Thread(target=getBadColumns,args=(rows,results))
    thread5.start()
    badColumns = results.get()
    if badRows == 0 and badColumns == 0:
        print "Yay! There are no errors in this Puzzle! Goodbye!"
        exit(0)
    else:
        thread6 = Thread(target=getRowAndColumnNumber(rows,columns,badRows,badColumns,results))
        thread6.start()
        position = results.get()
        thread7 = Thread(target=getAnswer,args=(rows,columns,position,results))
        thread7.start()
        correctAnswer = results.get()
        print "There is an error in your puzzle in Row ", position[0]+1," and Column ", position[1]+1, ". This number should be replaced with: ", correctAnswer
        thread1.join()
        thread2.join()
        thread3.join()
        thread4.join()
        thread5.join()
        thread6.join()
        thread7.join()

#END MAIN
