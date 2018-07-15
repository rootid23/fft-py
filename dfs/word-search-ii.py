
#Trie in python way
class Solution:
    # @param {character[][]} board
    # @param {string[]} words
    # @return {string[]}
    def findWords(self, board, words):
        #make trie please refer
        trie={}
        for w in words:
            t=trie
            for c in w:
                if c not in t:
                    t[c]={}
                t=t[c]
            t['#']='#'

        self.res=set()

        self.used=[[False]*len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.find(board,i,j,trie,'')
        return list(self.res)

    def find(self,board,i,j,trie,pre):
        if '#' in trie:
            self.res.add(pre)
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]):
            return
        if not self.used[i][j] and board[i][j] in trie:
            self.used[i][j]=True
            self.find(board,i+1,j,trie[board[i][j]],pre+board[i][j])
            self.find(board,i,j+1,trie[board[i][j]],pre+board[i][j])
            self.find(board,i-1,j,trie[board[i][j]],pre+board[i][j])
            self.find(board,i,j-1,trie[board[i][j]],pre+board[i][j])
            self.used[i][j]=False




#Complex number + py
class Solution:
    def findWords(self, board, words):

        root = {}
        for word in words:
            node = root
            for c in word:
                node = node.setdefault(c, {})
            node[None] = True
        board = {i + 1j*j: c
                 for i, row in enumerate(board)
                 for j, c in enumerate(row)}

        found = []
        def search(node, z, word):
            if node.pop(None, None):
                found.append(word)
            c = board.get(z)
            if c in node:
                board[z] = None
                for k in range(4): #//4 directions
                    search(node[c], z + 1j**k, word + c)
                board[z] = c
        for z in board:
            search(root, z, '')
        return found


#Word Search II
#Given a 2D board and a list of words from the dictionary, find all words in
#the board.
#Each word must be constructed from letters of sequentially adjacent cell,
#where "adjacent" cells are those horizontally or vertically neighboring. The
#same letter cell may not be used more than once in a word.
#For example,
#Given words = ["oath","pea","eat","rain"] and board =
#[
#  ['o','a','a','n'],
#  ['e','t','a','e'],
#  ['i','h','k','r'],
#  ['i','f','l','v']
#]
#Return ["eat","oath"].
#Note:
#You may assume that all inputs are consist of lowercase letters a-z.
#click to show hint.
#You would need to optimize your backtracking to pass the larger test. Could
#you stop backtracking earlier?
#If the current candidate does not exist in all words' prefix, you could stop
#backtracking immediately. What kind of data structure could answer such query
#efficiently? Does a hash table work? Why or why not? How about a Trie? If you
#would like to learn how to implement a basic trie, please work on this
#problem: Implement Trie (Prefix Tree) first.
