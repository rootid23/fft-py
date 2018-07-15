

#"next" and "prev" ptr associated with it. Just use the property of a BST and restructure tree so
#that all greater elements will be in a "flattened" right subtree.

def convert(root):
    if not root: return

    if root.left:
        # find inorder predecessor
        p = root.left

        while p.right:
          p = p.right

        # restructure tree
        temp, root.left, p.right = root.left, None, root

        return convert(temp)
    # Assigning pointers
    root.next = convert(root.right)
    if root.next: root.next.prev = root
    return root



#divide and conquer
#convert into Circular doubly linked list

# helper function -- given two list nodes, join them
# together so the second immediately follow the first.
# Sets the .next of the first and the .previous of the second.
def join(a, b) :
    a.right = b
    b.left = a

# helper function -- given two circular doubly linked
# lists, append them and return the new list.
def append(a, b) :
    # if either is None, return the other
    if (not a): return(b)
    if (not b): return(a)

    # find the last node in each using the .previous pointer
    aLast = a.left
    bLast = b.left

    # join the two together to make it connected and circular
    join(aLast, b)
    join(bLast, a)

    return(a)


# --Recursion--
# Given an ordered binary tree, recursively change it into
# a circular doubly linked list which is returned.
def treeToList(root) :
    # base case: empty tree -> empty list
    if (not root): return None

    # Recursively do the subtrees (leap of faith!)
    aList = treeToList(root.left)
    bList = treeToList(root.right)

    # Make the single root node into a list length-1
    # in preparation for the appending
    root.left = root
    root.right = root

    # At this point we have three lists, and it's
    # just a matter of appending them together
    # in the right order (aList, root, bList)
    aList = append(aList, root)
    aList = append(aList, bList)

    return(aList)

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root, root.left, root.right,root.left.left, root.left.right = TreeNode(4), TreeNode(2), TreeNode(5), TreeNode(1), TreeNode(3)

head = treeToList(root)

tmp = head
while tmp :
  print tmp.val
  tmp = tmp.right
  if(tmp == head) : break




#Recursion


# This is a modified in-order traversal adapted to this problem.
# prev (init to NULL) is used to keep track of previously traversed node.
# head pointer is updated with the list's head as recursion ends.

prev = None
head = None

def treeToDoublyListHelper(p) :
  global prev, head
  if (not p) : return
  treeToDoublyListHelper(p.left)
  # current node's left points to previous node
  p.left = prev
  if (prev) :
    prev.right = p  # previous node's right points to current node
  else :
    head = p # current node (smallest element) is head of
              # the list if previous node is not available
  # as soon as the recursion ends, the head's left pointer
  # points to the last node, and the last node's right pointer
  # points to the head pointer.
  right = p.right
  head.left = p
  p.right = head
  # updates previous node
  prev = p
  treeToDoublyListHelper(right)

# Given an ordered binary tree, returns a sorted circular
# doubly-linked list. The conversion is done in-place.
def treeToDoublyList(root) :
  treeToDoublyListHelper(root)
  return head
