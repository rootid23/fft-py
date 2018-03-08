
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def oddEvenList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    dmyNdE = ListNode(-1)
    dmyNdo = ListNode(-1)
    tmpDmyE = dmyNdE
    tmpDmyo = dmyNdo
    idx = 0
    while head is not None:
      if(idx%2 == 0) :
          tmpDmyE.next = head
          tmpDmyE = tmpDmyE.next
      else :
          tmpDmyo.next = head
          tmpDmyo = tmpDmyo.next
      head = head.next
      idx += 1
    tmpDmyo.next = None
    tmpDmyE.next = dmyNdo.next
    return dmyNdE.next


# vim: ai ts=2 sts=2 et sw=2 tw=100 fdm=indent fdl=1
