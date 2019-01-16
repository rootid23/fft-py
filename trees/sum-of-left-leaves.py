#Top-down w/ auxillary flag
class Solution(object):
    def sumOfLeftLeaves(self, root):
        #how to determin leaft leave?
        #BFS - > can't deter

        def slhelper(root, islt) :
            sum_ = 0
            if(not root) :
                return sum_
            if(not root.left and not root.right and islt) :
                sum_ += root.val
            sum_ += slhelper(root.left, True)
            sum_ += slhelper(root.right, False)
            return sum_

        return slhelper(root, False)

#Sum of Left Leaves
#Find the sum of all left leaves in a given binary tree.
#Example:
#    3
#   / \
#  9  20
#    /  \
#   15   7
#There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
