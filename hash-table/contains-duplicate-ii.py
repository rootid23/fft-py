#w/ sliding window
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        #Ida
        #sliding window
        import collections
        dq = collections.deque([])
        a_set = set()
        no_ele_to_track = k + 1
        for i,v in enumerate(nums) :
            #if have at most k elements
            if(no_ele_to_track == len(dq)) :
                a_set.remove(dq.popleft())
            dq += [v]
            if(v in a_set) : return True
            a_set.add(v)
        return False


#Contains Duplicate II
#Given an array of integers and an integer k, find out whether there are two distinct indices i and
#j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
#Example 1:
#Input: nums = [1,2,3,1], k = 3
#Output: true
#Example 2:
#Input: nums = [1,0,1,1], k = 1
#Output: true
#Example 3:
#Input: nums = [1,2,3,1,2,3], k = 2
#Output: false
