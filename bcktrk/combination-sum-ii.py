#Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
#Each number in candidates may only be used once in the combination.
#Note:
#    All numbers (including target) will be positive integers.
#    The solution set must not contain duplicate combinations.
#Example 1:
#Input: candidates = [10,1,2,7,6,1,5], target = 8,
#A solution set is:
#[
#  [1, 7],
#  [1, 2, 5],
#  [2, 6],
#  [1, 1, 6]
#]
#Example 2:
#Input: candidates = [2,5,2,1,2], target = 5,
#A solution set is:
#[
#  [1,2,2],
#  [5]
#]

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def csHelper(cs, sc, target, last_decision =0) :
            rst = []
            if(sc and target == 0) :
                #print(sc)
                rst += [ sc[:] ]
            for i in range(last_decision, len(cs)) :
                #if(i > last_decision and cs[i-1] == cs[i]) : continue #skip duplicate elements
                if(i <= last_decision or cs[i-1] != cs[i] and target >= cs[i]) :
                    sc += [ cs[i] ]
                    #print(sc)
                    rst += csHelper(cs, sc, target - cs[i], i+1)
                    sc.pop()
            return rst
        #repeat the elment
        candidates.sort()
        return csHelper(candidates, [] , target)
