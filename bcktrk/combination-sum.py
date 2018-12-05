#Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
#The same repeated number may be chosen from C unlimited number of times.
#Note:
#    All numbers (including target) will be positive integers.
#    The solution set must not contain duplicate combinations.
#For example, given candidate set [2, 3, 6, 7] and target 7,
#A solution set is:
#[
#  [7],
#  [2, 2, 3]
#]


class Solution(object):

  def combinationSum(self, cands, target):
    """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
    rst = []

    def cSumHelper(k=0, lsum=0, lst=[]):
      #if(lsum > target) : return
      if (lsum == target):
        rst.append(list(lst))
      if (lsum < target):
        for i in range(k, len(cands)):
          #Choose
          if (cands[i] <= target):
            lsum += cands[i]
            #print lsum
            lst.append(cands[i])
          #Xplore
            cSumHelper(i, lsum, lst)
          #Unchoose
            k += 1
            lsum -= lst.pop()

    cSumHelper()
    return rst


class Solution(object):
    def combinationSum(self, candidates, target):
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
                if(target >= cs[i]) :
                    sc += [ cs[i] ]
                    #print(sc)
                    rst += csHelper(cs, sc, target - cs[i], i)
                    sc.pop()
            return rst

        #repeat the elment
        candidates.sort()

        return csHelper(candidates, [] , target)

