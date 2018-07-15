
#Recursion
# Deserialize = Preorder + Inorder
# Serialize = Preorder

#Serialization: generate space separated pre-order traversal string
#Deserialization: get in-order traversal string by sorting & generate the tree based on in-order and pre-order sequences

class Codec:
    def serialize(self, root):
        def preorder(node):
            if node:
                vals.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
        vals = []
        preorder(root)
        return ' '.join(vals)

    def deserialize(self, data):
        preorder = map(int, data.split())
        inorder = sorted(preorder)
        return self.buildTree(preorder, inorder)

    def buildTree(self, preorder, inorder):
        def build(stop):
            if inorder and inorder[-1] != stop:
                root = TreeNode(preorder.pop())
                root.left = build(root.val)
                inorder.pop()
                root.right = build(stop)
                return root
        preorder.reverse()
        inorder.reverse()
        return build(None)


#Serialize and Deserialize BST
#Serialization is the process of converting a data structure or object into a
#sequence of bits so that it can be stored in a file or memory buffer, or
#transmitted across a network connection link to be reconstructed later in the
#same or another computer environment.
#Design an algorithm to serialize and deserialize a binary search tree. There
#is no restriction on how your serialization/deserialization algorithm should
#work. You just need to ensure that a binary search tree can be serialized to
#a string and this string can be deserialized to the original tree structure.
#The encoded string should be as compact as possible.
#Note: Do not use class member/global/static variables to store states. Your
#serialize and deserialize algorithms should be stateless.
