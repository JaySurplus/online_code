"""
    37. Sudoku Solver

    Write a program to solve a Sudoku puzzle by filling the empty cells.

    Empty cells are indicated by the character '.'.

    You may assume that there will be only one unique solution.

    https://leetcode.com/problems/sudoku-solver/
"""
import time
import copy
from collections import defaultdict
class Solution(object):
    def solveSudoku(self, board, n):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
        solution = []


        valid_num = set(["1","2","3","4","5","6","7","8","9"])
        row = defaultdict(set)
        col = defaultdict(set)
        squ = defaultdict(set)
        poss = defaultdict(lambda : defaultdict(set))

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    squ[i/3*3+j/3].add(board[i][j])

    
        self.update(board, solution ,n , row, col , squ)
        
        return solution
    
        
      
    def update(self, board,solution ,n , row ,col ,squ):
        if n > 0:
            if len(solution) >= n:
                return

        valid_num = set(["1","2","3","4","5","6","7","8","9"])
        poss = []

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    poss.append( ( (i,j),valid_num - (row[i]|col[j]|squ[i/3*3+j/3])))
           



        poss_list = [(key , list(val)) for key , val in poss]

        if  len(poss_list) == 0:
            temp = copy.deepcopy(board)
            
            solution.append(temp)

             
        else:
            poss_list.sort(key = lambda x:len(x[1]))
           
            if len(poss_list[0][1]) != 0:
                
                ind , vals = poss_list[0]
                i , j = ind

                for val in vals:
                    temp = board[i][j]

                    board[i][j] = val


                 

                    row[i].add(val)
                    col[j].add(val)
                    squ[i/3*3+j/3].add(val)

                    
                   
                    #print 'b' ,squ[i/3*3+j/3] , board[i][j]
                    
                    self.update(board,solution,n ,row,col ,squ)

                    
                    row[i].remove(val)
                    col[j].remove(val)
                    squ[i/3*3+j/3].remove(val)

                    board[i][j] = temp
                 

            else:
                return
                
                
        
        

    def test(self, board):
        board = [list(i) for i in board]
        valid_num = set(["1","2","3","4","5","6","7","8","9"])
        for i in range(9):
            if len(set(board[i])) != 9:
                return False

            col = [row[i] for row in board]
            if len(set(col)) != 9:
                return False

            block = [ row[i%3*3: i%3*3+3] for row in board[i/3*3 : i/3*3+3]]
            block = [ val for sublist in block for val in sublist]
            if len(set(block)) != 9:
                return False

        return True
        
        
        

        
        
sol = Solution()
board = [".........","..2......",".....271.",".........",".2.......",".5.......","....9...8",".....16..","....6...."]
#board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]

board = ["8........","..36.....",".7..9.2..",".5...7...","....457..","...1...3.","..1....68","..85...1.","..9...4.."]
#board = [".87654321","2........","3........","4........","5........","6........","7........","8........","........."]
#board = [".........",".........",".........",".........",".........",".........",".........",".........","........."]
board = [list(i) for i in board]


n = 0
print "Sudoku :"
for i in board:
    print '  '.join(i)


start = time.time()
t = sol.solveSudoku(board,n)
end = time.time()

print 
print "Running time is %f ms" %  (1000*float(end - start))

print
i = 0 
for i in range(len(t)):
    print "Solution %d" %(i+1)
    print sol.test(t[i])
    for row in t[i]:
        print '  '.join(row)
    print ""
print "%.2f ms for %d solutions. %.2f ms per solution." %( 1000*float(end - start) , i + 1 , 1000*float(end - start)/(i+1) ) 