#W/ dummy head - How to handle the 2 way insertion and deletion
#Must see
#1. How to initialize
#Use the dummyhead as a anchor node
#How to use __str__
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dummyHead = Node(0)
        self.tail = None
        self.size = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index >= self.size:
            return -1
        node = self.getIthNode(index)
        if node is None: return -1
        return node.next.val


    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion,
the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        node = Node(val)
        if self.dummyHead.next is None:
            self.tail = node
        node.next = self.dummyHead.next
        self.dummyHead.next = node
        self.size += 1


    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        if self.tail is None:
            self.addAtHead(val)
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next
            self.size += 1


    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the
length of linked list, the node will be appended to the end of linked list. If index is greater than
the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index > self.size:
            return
        node = self.getIthNode(index)
        if node.next is None:
            self.addAtTail(val)
        else:
            nodeToInsert = Node(val)
            nodeToInsert.next = node.next
            node.next = nodeToInsert
            self.size += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index >= self.size:
            return None
        node = self.getIthNode(index)
        node.next = node.next.next
        if node.next is None:
            self.tail = node
        self.size -= 1

    def getIthNode(self, index):
        node = self.dummyHead
        for i in range(index):
            node = node.next
        return node

#W/ head and tail nodes
class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        """Create an empty list."""
        self._head = None
        self._tail = None
        self._size = 0

    def get(self, index):
        """Get the value of the index-th node in the linked list.
        If the index is invalid, return -1."""

        if index < 0 or index >= self._size:
            return -1
        #print(self)
        current = self._head
        for _ in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val):
        """Add a node of value val before the first element of the list."""
        new_head = Node(val)
        if self._size == 0:
            self._head = new_head
            self._tail = self._head
        else:
            new_head.next = self._head
            self._head = new_head
        self._size += 1

    def addAtTail(self, val):
        """Add a node of value val after the last element of the list."""
        new_tail = Node(val)
        if self._size == 0:
            self._head = new_head
            self._tail = self._head
        else:
            self._tail.next = new_tail
            self._tail = new_tail
        self._size += 1

    def addAtIndex(self, index, val):
        """Add a node of value val before the index-th node in the list.
        If the index equals the length of the list, the node will be appended
        to the end of the list. If the index is greater than the length, the
        node will not be inserted."""
        if index < 0 or index > self._size:
            return
        elif index == 0:
            self.addAtHead(val)
            return
        elif index == self._size:
            self.addAtTail(val)
            return

        current = self._head
        for _ in range(index - 1):
            current = current.next
        new_node = Node(val)
        new_node.next = current.next
        current.next = new_node
        self._size += 1

    def deleteHead(self):
        """Remove the first node in the list, if any."""
        if not self._head:
            return

        if self._head is self._tail:
            self._head = None
            self._tail = None
        else:
            self._head = self._head.next
        self._size -= 1

    def deleteTail(self):
        """Remove the last node in the list, if any."""
        if not self._tail:
            return

        if self._head is self._tail:
            self._head = None
            self._tail = None
        else:
            current = self._head
            while current.next != self._tail:
                current = current.next
            current.next = None
            self._tail = current
        self._size -= 1


    def deleteAtIndex(self, index):
        """Remove the index-th node in the list, if the index is valid."""
        if index < 0 or index >= self._size:
            return
        elif index == 0:
            self.deleteHead()
            return
        elif index == self._size - 1:
            self.deleteTail()
            return

        current = self._head
        for _ in range(index - 1):
            current = current.next
        current.next = current.next.next
        self._size -= 1

    def __str__(self):
        """Return a string representation of the list."""
        elements = []
        current = self._head
        while current:
            elements.append(str(current.val))
            current = current.next
        return ' -> '.join(elements)


#Design Linked List
#Design your implementation of the linked list. You can choose to use the singly linked list or the
#doubly linked list. A node in a singly linked list should have two attributes: val and next. val is
#the value of the current node, and next is a pointer/reference to the next node. If you want to use
#the doubly linked list, you will need one more attribute prev to indicate the previous node in the
#linked list. Assume all nodes in the linked list are 0-indexed.
#Implement these functions in your linked list class:
#get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return
#-1.
#addAtHead(val) : Add a node of value val before the first element of the linked list. After the
#insertion, the new node will be the first node of the linked list.
#addAtTail(val) : Append a node of value val to the last element of the linked list.
#addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list. If
#index equals to the length of linked list, the node will be appended to the end of linked list. If
#index is greater than the length, the node will not be inserted.
#deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.
#Example:
#MyLinkedList linkedList = new MyLinkedList();
#linkedList.addAtHead(1);
#linkedList.addAtTail(3);
#linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
#linkedList.get(1);            // returns 2
#linkedList.deleteAtIndex(1);  // now the linked list is 1->3
#linkedList.get(1);            // returns 3
#Note:
#All values will be in the range of [1, 1000].
#The number of operations will be in the range of [1, 1000].
#Please do not use the built-in LinkedList library.
