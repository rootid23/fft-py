#Search for a Range
#Given an array of integers sorted in ascending order, find the starting and
#ending position of a given target value.
#Your algorithm's runtime complexity must be in the order of O(log n).
#If the target is not found in the array, return [-1, -1].
#For example,
#Given [5, 7, 7, 8, 8, 10] and target value 8,
#return [3, 4].

#Template 3
#Initial Condition: left = 0, right = length-1
#Invariant: left + 1 < right
#Termination: left + 1 == right
#Searching Left: right = mid
#Searching Right: left = mid

#Iterative - look for 2 solution space
class Solution(object):

    def searchRange(self, nums, target):

        start=0
        end = len(nums)-1
        while start <= end:
            mid = (start + end)/2
            if nums[mid] == target:
                l = r = mid
                while l >= 0 and nums[l] == nums[mid]:
                    l -= 1
                while r < len(nums) and nums[r] == nums[mid]:
                    r += 1
                return [l+1,r-1]
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return [-1,-1]

#2 binary searches w/ 2 values target, target+1
def searchRange(self, nums, target):
    def search(n):
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) / 2
            if nums[mid] >= n:
                hi = mid #mid is included
            else:
                lo = mid + 1 #mid not included
        return lo
    lo = search(target)
    return [lo, search(target+1)-1] if target in nums[lo:lo+1] else [-1, -1]

#2 binary searches
def searchRange(self, nums, target):
    def search(lo, hi):
        if nums[lo] == target == nums[hi]:
            return [lo, hi]
        if nums[lo] <= target <= nums[hi]:
            mid = (lo + hi) / 2
            l, r = search(lo, mid), search(mid+1, hi)
            return max(l, r) if -1 in l+r else [l[0], r[1]]
        return [-1, -1]
    return search(0, len(nums)-1)


#Using bisect
#1.bisect_left
def searchRange(self, nums, target):
    lo = bisect.bisect_left(nums, target)
    return [lo, bisect.bisect(nums, target)-1] if target in nums[lo:lo+1] else [-1, -1]

#https://leetcode.com/problems/search-for-a-range/discuss/14707/9-11-lines-O(log-n)
