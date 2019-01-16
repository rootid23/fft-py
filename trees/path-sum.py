
# DFS + stack
def hasPathSum(self, root, sum):
    stack = [(root, sum)]
    while stack:
        node, value = stack.pop()
        if node:
            if not node.left and not node.right and node.val == value:
                return True
            stack.append((node.right, value-node.val))
            stack.append((node.left, value-node.val))
        else:
            continue
    return False

#Top down short circuit operator
class Solution(object):
    def hasPathSum(self, root, sum):
        #top down -> Why ? can prune easily

        if(not root) : return False
        #Pruning
        #if(sum - root.val < 0) : return False
        sum -= root.val
        if(sum == 0 and not root.left and not root.right) : return True
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)


#Path Sum
#Given a binary tree and a sum, determine if the tree has a root-to-leaf path
#such that adding up all the values along the path equals the given sum.
#For example:
#Given the below binary tree and sum = 22,
#              5
#             / \
#            4   8
#           /   / \
#          11  13  4
#         /  \      \
#        7    2      1
#return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
