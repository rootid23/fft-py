
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0

        def depth(p):
            if not p: return 0
            left, right = depth(p.left), depth(p.right)
            self.ans = max(self.ans, left+right)
            return 1 + max(left, right)

        depth(root)
        return self.ans

class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.ans = 1
        def depth(node):
            if not node: return 0
            L = depth(node.left)
            R = depth(node.right)
            self.ans = max(self.ans, L+R+1)
            return max(L, R) + 1

        depth(root)
        return self.ans - 1

# w/ stack - iterative solution
      def diameterOfBinaryTree(self, root):
        if not root: return 0
        d = {None: -1}
        s = [root]
        ans = 0
        while s:
            node = s[-1]
            print(node)
            print(d)
            if node.left in d and node.right in d:
                print(d)
                s.pop()
                l = d[node.left] + 1
                r = d[node.right] + 1
                ans = max(ans, l + r)
                d[node] = max(l, r)
            else:
                if node.left:
                    s.append(node.left)
                if node.right:
                    s.append(node.right)
        return ans

#Diameter of Binary Tree
#Given a binary tree, you need to compute the length of the diameter of the
#tree. The diameter of a binary tree is the length of the longest path between
#any two nodes in a tree. This path may or may not pass through the root.
#Example:
#Given a binary tree
#          1
#         / \
#        2   3
#       / \
#      4   5
#Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
#Note: The length of path between two nodes is represented by the number of
#edges between them.

# Postorder traversal #
#Let's calculate the depth of a node in the usual way: max(depth of node.left, depth of node.right)
#+ 1. While we do, a path "through" this node uses 1 + (depth of node.left) + (depth of node.right)
#nodes. Let's search each node and remember the highest number of nodes used in some path. The
#desired length is 1 minus this number.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
