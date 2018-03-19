#Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
#For example,
#Given:
#s1 = "aabcc",
#s2 = "dbbca",
#When s3 = "aadbbcbcac", return true.
#When s3 = "aadbbbaccc", return false.
#If go from start pick suffix from s1 or s2 if match found in s3
#s1[i:] s3[t:] or s2[j:] s3[t:] t:min(i,j)


class Solution(object):

  def isInterleave(self, s1, s2, s3, memo={}):
    if len(s1) + len(s2) != len(s3):
      return False
    if not s1 and not s2 and not s3:
      return True
    if (s1, s2, s3) in memo:
      return memo[s1, s2, s3]
    memo[s1,s2,s3] =\
    (len(s1) > 0 and len(s3) > 0 and s1[0] == s3[0] and self.isInterleave(s1[1:], s2, s3[1:], memo)) or\
    (len(s2) > 0 and len(s3) > 0 and s2[0] == s3[0] and self.isInterleave(s1, s2[1:], s3[1:], memo))
    return memo[s1, s2, s3]
