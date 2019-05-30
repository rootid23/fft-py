#LRU Cache
#Design and implement a data structure for Least Recently Used (LRU) cache. It
#should support the following operations: get and put.
#get(key) - Get the value (will always be positive) of the key if the key
#exists in the cache, otherwise return -1.
#put(key, value) - Set or insert the value if the key is not already present.
#When the cache reached its capacity, it should invalidate the least recently
#used item before inserting a new item.
#Follow up:
#Could you do both operations in O(1) time complexity?
#Example:
#LRUCache cache = new LRUCache( 2 /* capacity */ );
#cache.put(1, 1);
#cache.put(2, 2);
#cache.get(1);       # returns 1
#cache.put(3, 3);    # evicts key 2
#cache.get(2);       # returns -1 (not found)
#cache.put(4, 4);    # evicts key 1
#cache.get(1);       # returns -1 (not found)
#cache.get(3);       # returns 3
#cache.get(4);       # returns 4

#Follow up:
#Could you do both operations in O(1) time complexity?

#According to Wiki, put operation is considered and in each iteration value is
#Ordered dictionary implemetaion
#https://github.com/python/cpython/blob/2.7/Lib/collections.py
#         Delete
#DL       \/
#+------+ |  +-------+    +-------+    +-------+    +------+
#| Head |----| k1,v1 |----| k2,v2 |----| k3,v3 |----| tail |
#|      |----|       |----|       |----|       |----|      | <<<<< Insert
#+------+    +---+---+    +---+---+    +---+---+    +------+
#                |            |            |
#                h1           h2           h3
#
# Map
#+----+ +----+ +----+
#| h1 | | h2 | | h3 |
#+----+ +----+ +----+
#  K1     K2     K3
#


# W/DLL - > (Key, Val) -> head,tail -> insert/delete
#Map -> (Key, DLLNODE)
class Node:
def __init__(self, k, v):
    self.key = k
    self.val = v
    self.prev = None
    self.next = None

class LRUCache:
  def __init__(self, capacity):
      self.capacity = capacity
      self.dic = dict() #store the node
      self.head = Node(0, 0)
      self.tail = Node(0, 0)
      self.head.next = self.tail #
      self.tail.prev = self.head #

  def get(self, key):
      if key in self.dic:
          n = self.dic[key]
          self._remove(n)
          self._add(n)
          return n.val
      return -1

  def set(self, key, value):
      if key in self.dic:
          self._remove(self.dic[key])
      n = Node(key, value)
      self._add(n)
      self.dic[key] = n
      if len(self.dic) > self.capacity:
          n = self.head.next
          self._remove(n)
          del self.dic[n.key]

  def _remove(self, node):
      p = node.prev
      n = node.next
      p.next = n
      n.prev = p

  def _add(self, node):
      p = self.tail.prev
      p.next = node
      self.tail.prev = node
      node.prev = p
      node.next = self.tail

# Whenever element is accessed get/set -> it must be moved to last/first
#Get -> Adjust/Move/Set to Last
#Put -> Check capacity if > : remove first  -> Adjust/Put/set to Last
#ordered dict
#--(Add) (Remove)--
#Add @head and Remove @tail
class LRUCache:
  from collections import OrderedDict
  def __init__(self, capacity):
      self.dic = OrderedDict()
      self.remain = capacity

  def get(self, key):
      if key not in self.dic:
          return -1
      #Adjust position
      v = self.dic.pop(key) #Remove the key from dictionary
      self.dic[key] = v   # set key as the newest one
      return v

  def put(self, key, value):
      #If already exists remove
      if key in self.dic:
          self.dic.pop(key)
      else:
          #update the capacity
          if self.remain > 0:
              self.remain -= 1
          else:  # self.dic is full
              #Remove the first item
              self.dic.popitem(last=False)
      #Adjust the value
      self.dic[key] = value

# W/ DLL
class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.head = LinkedNode(None,'head')
        self.tail = LinkedNode(None,'tail')
        self.head.next = self.tail # tail being most recent
        self.tail.prev = self.head # head being oldest
        self.data = {}

    def deleteNode(self,node):
        assert(node is not self.head and node is not self.tail)
        del self.data[node.key]
        node.prev.next = node.next
        node.next.prev = node.prev
        del node

    def get(self,key):
        if key not in self.data:
            return -1
        node = self.data[key]
        # take the node out
        node.prev.next = node.next
        node.next.prev = node.prev
        # insert into most recent position
        self.insertNew(node)
        return node.value

    def put(self, key, value):
        # remove old value if present
        if key in self.data:
            self.deleteNode(self.data[key])

        # create new node
        newNode = LinkedNode(key,value)
        self.data[key] = newNode

        # if over limit, delete oldest node
        if len(self.data)>self.capacity:
            self.deleteNode(self.head.next)

        self.insertNew(newNode)

    def insertNew(self,newNode):
        # insert new node into last position
        last = self.tail.prev
        last.next = newNode
        self.tail.prev = newNode
        newNode.next = self.tail
        newNode.prev = last


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
