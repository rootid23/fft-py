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



#[] | start = 0
#	[2] | start = 0
#		[2, 2] | start = 0
#			[2, 2, 2] | start = 0
#			[2, 2, 3] | start = 1
#		[2, 3] | start = 1
#	[3] | start = 1
#		[3, 3] | start = 1
#	[6] | start = 2
#	[7] | start = 3


def combinationSum(self, candidates, target):
        candidates.sort()

        def csHelper(start, candidates, sel, target, ws = '\t') :
            print(ws + str(sel) + " | start = " +  str(start))
            rst = []
            if(start < len(candidates)) :
                if(target == 0) :
                    rst += [ sel [:] ]
                for idx in range(start, len(candidates)) :
                    if(target >= candidates[idx]) :  #Explore only possible elements
                        sel += [ candidates[idx] ]
                        rst += csHelper(idx, candidates, sel, target - candidates[idx], ws + '\t')
                        sel.pop() #Undo the decision
                return rst


                # if(candidates[start] <= target) :
                #     sel += [ candidates[start] ]
                #     #Select element
                #     rst += csHelper(start, candidates, sel, target - candidates[start])
                #     sel.pop()
                #     #discard the lement
                #     rst += csHelper(start+1, candidates, sel, target)


            return rst


        return csHelper(0, candidates, [] , target)


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

