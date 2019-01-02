
class Solution(object):
    def longestConsecutive(self, root):
        #parent->child
        #start or end at any node
        #Think of boottup
        #each node contriute leght 1
        #parent->child relation
        self.ans = 0
        def lchelper(root) :
            if(not root) :
                return [0, 0]
            d_lt = lchelper(root.left) #from down node
            d_rt = lchelper(root.right) # from
            c_inc, c_dec = 1,1
            if(root.left) :
                if(root.left.val == root.val + 1) :
                    c_inc = d_lt[0] + 1
                elif(root.left.val == root.val - 1) :
                    c_dec = d_lt[1] + 1
            if(root.right) :
                if(root.right.val == root.val + 1) :
                    c_inc = max(c_inc, d_rt[0] + 1)
                elif(root.right.val == root.val - 1) :
                    c_dec = max(c_dec, d_rt[1] + 1)
            local_max = c_inc + c_dec - 1
            self.ans = max(self.ans, local_max)
            return [c_inc, c_dec]
        lchelper(root)
        return self.ans
        """
        :type root: TreeNode
        :rtype: int
        """

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#Binary Tree Longest Consecutive Sequence II
#Given a binary tree, you need to find the length of Longest Consecutive Path in Binary Tree.
#Especially, this path can be either increasing or decreasing. For example, [1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is not valid. On the other hand, the path can be in the child-Parent-child order, where not necessarily be parent-child order.
#Example 1:
#Input:
#        1
#       / \
#      2   3
#Output: 2
#Explanation: The longest consecutive path is [1, 2] or [2, 1].
#Example 2:
#Input:
#        2
#       / \
#      1   3
#Output: 3
#Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].
#Note: All the values of tree nodes are in the range of [-1e7, 1e7].
