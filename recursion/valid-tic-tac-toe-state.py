class Solution(object):
    def validTicTacToe(self, board):
        #Case analysis
        #XOX
        #O O
        #XOX

        #XOX
        # X
        #

        #3X3?

        #first player X
        #non-empty
    def validTicTacToe(self, board):
        FIRST, SECOND = 'XO'
        x_count = sum(row.count(FIRST) for row in board)
        o_count = sum(row.count(SECOND) for row in board)
        def win(board, player):

            for i in xrange(3):
                #Check Row
                if all(board[i][j] == player for j in xrange(3)):
                    return True

                #check column
                if all(board[j][i] == player for j in xrange(3)):
                    return True

            #check diagonal
            return (player == board[1][1] == board[0][0] == board[2][2] or
                    player == board[1][1] == board[0][2] == board[2][0])
        if(o_count > x_count or x_count - o_count > 1) : return False

        #If o is wining
        if(win(board, 'O')) :
            if(win(board, 'X')) : return False
            return o_count == x_count

        #If x is wininning
        if win(board, 'X') and x_count != o_count+1: #Since player X plays the first move, if player X wins, the player X's count would be 1 more than player O
            return False
        return True


#Valid Tic-Tac-Toe State
#A Tic-Tac-Toe board is given as a string array board. Return True if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.
#The board is a 3 x 3 array, and consists of characters " ", "X", and "O".  The " " character represents an empty square.
#Here are the rules of Tic-Tac-Toe:
#    Players take turns placing characters into empty squares (" ").
#    The first player always places "X" characters, while the second player always places "O" characters.
#    "X" and "O" characters are always placed into empty squares, never filled ones.
#    The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
#    The game also ends if all squares are non-empty.
#    No more moves can be played if the game is over.
#Example 1:
#Input: board = ["O  ", "   ", "   "]
#Output: false
#Explanation: The first player always plays "X".
#Example 2:
#Input: board = ["XOX", " X ", "   "]
#Output: false
#Explanation: Players take turns making moves.
#Example 3:
#Input: board = ["XXX", "   ", "OOO"]
#Output: false
#Example 4:
#Input: board = ["XOX", "O O", "XOX"]
#Output: true
#Note:
#    board is a length-3 array of strings, where each string board[i] has length 3.
#    Each board[i][j] is a character in the set {" ", "X", "O"}.
