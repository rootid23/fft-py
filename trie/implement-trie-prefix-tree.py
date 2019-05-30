#!/usr/bin/env python

#Implement a trie with insert, search, and startsWith methods.
#Note:
#You may assume that all inputs are consist of lowercase letters a-z.

#Trie - w/ only array of size 26
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        #apple,
        #predix
        #input size?
        #input spec?
        # ( [visited char, leaf], children )
        self.root = [ [-1,-1], [None] * 26 ]

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        tmpRoot  = self.root
        for c in word :
            idx = ord(c) - ord('a')
            #init
            if(tmpRoot[1][idx] == None) :
                tmpRoot[1][idx] = [ [-1,0], [None] * 26 ]
            #progress
            tmpRoot = tmpRoot[1][idx]
            #set
            if(tmpRoot[0][0] == -1) :
                tmpRoot[0][0] = 1
        tmpRoot[0][1] = -1

    def __find(self, word) :
        tmpRoot  = self.root
        for c in word :
            idx = ord(c) - ord('a')
            if(tmpRoot[1][idx] == None) : return None
            tmpRoot = tmpRoot[1][idx]
        return tmpRoot

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        tmpRoot = self.__find(word)
        if(tmpRoot == None) : return False
        return tmpRoot[0][1] == -1

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        tmpRoot = self.__find(prefix)
        if(tmpRoot == None) : return False
        return True

# W/ child as a array
class TrieNode(object):

  def __init__(self, x):
    self.node = x
    self.chlds = None
    self.isLeaf = False

class Trie(object):

  def __init__(self):
    self.root = TrieNode('')

  def insert(self, word):
    dmyNode = self.root
    for t in word:
      rnk = ord(t) - ord('a')
      if (dmyNode.chlds == None):
        dmyNode.chlds = [None] * 26
      if (dmyNode.chlds[rnk] == None):
        dmyNode.chlds[rnk] = TrieNode(rnk)  #apple for pp only create 1 node
      dmyNode = dmyNode.chlds[rnk]
    dmyNode.isLeaf = True

  def search(self, word):
    dmyNode = self.root
    for t in word:
      rnk = ord(t) - ord('a')
      if (dmyNode.chlds == None or dmyNode.chlds[rnk] == None):
        return False
      dmyNode = dmyNode.chlds[rnk]
    return dmyNode.isLeaf == True

  def startsWith(self, prefix):
    dmyNode = self.root
    for t in prefix:
      rnk = ord(t) - ord('a')
      if (dmyNode.chlds == None or dmyNode.chlds[rnk] == None):
        return False
      dmyNode = dmyNode.chlds[rnk]
    return True

## Python W/ childs as dictionary
class TrieNode:
  # Initialize your data structure here.
  def __init__(self):
    self.word = False
    self.children = {}

class Trie:

  def __init__(self):
    self.root = TrieNode()

  def insert(self, word):
    node = self.root
    for i in word:
      if i not in node.children:
        node.children[i] = TrieNode()
      node = node.children[i]
    node.word = True

  def search(self, word):
    node = self.root
    for i in word:
      if i not in node.children:
        return False
      node = node.children[i]
    return node.word

  def startsWith(self, prefix):
    node = self.root
    for i in prefix:
      if i not in node.children:
        return False
      node = node.children[i]
    return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

if __name__ == "__main__":
  main()
