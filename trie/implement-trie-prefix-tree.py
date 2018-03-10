#!/usr/bin/env python

#Implement a trie with insert, search, and startsWith methods.
#Note:
#You may assume that all inputs are consist of lowercase letters a-z.


# W/ child as a array
class TrieNode(object):

  def __init__(self, x):
    self.node = x
    self.chlds = None
    self.isLeaf = False


class Trie(object):

  root = None

  def __init__(self):
    """
        Initialize your data structure here.
        """
    self.root = TrieNode('')

  def insert(self, word):
    """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
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
    """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
    dmyNode = self.root
    for t in word:
      rnk = ord(t) - ord('a')
      if (dmyNode.chlds == None or dmyNode.chlds[rnk] == None):
        return False
      dmyNode = dmyNode.chlds[rnk]
    return dmyNode.isLeaf == True

  def startsWith(self, prefix):
    """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
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

  # @param {string} word
  # @return {void}
  # Inserts a word into the trie.
  def insert(self, word):
    node = self.root
    for i in word:
      if i not in node.children:
        node.children[i] = TrieNode()
      node = node.children[i]
    node.word = True

  # @param {string} word
  # @return {boolean}
  # Returns if the word is in the trie.
  def search(self, word):
    node = self.root
    for i in word:
      if i not in node.children:
        return False
      node = node.children[i]
    return node.word

  # @param {string} prefix
  # @return {boolean}
  # Returns if there is any word in the trie
  # that starts with the given prefix.
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
