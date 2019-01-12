
#Recursive solution
def isSymmetric(self, root):


    #top - down
    #structure and value
    def isSHelper(lt, rt) :
        if(not lt and not rt) :
            return True
        if(lt and rt and lt.val == rt.val) :
            return isSHelper(lt.left, rt.right) and isSHelper(lt.right, rt.left)
        return False

    if(not root) : return True
    return isSHelper(root.left, root.right)

#Iterative solution
import collections
class Solution:
    def isSymmetric(self, root):
        if not root :
            return True
        q = collections.deque([root.left, root.right])

        while q :
            t1, t2 = q.popleft(), q.popleft()
            if not t1 and not t2 :
                continue
            if not t1 or not t2 or (t1.val != t2.val) : return False

            q += [t1.left, t2.right, t1.right, t2.left]
        return True


#101. Symmetric Tree
#Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#    1
#   / \
#  2   2
# / \ / \
#3  4 4  3
#But the following [1,2,2,null,3,null,3] is not:
#    1
#   / \
#  2   2
#   \   \
#   3    3
