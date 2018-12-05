#Merge k Sorted Lists
#Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
#Example:
#Input:
#[
#  1->4->5,
#  1->3->4,
#  2->6
#]
#Output: 1->1->2->3->4->4->5->6

# W/ Priority queue
from Queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        #constraint -
        #1. Space?
        #2. Static/streaming?

        #Idea
        #1. Iterate over the rows + put values and references last visited referces into the list
        #2. divide the list and merge

        #1. Store only heads at the frontier
        pq = PriorityQueue()

        for h in lists :
            if h :
                pq.put( (h.val, h) )
        nh = ListNode(-1)
        tmp = nh
        while not pq.empty():
            (v, node) = pq.get()
            tmp.next = ListNode(v)
            tmp = tmp.next
            node = node.next
            if node :
                pq.put( (node.val, node) )

        return nh.next


