#Same Tree
#Given two binary trees, write a function to check if they are equal or not.
#Two binary trees are considered equal if they are structurally identical and
#the nodes have the same value.
#Example 1:
#Input:     1         1
#          / \       / \
#         2   3     2   3
#        [1,2,3],   [1,2,3]
#Output: true
#Example 2:
#Input:     1         1
#          /           \
#         2             2
#        [1,2],     [1,null,2]
#Output: false
#Example 3:
#Input:     1         1
#          / \       / \
#         2   1     1   2
#        [1,2,1],   [1,1,2]
#Output: false
class Solution(object):
    def isSameTree(self, p, q):
        #struct and values must be same
        if(not p and not q) : return True
        if( (not p and q) or  (p and not q) ) : return False
        return p.val == q.val \
                 and self.isSameTree(p.left, q.left) \
                 and self.isSameTree(p.right, q.right)

#W/stack
class Solution_iterative_DFS:
    def isSameTree(self, p, q):
        stack = [(p, q)]
        while stack:
            node1, node2 = stack.pop()
            if node1 and node2 and node1.val == node2.val:
                stack.append((node1.left, node2.left))
                stack.append((node1.right, node2.right))
            else:
                if not node1 == node2:
                    return False
        return True
