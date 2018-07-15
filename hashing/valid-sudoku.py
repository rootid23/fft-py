#Valid Sudoku
#Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#    Each row must contain the digits 1-9 without repetition.
#    Each column must contain the digits 1-9 without repetition.
#    Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
#A partially filled sudoku which is valid.
#The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
#Example 1:
#Input:
#[
#  ["5","3",".",".","7",".",".",".","."],
#  ["6",".",".","1","9","5",".",".","."],
#  [".","9","8",".",".",".",".","6","."],
#  ["8",".",".",".","6",".",".",".","3"],
#  ["4",".",".","8",".","3",".",".","1"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".","6",".",".",".",".","2","8","."],
#  [".",".",".","4","1","9",".",".","5"],
#  [".",".",".",".","8",".",".","7","9"]
#]
#Output: true
#Example 2:
#Input:
#[
#  ["8","3",".",".","7",".",".",".","."],
#  ["6",".",".","1","9","5",".",".","."],
#  [".","9","8",".",".",".",".","6","."],
#  ["8",".",".",".","6",".",".",".","3"],
#  ["4",".",".","8",".","3",".",".","1"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".","6",".",".",".",".","2","8","."],
#  [".",".",".","4","1","9",".",".","5"],
#  [".",".",".",".","8",".",".","7","9"]
#]
#Output: false
#Explanation: Same as Example 1, except with the 5 in the top left corner being
#    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
#Note:
#    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#    Only the filled cells need to be validated according to the mentioned rules.
#    The given board contain only digits 1-9 and the character '.'.
#    The given board size is always 9x9.

# Use encoded key
#1. row key - (row,val)
#2. col key - To avoid collision use (col, val)
#3. inner board key - (position, val)
class Solution(object):

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        #0,0 -> 8 , 0,1 -> 3
        # m,n = map(len, [board, board[0]])
        seen = set()
        for i, row in enumerate(board) :
            for j, c in enumerate(row) :
                if(c != '.') :
                    row_key = (c,i)
                    col_key = (j,c)
                    inner_board_key = (i/3,j/3,c)
                    if(row_key in seen or col_key in seen or inner_board_key in seen) : return False
                    seen.add(row_key)
                    seen.add(col_key)
                    seen.add(inner_board_key)
        return True

#Shortest
def isValidSudoku(board) :
  seen=[x for i, row in enumerate(board)
               for j, c in enumerate(row)
                   if c!='.'
                       for x in ((c,i),(j,c),(i/3,j/3,c))]
   return len(seen)==len(set(seen))


##1. Check column grid:w

#[["8","3",".",".","7",".",".",".","."],
#["6",".",".","1","9","5",".",".","."],
#[".","9","8",".",".",".",".","6","."],
#["8",".",".",".","6",".",".",".","3"],
#["4",".",".","8",".","3",".",".","1"],
#["7",".",".",".","2",".",".",".","6"],
#[".","6",".",".",".",".","2","8","."],
#[".",".",".","4","1","9",".",".","5"],
#[".",".",".",".","8",".",".","7","9"]]
#
##2. Check row grid
#[
#["7",".",".",".","4",".",".",".","."],
#[".",".",".","8","6","5",".",".","."],
#[".","1",".","2",".",".",".",".","."],
#[".",".",".",".",".","9",".",".","."],
#[".",".",".",".","5",".","5",".","."],
#[".",".",".",".",".",".",".",".","."],
#[".",".",".",".",".",".","2",".","."],
#[".",".",".",".",".",".",".",".","."],
#[".",".",".",".",".",".",".",".","."]]
#
#
##3. Check x/3,y/3 grid
#[
#[".",".",".",".","5",".",".","1","."],
#[".","4",".","3",".",".",".",".","."],
#[".",".",".",".",".","3",".",".","1"],
#["8",".",".",".",".",".",".","2","."],
#[".",".","2",".","7",".",".",".","."],
#[".","1","5",".",".",".",".",".","."],
#[".",".",".",".",".","2",".",".","."],
#[".","2",".","9",".",".",".",".","."],
#[".",".","4",".",".",".",".",".","."]]
#
#
