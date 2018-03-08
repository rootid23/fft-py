#Invert a binary tree.
#     4
#   /   \
#  2     7
# / \   / \
#1   3 6   9
#
# to
#     4
#   /   \
#  7     2
# / \   / \
#9   6 3   1


#Top-down traversal w/
#TC : O(h)
#SC : O(h)
class Solution(object):

  def invertTree(self, root):
    if root is None:
      return root
    #swap lt and rt nodes
    root.left, root.right = root.right, root.left
    lt = self.invertTree(root.left)
    rt = self.invertTree(root.right)
    return root

  #W/ map fn
  def invertTreeWithMap(self, root):
    if root is None:
      return root
    #swap lt and rt nodes
    root.left, root.right = root.right, root.left
    map(self.invertTreeWithMap, (root.left, root.right))
    return root

  #W/ BFS q
  def invertTreeWithQueue(self, root):
    if root:
      queue = [root]
      while queue:
        for each_node in queue:  # swap in the first lvl
          each_node.left, each_node.right = each_node.right, each_node.left
        #update queue
        queue = [
            nodes for node in queue for nodes in (node.left, node.right)
            if nodes
        ]
      return root
