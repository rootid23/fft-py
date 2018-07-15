
#Preorder save
#Use of iter and next
#recursion
#[1,2,3,null,null,4,5]
#1 2 # # 3 4 # # 5 # #

class Codec:
    def serialize(self, root):
        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')
        vals = []
        doit(root)
        return ' '.join(vals)

    def deserialize(self, data):
        def doit():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node
        vals = iter(data.split())
        return doit()


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        if (not root) :
            return "#"
        st = str(root.val) + ','
        st += self.serialize(root.left) + ','
        st += self.serialize(root.right)

        return st

    def deserialize(self, data):

        lst = data.split(',')
        def doit():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node
        #NOTE : use of iterator
        vals = iter(lst)
        return doit()


#append with None and prepend with ,
#[1,2,3,null,null,4,5]
#,1,2,3,None,None,4,5,None,None,None,None


from collections import deque

class Codec:

    def serialize(self, root):
        string = ""
        queue = deque([root])
        while queue:
            cur = queue.popleft()
            if not cur:
                string += ",None"
                continue
            else:
                string += "," + str(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)
        return string

    def deserialize(self, data):
        data = deque(data.split(","))
        _, val = data.popleft(), data.popleft()
        root = None if val == "None" else TreeNode(int(val))
        queue = deque([root])
        while queue:
            cur = queue.popleft()
            if cur:
                a, b = data.popleft(), data.popleft()
                cur.left = TreeNode(int(a)) if a != "None" else None
                cur.right = TreeNode(int(b)) if b != "None" else None
                queue.append(cur.left)
                queue.append(cur.right)
        return root

#iterative w/ q
class Codec:

    def serialize(self, root):
        code, queue = "", [root]
        for node in queue:
            code += "," * (node != root) + "#" * (not node) + (str(node.val) if node else "")
            if node: queue += node.left, node.right,
        return code

    def deserialize(self, data):
        data = collections.deque(data.split(","))
        val = data.popleft()
        root = TreeNode(int(val)) if val != "#" else None
        queue = [root]
        for node in queue:
            if not node: continue
            l, r = data.popleft(), data.popleft()
            node.left  = TreeNode(int(l)) if l != "#"  else None
            node.right = TreeNode(int(r)) if r != "#" else None
            queue += node.left, node.right,
        return root

#Serialize and Deserialize Binary Tree
#Serialization is the process of converting a data structure or object into a
#sequence of bits so that it can be stored in a file or memory buffer, or
#transmitted across a network connection link to be reconstructed later in the
#same or another computer environment.
#
#Design an algorithm to serialize and deserialize a binary tree. There is no
#restriction on how your serialization/deserialization algorithm should work.
#You just need to ensure that a binary tree can be serialized to a string and
#this string can be deserialized to the original tree structure.
#
#For example, you may serialize the following tree
#
#    1
#   / \
#  2   3
#     / \
#    4   5
#as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a
#binary tree. You do not necessarily need to follow this format, so please be
#creative and come up with different approaches yourself.
#Note: Do not use class member/global/static variables to store states. Your
#serialize and deserialize algorithms should be stateless.
