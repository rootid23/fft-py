#Copy List with Random Pointer
#A linked list is given such that each node contains an additional random pointer which could point
#to any node in the
#list or null.
#Return a deep copy of the list.

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if (not head) : return head

        dNode = RandomListNode(-1)
        nxtNode = dNode

        #copy node with next reference directly
        lookupDict = {}

        while head :
            nxtNode.next = RandomListNode(head.label)
            nxtNode = nxtNode.next
            lookupDict[head] = nxtNode
            head = head.next

        #Copy randome references
        for oldNode in lookupDict.keys() :
            latestNode = lookupDict[oldNode]
            if oldNode.random :
                latestNode.random = lookupDict[oldNode.random]

        return dNode.next
