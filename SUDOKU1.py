def find_next_empty(puzzle):  #finds next row or column that is not filled yet
    for r in range(9):
        for c in range(9):
            if puzzle[r][c]== -1:
                return r,c
    return None, None
def is_valid(puzzle,guess,row,col):
    
    row_vals =puzzle[row]
    if guess in row_vals:
        return False
    col_vals = []
    for i in range(9):
        col_vals.append(puzzle[i][col])
    col_vals =[puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    
    row_start =(row // 3) *3   
    col_start =(col // 3) *3   

    for r in range(row_start,row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] ==guess:
                return False
          
    return True      

def solve_sudoku(puzzle):    #using backtracking and we using indcies 0-8

    #step1:choose somewhere on the puzzle to guess
    row,col =find_next_empty(puzzle)
   #step1.1: If there is nowhere left, then we are done  
    if row is None:
        return True
        #step2: If there is a place to put a number,then make a guess between 1 and 9
    for guess in range(1,10):
        #step3: Check if this is valid guess

        if is_valid(puzzle,guess,row,col):
            #step3.1: If this is valid then place that guess on the puzzle
            puzzle[row][col] = guess
            
            #step4: Recursively call our function
            if solve_sudoku(puzzle):
                return True
        #step5: if not valid or if our guess does not solve the puzzle
        #Backtrack and try a new number 
        puzzle[row][col] = -1    #reset the guess
   #step6: If none of the numbers that we try work, then this puzzle is unsolvable
    return False
if __name__ =='__main__':
    example_board =[
        [3,9,-1,   -1,5,-1,   -1,-1,-1],
        [-1,-1,-1,  2,-1,-1,   -1,-1,5],
        [-1,-1,-1,  7,1,9,     -1,8,-1],

        [-1,5,-1,  -1,6,8,     -1,-1,-1],
        [2,-1,6,   -1,-1,3,    -1,-1,-1],
        [-1,-1,-1,  -1,-1,-1,  -1,-1,4],

        
        [5,-1,-1,  -1,-1,-1,   -1,-1,-1],
        [6,7,-1,  -1,-1,5,     -1,4,-1],
        [-1,1,9,  -1,-1,-1,     2,-1,-1]
    ]        
    print(solve_sudoku(example_board))
    print(example_board)

  
