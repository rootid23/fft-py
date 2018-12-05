#We are given the head node root of a binary tree, where additionally every node's value is either a 0 or a 1.
#Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.
#(Recall that the subtree of a node X is X, plus every node that is a descendant of X.)
#Example 1:
#Input: [1,null,0,0,1]
#Output: [1,null,0,null,1]
#
#Explanation:
#Only the red nodes satisfy the property "every subtree not containing a 1".
#The diagram on the right represents the answer.
#Example 2:
#Input: [1,0,1,0,0,0,1]
#Output: [1,null,1,null,1]
#Example 3:
#Input: [1,1,0,1,1,0,1,0]
#Output: [1,1,0,1,1,null,1]
#Note:
#    The binary tree will have at most 100 nodes.
#    The value of each node will only be 0 or 1.

from collections import deque

class Solution(object):
    def pruneTree(self, root):
        #remove 0 leaf node
        #remove substree containg 0
        #how to detect the substree with 0's
        #is it read only tree?
        #can we mutate the tree?
        #will it fit in memory?

        #how to locate the substrees with all 0s
        #locate the nodes with 0 node and then reverse and find out

        #1. Scan tree with BFS and simulatneously
        #2. Find the root with 0 substree and make it empty

        def is_node_zero(root) :
            if(not root) : return True
            if(root.val == 1) : return False
            return is_node_zero(root.left) and is_node_zero(root.right)

        q = deque([root])
        while q :
            tmp = q.popleft()
            if(is_node_zero(tmp.left)) :
                tmp.left = None
            if(is_node_zero(tmp.right)) :
                tmp.right = None
            if(tmp.left) :
                q += [tmp.left]
            if(tmp.right) :
                q += [tmp.right]

        return root



