
#Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right
#to left for the next level and alternate between).
#For example:
#Given binary tree [3,9,20,null,null,15,7],
#    3
#   / \
#  9  20
#    /  \
#   15   7
#return its zigzag level order traversal as:
#[
#  [3],
#  [20,9],
#  [15,7]
#]


#Iterative + deque
import collections

def zig_zag(root) :

    if(not root) : return []

    vq, r = collections.deque() ,[]

    vq += [ root ]
    lvl = 0
    while vq :
        if(lvl % 2 == 1) :
            r += [node.val for node in vq]
        else :
            r += reversed ([node.val for node in vq] )
        number_of_parents = len(vq)
        for _ in range(number_of_parents):
            tmp = vq.popleft()
            if(tmp.left) :
                vq += [ tmp.left ]
            if(tmp.right) :
                vq += [ tmp.right ]
        lvl += 1

    return r
