#!/usr/bin/env python

#constrnt :
#1. How many chars in the string
#2. ascii?
#3. Case sensitive?
#4. White space characters?
#Ida
#1.

def isPalindorme(s) :
  m = len(s)
  s = s.lower()
  if(m <= 1) : return True
  strt = 0
  end = m-1
  while strt < end :
    if(s[strt] != s[end]) : return False
    strt += 1
    end -= 1
  return True


#cnstrnt :
#1. Will -ve number
#2. Will it contain float?
#3. Is it integer/ real number/ float?

#12321 -> first - last , remainder
def isPalindormeNum(s) :
   return isPalindorme(str(s))

#symmetric
#1. values and structures are same


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

## Recursive version
class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if(root == None) :  return True

        # compare outer and inner paier
        def isSymmetricHelper(lt, rt) :
            if(not lt and not rt) : return True #both are None
            if(not lt or not rt) : return False
            #outer - isSymmetricHelper(lt.left, rt.right), inner - isSymmetricHelper(lt.right, rt.left)
            #visualize
            return lt.val == rt.val and isSymmetricHelper(lt.left, rt.right) and isSymmetricHelper(lt.right, rt.left)


        return isSymmetricHelper(root.left, root.right)

## Iterative version
import collections
class Solution:
    def isSymmetric(self, root):
        if not root:
            return True

        q = collections.deque([root.left, root.right])

        while q:
            t1, t2 = q.popleft(), q.popleft()

            if not t1 and not t2:
                continue
            elif (not t1 or not t2) or (t1.val != t2.val):
                return False

            q += [t1.left, t2.right, t1.right, t2.left]

        return True




if __name__ == '__main__':
  print('Running Test cses.')
  assert isPalindorme("unique") == False
  assert isPalindorme("aba") == True
  assert isPalindorme("Aba") == True
  assert isPalindorme("Aa") == True
  print('Done.')

  print('Running Test cses for numbers')
  assert isPalindormeNum(1234) == False
  assert isPalindormeNum(12321) == True
  print('Done.')
