
#Flatten Binary Tree to Linked List
#Given a binary tree, flatten it to a linked list in-place.
#For example,
#Given
#         1
#        / \
#       2   5
#      / \   \
#     3   4   6
#The flattened tree should look like:
#   1
#    \
#     2
#      \
#       3
#        \
#         4
#          \
#           5
#            \
#             6


class Solution(object):

    def flatten(self, root):

        if(not root) : return
        tmp = root.right
        root.right = root.left
        root.left = None
        v = root
        while v.right:
            v = v.right
        v.right = tmp
        self.flatten(root.right)
