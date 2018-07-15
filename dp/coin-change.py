#NOTE - Use of i and k
#Cases for i and k
#i  - updates and increment during each level
#k - Never updates always start from 0 : so we get repeated and permuted order output


#Choose the coin with repeat
class Solution:
    def coinChange(self, coins, amount):
        #min count change
        MAX = float('inf')
        dp = [0] + [MAX] * amount

        coins.sort(reverse=True)

        #iterate over coins
        for i in coins:
            for j in range(i, amount+1) :
                dp[j] = min(dp[j], dp[j-i] + 1)
            # print(dp)
        return -1 if dp[amount] > amount else dp[amount]

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        m = len(coins)
        opt = [0] * (amount+1)
        for i in range(1, amount+1) :
            opt[i] = amount+1
        for i in range(0, m) :
            for j in range(i, amount+1) :
                if(j - coins[i] >= 0) : #check if OPT(n-1) falls within the range
                    opt[j] = min(opt[j], opt[j - coins[i]]+1)  #choose between OPT(n), OPT(n-1)
                    #if j is not part of OPT then  j - coins[i]
        return -1 if opt[amount] > amount else opt[amount]

#To pick coin W/O repeat = pick coin w/ repeat + check the last candidate

#Pick coin w/ repeat
N = 4
S = [1,2,3]

def makeChange(s, n, k, lst=[], rst=[]) :

  if(n == 0) :
    rst += [ list(lst) ]
  elif(k < len(s) and n >= s[k]) :
    for i in range(k, len(s)):
      lst += [ s[i] ]

      #When order doesn't matter
      #NOTE : i increment - not start To avoid duplicates (2,3) and (3,2)
      makeChange(s, n-s[i], i, lst, rst)

      #k - when order matters
      #[1,3] and [3,1] are different
      # makeChange(s, n-s[i], k, lst, rst)
      lst.pop()


#Pick coin w/o repeat
def makeChange(s, n, k, lst=[], rst=[]) :

  if(n == 0) :
    rst += [ list(lst) ]
  elif(k < len(s) and n >= s[k]) :
    for i in range(k, len(s)):
      #To avoid duplicate scan the configuration
      if(len(lst) >= 1 and lst[-1] == s[i]) :
        pass
      else :
        lst += [ s[i] ]

        #When order doesn't matter
        #NOTE : i increment - not start To avoid duplicates (2,3) and (3,2)
        makeChange(s, n-s[i], i, lst, rst)

        #k - when order matters
        #[1,3] and [3,1] are different
        # makeChange(s, n-s[i], k, lst, rst)

        lst.pop()



#pick coin w/ repeat
lst = []
rst = []
makeChange(S, N, 0, lst, rst)

print(len(rst))
print (rst)
