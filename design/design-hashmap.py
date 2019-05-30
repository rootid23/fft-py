
class MyHashMap(object):

    #1. What kind of keys?
    #2. put - expected complexity for each operation
    #3. put/get/delete - O(1)
    #4. # of keys?
    #key -> index
    def __init__(self):
        """
        Initialize your data structure here.
        """
        #collision ->
        self.sz = 1000001
        self.mp = [None]  * self.sz

    def __getIdxKey(self, key) :
        return hash(key) % self.sz

    def __find(self, idx, key) :
        lst = self.mp[idx]
        for item in lst :
            if(item[0] == key) :
                return item
        return None

    def __remove(self, idx, key) :

        lst = self.mp[idx]
        if(not lst) : return None
        idx_to_rmv = -1
        for item in lst :
            if(item[0] == key) :
                idx_to_rmv += 1
                break
            idx_to_rmv += 1 #-1, -> 0 ()

        if(idx_to_rmv < len(lst)) :
            tmplst = lst[:idx_to_rmv] + lst[idx_to_rmv+1:]
            self.mp[idx] = []
            self.mp[idx] = tmplst[:]
        return None


    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        idx = self.__getIdxKey(key)
        if(not self.mp[idx]) :
            self.mp[idx] = list()
        else :
            idx = self.__getIdxKey(key)
            rst = self.__find(idx, key)
            if(rst) :
                rst[1] = value
                return
        self.mp[idx] += [ [key, value] ]
        #print(self.mp)


    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        idx = self.__getIdxKey(key)
        if(not self.mp[idx]) : return -1
        rst = self.__find(idx, key)
        if(rst) : return rst[1]
        return -1




    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        idx = self.__getIdxKey(key)
        if(not self.mp[idx]) : return
        self.__remove(idx, key)




# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


#Design a HashMap without using any built-in hash table libraries.
#To be specific, your design should include these functions:
#put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the
#HashMap, update the value.
#get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no
#mapping for the key.
#remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.
#Example:
#MyHashMap hashMap = new MyHashMap();
#hashMap.put(1, 1);
#hashMap.put(2, 2);
#hashMap.get(1);            // returns 1
#hashMap.get(3);            // returns -1 (not found)
#hashMap.put(2, 1);          // update the existing value
#hashMap.get(2);            // returns 1
#hashMap.remove(2);          // remove the mapping for 2
#hashMap.get(2);            // returns -1 (not found)
#Note:
#All keys and values will be in the range of [0, 1000000].
#The number of operations will be in the range of [1, 10000].
#Please do not use the built-in HashMap library.
