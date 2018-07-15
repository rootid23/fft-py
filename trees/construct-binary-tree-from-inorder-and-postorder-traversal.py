#Given inorder and postorder traversal of a tree, construct the binary tree.
#Note:
#You may assume that duplicates do not exist in the tree.
#For example, given
#inorder = [9,3,15,20,7]
#postorder = [9,15,7,20,3]
#Return the following binary tree:
#    3
#   / \
#  9  20
#    /  \
#   15   7


class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node

    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None

        root = TreeNode(postorder.pop())
        inIdx = inorder.index(root.val)

        #NOTE :  right first and later left
        root.right = self.buildTree(inorder[inIdx+1:], postorder)
        root.left = self.buildTree(inorder[0:inIdx], postorder)

        return root
