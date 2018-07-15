
#Given preorder and inorder traversal of a tree, construct the binary tree.
#Note:
#You may assume that duplicates do not exist in the tree.
#For example, given
#preorder = [3,9,20,15,7]
#inorder = [9,3,15,20,7]
#Return the following binary tree:
#    3
#   / \
#  9  20
#    /  \
#   15   7

class Solution(object):


    def buildTree(self, preorder, inorder):


        if not preorder or not inorder:
            return None

        root = TreeNode(preorder.pop(0))
        ind = inorder.index(root.val)
        root = TreeNode(inorder[ind])
        root.left = self.buildTree(preorder, inorder[0:ind])
        root.right = self.buildTree(preorder, inorder[ind+1:])
        return root

