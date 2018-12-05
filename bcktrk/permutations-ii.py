#Given a collection of numbers that might contain duplicates, return all possible unique permutations.
#For example,
#[1,1,2] have the following unique permutations:
#[
#  [1,1,2],
#  [1,2,1],
#  [2,1,1]
#]


class Solution(object):

  def permuteUnique(self, nums):
    """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
    # 1-> (1,1)
    # 1-> (1,1,2)
    rst = []

    def permuteUniqHelper(avail, choosen=[]):
      #print avail
      if (len(avail) == 0):
        rst.append(list(choosen))
      else:
        for i in range(len(avail)):
          if (i + 1 < len(avail) and avail[i + 1] == avail[i]):
            continue
          choosen.append(avail[i])  # Choose
          permuteUniqHelper(avail[0:i] + avail[i + 1:], choosen)  #Xplore
          choosen.pop()  # Unchoose

    nums.sort()
    permuteUniqHelper(nums)
    return rst

class Solution(object):

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 1-> (1,1)
        # 1-> (1,1,2)
        def permuteHelper(rest, curr, tmp='\t') :
            # print( tmp + "A = " + str(rest) + " | S = " +  str(curr))
            rst = []
            if(len(rest) == 0) :
                # print curr
                rst += [ curr[:] ]
                return rst
            for i in range(len(rest)) :
                #Choose
                if(i == 0 or rest[i-1] != rest[i]) :
                    curr += [ rest[i] ]
                    #Pick next
                    rst += permuteHelper( rest[:i] + rest[i+1:], curr, tmp + '\t')
                    #Unchoose
                    #rest += [ rest[i] ]
                    curr.pop()

            return rst

        curr = []
        nums.sort()
        rst = permuteHelper(nums, curr)
        return rst

