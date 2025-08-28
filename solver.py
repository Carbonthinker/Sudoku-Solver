import sys
number_of_calls = 0
def read_file(text_file):
    f=open(text_file, 'r');
    next(f)
    matrix = [[0 for x in range(9)] for y in range(9)]

    for i in range(9):
        line = f.readline()
        for j in range(9):
            matrix[i][j] = int(line[j])
    
    return matrix

def sudoku_solver(matrix):
    global number_of_calls
    number_of_calls += 1;

    if (loc_next_to_solve(matrix) == -1):
        return matrix
    else:
        for i in range(9):
            for j in range(9):
                if (matrix[i][j] == 0):
                    loc = (i, j)
                    for k in range(1,10):
                        if (check_validity(k, matrix, loc[0], loc[1])):
                            matrix[loc[0]][loc[1]] = k
                            res = sudoku_solver(matrix)
                            if (res != -1):
                                return res
                            else:
                                matrix[loc[0]][loc[1]] = 0
                    return -1
    return "no solution"


def check_validity(x, matrix, i, j):
    square_offset = ((int(i/3)) * 3, (int(j/3)) * 3)
    for k in range(9):
        if (matrix[i][k] == x and  k != j):
            return False
        if (matrix[k][j] == x and  k != i):
            return False
    for k in range(3):
        for h in range(3):
            loc = (k + square_offset[0], h + square_offset[1])
            if (matrix[loc[0]][loc[1]] == x and loc[0]!=i and loc[1]!=j):
                return False
    return True
        

def loc_next_to_solve(matrix):
    for i in range(9):
        for j in range(9):
            if (matrix[i][j] == 0):
                return (i, j)
    return -1
    
matrix = read_file(sys.argv[1])

print(sudoku_solver(matrix))
print(number_of_calls)