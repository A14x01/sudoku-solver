import numpy as np

sudoku = [[1,7,0,4,0,5,0,0,9],
        [0,0,0,0,2,0,4,0,0],
        [0,0,5,0,6,0,0,0,0],
        [0,0,0,0,5,0,0,0,0],
        [0,0,7,3,0,1,6,0,0],
        [0,9,0,0,0,0,0,8,0],
        [0,0,0,2,0,0,0,0,0],
        [3,0,0,0,0,0,0,0,6],
        [0,0,1,7,0,4,3,0,0]]

print(np.array(sudoku))

print("---------------------")

def possible (row, column, number):
    global sudoku
    for i in range(0,9):
        if sudoku[row][i] == number:
            return False

    for i in range(0,9):
        if sudoku[i][column] == number:
            return False

    x0 = (column // 3) * 3
    y0 = (row // 3) * 3
    for i in range(0,3):
        for j in range(0,3):
            if sudoku[y0+i] [x0+j] == number:
                return False
    
    return True

def solve():
    global sudoku
    for row in range(0,9):
        for column in range(0,9):
            if sudoku[row][column] == 0:
                for number in range(1,10):
                    if possible(row, column ,number):
                        sudoku[row][column] = number
                        solve()
                        sudoku[row][column] = 0
                return
    
    print(np.array(sudoku))
    input("Press enter, if you want to see more solutions.")
solve()
