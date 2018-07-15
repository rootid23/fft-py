#Lowest Common Ancestor of a Binary Tree
#Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
#According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as
#the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”
#        _______3______
#       /              \
#    ___5__          ___1__
#   /      \        /      \
#   6      _2       0       8
#         /  \
#         7   4
#For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5,
#since a node can be a descendant of itself according to the LCA definition.


#Recursive
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root :
            return root
        if(p == root or q == root) : return root

        ltsign = self.lowestCommonAncestor(root.left, p, q)
        rtsign = self.lowestCommonAncestor(root.right, p, q)

        #p and q are on oppsite side
        if( (ltsign == p and rtsign == q)  or (ltsign == q and rtsign == p) ) :
            return root

        #p and q are on same side
        if(not ltsign) : return rtsign #if rtsign is above ltsign
        return ltsign

#Iterative
def lowestCommonAncestor(self, root, p, q):
    stack = [root]
    parent = {root: None}
    while p not in parent or q not in parent:
        node = stack.pop()
        if node.left:
            parent[node.left] = node
            stack.append(node.left)
        if node.right:
            parent[node.right] = node
            stack.append(node.right)
    ancestors = set()
    while p:
        ancestors.add(p)
        p = parent[p]
    while q not in ancestors:
        q = parent[q]
    return q

