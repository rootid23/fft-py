
import threading

class Node(object) :
    def __init__(self, val) :
        self.val = val
        self.next = None

class LinkedList(object) :

    def __init__(self) :
        self.head = None
        self.tail = None
        self.it = None
        self.wrtLock = threading.Lock()

    def appendNode(self, val) :
        try :
          self.wrtLock.acquire()
          self._addToFront(val)
        finally :
          self.wrtLock.release()

    def _addToFront(self, val) :
      newNode = Node(val)
      newNode.next = self.head
      if(self.head == None) :
        self.tail = newNode
      self.head = newNode

    def __iter__(self) :
      # print('init')
      self.it = self.head
      return self

    def __next__(self) :
      if(self.it) :
        ret = self.it.val
        self.it = self.it.next
        return ret
      raise StopIteration()       # there are no more elements

    def next(self) :
       return self.__next__()

    def getHead(self):
        try :
          self.wrtLock.acquire()
          return self.head
        finally :
          self.wrtLock.release()

    def getTail(self) :
        try :
          self.wrtLock.acquire()
          return self.tail
        finally :
          self.wrtLock.release()


head = LinkedList()
head.appendNode(10)
head.appendNode(200)
print(head.getHead().val)

for i in head :
  print(i)
