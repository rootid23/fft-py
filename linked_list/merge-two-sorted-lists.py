
#Iteration trick to process the 2 nodes
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if(not l1) : return l2 #Base case
        if(not l2) : return l1
        dl3 = ListNode(42)
        l3 = dl3
        while(l1 or l2) :
            if(not l2 or (l1 and l1.val < l2.val) ) :
                l3.next = l1
                l1 = l1.next
            else :
                l3.next = l2
                l2 = l2.next
            l3 = l3.next
        return dl3.next


#Recursion
def mergeTwoLists(self, l1, l2):
    if(not l1) : return l2 #Base case - Do nothing case
    if(not l2) : return l1
    l3 = None
    if(l1 and l2) :
        if(l1.val < l2.val) :
            l3 = l1
            l3.next = self.mergeTwoLists(l1.next, l2)
        else :
            l3 = l2
            l3.next = self.mergeTwoLists(l1, l2.next)
    return l3


#Update reference trick
#Iteration
def mergeTwoLists(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if(not l1) : return l2
    if(not l2) : return l1
    dl3 = ListNode(-1)
    l3 = dl3
    while(l1 and l2) :
        if(l1.val > l2.val) :
            l3.next = l2
            l2 = l2.next
        else :
            l3.next = l1
            l1 = l1.next
        l3 = l3.next
   #As we just update the reference
    if(l1) :
        l3.next = l1
    if(l2) :
        l3.next = l2
    #l3.next = None
    return dl3.next

#Merge Two Sorted Lists
#Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
#Example:
#Input: 1->2->4, 1->3->4
#Output: 1->1->2->3->4->4
