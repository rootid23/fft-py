#Given a set of distinct integers, nums, return all possible subsets (the power set).
#Note: The solution set must not contain duplicate subsets.
#Example:
#Input: nums = [1,2,3]
#Output:
#[
#  [3],
#  [1],
#  [2],
#  [1,2,3],
#  [1,3],
#  [2,3],
#  [1,2],
#  []
#]

#[1,2,3]
#	[] | start = 0
#		[1] | start = 1
#			[1, 2] | start = 2
#				[1, 2, 3] | start = 3
#			[1, 3] | start = 3
#		[2] | start = 2
#			[2, 3] | start = 3
#		[3] | start = 3


class Solution(object):
    def subsets(self, nums):
        #will there be any duplicate?

        #what if I've zero element/ 1 element

        def subsetHelper(nums, choices, k, ws = '\t') :
            print(ws + str(choices) + " | start = " +  str(k))

            rst = []
            rst += [ choices [:] ]
            for idx in range(k, len(nums)) :
                choices += [ nums[idx] ]
                rst += subsetHelper(nums, choices, idx + 1, ws + '\t')
                choices.pop()
            return rst

        choices = []
        return subsetHelper(nums, choices, 0)



class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def subsetsHelper(rest, cur) :
            rst = []
            print(rest , cur)
            if(len(rest) == 0) :
                rst += [ cur[:] ]
                return rst
            cur += [ rest[0] ]
            rst += subsetsHelper(rest[1:], cur)
            cur.pop()
            rst += subsetsHelper(rest[1:], cur)
            return rst
        cur = []
        rst = subsetsHelper(nums, cur)
        return rst


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        #will there be any duplicate?

        #what if I've zero element/ 1 element
        rst = []
        def subsetHelper(nums, choices, k) :
            if(k == len(nums)) :
                rst.append(choices [:])
            elif(k < len(nums)) :
                subsetHelper(nums, choices, k + 1)
                choices += [ nums[k] ]
                subsetHelper(nums, choices, k + 1)
                choices.pop()

        choices = []
        subsetHelper(nums, choices, 0)
        return rst

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        #       [1,2,3]
        #[1] [2,3]
        #[1,2] [3]
        #[1,2,3] []
        lst = []
        def subsetHelper(nums, lst, k, st='\t') :
            #print( st + "k = " + str(k) + "| lst = "  + str(lst))
            rst = []
            if(k > len(nums)) : return rst
            if(k == len(nums)) :
                rst += [ lst [:] ]
                return rst
            rst += subsetHelper(nums, lst, k+1, st+'\t')
            lst += [ nums[k] ]
            rst += subsetHelper(nums, lst, k+1, st+'\t')
            lst.pop()
            return rst



        return subsetHelper(nums, lst, 0)


