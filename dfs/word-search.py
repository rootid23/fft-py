

#DFS
#Whether its BFS / DFS in order to avoid backedge store the parent
#eg. memo.add( (x,y) )  and then explore the childern
class Solution(object):

    def exist(self, board, word):

        if(not board) : return False
        m, n = map(len, [board, board[0]])

        idx_dict = {}
        for i in range(m) :
            for j in range(n) :
                if(board[i][j] not in idx_dict) :
                    idx_dict[ board[i][j] ] = [ ]
                idx_dict[ board[i][j] ] += [ (i,j) ]

        start = word[0]
        if(start not in idx_dict) : return False

        flst = idx_dict[start] #collect all the frontiers

        for fnt in flst :
            if (self.dfs(fnt, board, word) == True) :
                return True
        return False


    def dfs(self, fnt, board, word, idx=0, memo = set()) :
        wlen = len(word)
        if(idx == wlen) :
            return True
        m, n = map(len, [board, board[0]])

        (x,y) = fnt

        if( (x, y) in memo or \
                x >= m or y >= n or x < 0 or y < 0 or \
                word[idx] != board[x][y]) :

            return False

        memo.add( (x,y) )  #Store parent To avoid visiting backedge
        res = self.dfs( (x+1, y) , board, word, idx + 1, memo) or \
                self.dfs((x-1, y) , board, word, idx + 1, memo) or \
                self.dfs((x, y+1) , board, word, idx + 1, memo) or \
                self.dfs((x, y-1) , board, word, idx + 1, memo)
        memo.remove( (x,y) )
        return res


# In place DFS
#Avoid backedge
#board[i][j] = "#"  # avoid visit agian
def exist(self, board, word):
    if not board:
        return False
    for i in xrange(len(board)):
        for j in xrange(len(board[0])):
            if self.dfs(board, i, j, word):
                return True
    return False

# check whether can find word, start at (i,j) position
def dfs(self, board, i, j, word):
    if len(word) == 0: # all the characters are checked
        return True
    if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
        return False
    tmp = board[i][j]  # first character is found, check the remaining part
    board[i][j] = "#"  # avoid visit agian
    # check whether can find "word" along one direction
    res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
    or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
    board[i][j] = tmp
    return res



#Given a 2D board and a word, find if the word exists in the grid.
#The word can be constructed from letters of sequentially adjacent cell, where
#"adjacent" cells are those horizontally or vertically neighboring. The same
#letter cell may not be used more than once.
#For example,
#Given board =
#[
#  ['A','B','C','E'],
#  ['S','F','C','S'],
#  ['A','D','E','E']
#]
#word = "ABCCED", -> returns true,
#word = "SEE", -> returns true,
#word = "ABCB", -> returns false

