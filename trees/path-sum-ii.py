#Path Sum II
#Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given
#sum.
#Note: A leaf is a node with no children.
#Example:
#Given the below binary tree and sum = 22,
#      5
#     / \
#    4   8
#   /   / \
#  11  13  4
# /  \    / \
#7    2  5   1
#Return:
#[
#   [5,4,11,2],
#   [5,8,4,5]
#]


class Solution(object):
    def pathSum(self, root, sum):
        def pshelp(root, sum_, lst) :
            rst = []

            if(root and not root.left and not root.right and sum_ == root.val) :
                lst += [ root.val ]
                rst += [ lst[:] ]
                lst.pop()
                return rst
            if(root) :

                rst += pshelp(root.left, sum_ - root.val, lst + [root.val])
                rst += pshelp(root.right, sum_ - root.val, lst + [root.val])

            return rst


        return pshelp(root, sum, [])

#
def pathSum2(self, root, sum):
    if not root:
        return []
    if not root.left and not root.right and sum == root.val:
        return [[root.val]]
    tmp = self.pathSum(root.left, sum-root.val) + self.pathSum(root.right, sum-root.val)
    return [[root.val]+i for i in tmp]

class Solution(object):

    def pathSum(self, root, sum):

        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        #How to pick intermediate node and put in list
        def pathSumHelper(root, sum, lst, rst) :
            if(root) :
                if(not root.left and not root.right and sum == root.val) :
                    lst.append(root.val)
                    rst.append(lst)
                if(root.left) :
                    pathSumHelper(root.left, sum - root.val, lst+[root.val], rst)
                if(root.right) :
                    pathSumHelper(root.right, sum - root.val, lst+[root.val], rst)
            return rst

        return pathSumHelper(root, sum ,[], [])

#W/ deque
from collections import deque
class Solution(object):

    # BFS + deque
    def pathSum(self, root, sum):
        if not root:
            return []
        res = []
        queue = deque ( [(root, root.val, [root.val])])
        while queue:
            curr, val, ls = queue.popleft()
            if not curr.left and not curr.right and val == sum:
                res.append(ls)
            if curr.left:
                queue += [ ((curr.left, val+curr.left.val, ls+[curr.left.val]))]
            if curr.right:
                queue += [ ((curr.right, val+curr.right.val, ls+[curr.right.val])) ]
        return res

