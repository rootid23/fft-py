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
