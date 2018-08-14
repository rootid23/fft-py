#Reverse a singly linked list.
#click to show more hints.
#Hint:
#A linked list can be reversed either iteratively or recursively. Could you implement both?


#Iterative
class Solution(object):

  def reverseList(self, head):
    if (head == None or head.next == None):
      return head
    nxtHead = None
    while (head != None):
      tmp = head.next
      head.next, nxtHead = nxtHead, head
      head = tmp
    return nxtHead


#Recursive
#n1 → … → nk-1 → nk → nk+1 ← … ← nm
#1. nk+1 shud point to nk i.e. nk.next.next = nk
#2. nk.next = null
def reverseList(self, head):
  if (head == None or head.next == None):
    return head
  tmp = self.reverseList(head.next)
  head.next.next, head.next = head, None  #Fix GrandChild and then child
  return tmp
