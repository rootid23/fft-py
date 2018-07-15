#Find Bottom Left Tree Value
#Given a binary tree, find the leftmost value in the last row of the tree.
#Example 1:
#Input:
#    2
#   / \
#  1   3
#Output:
#1
#Example 2:
#Input:
#        1
#       / \
#      2   3
#     /   / \
#    4   5   6
#       /
#      7
#Output:
#7


import collections
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if (not root) : return root
        q = collections.deque( [root] )
        last_left = root
        while q :
            pt_cnt = len(q)
            last_left = q[0] #peek left from the deque
            for _ in range(pt_cnt) :
                tmp = q.popleft()
                if(tmp.left) :
                    q += [tmp.left]
                if(tmp.right) :
                    q += [tmp.right]
        return last_left.val
