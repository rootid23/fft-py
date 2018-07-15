#Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#For example, given n = 3, a solution set is:
#[
#  "((()))",
#  "(()())",
#  "(())()",
#  "()(())",
#  "()()()"
#]

#Backtracking

#T(n) = 2T(n-1)
#Catlan # analysis
#1/(n+1) (2n C n) = 4^n/n(n)^1/2
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        rst = []
        def genHelper(n, lcal="", lt=n, rt=n) :
            #Base case
            #indent(n-lt)
            #print lcal
            if(lt == rt and lt == 0) :
                rst.append(str(lcal))
                return
            # if(lt < rt) : return
            #Choose
            if(lt > 0) :
                lcal += '('
                #Xplore
                genHelper(n, lcal, lt-1, rt)
                lcal = lcal[0:-1]
            if(rt > lt) :
                lcal += ')'
                genHelper(n, lcal, lt, rt-1)
                #Unchoose
                lcal = lcal[0:-1]

        genHelper(n)
        return rst

      #() - lf = 1, rt = 1
      def indent(n) :
          for _ in range(n) :
              print "  ",

#Closure
#CFG grammar : S -> S(S) | empty
#P --> ( P ) | P P | epsilon
#O(4^n/n^1/2)
class Solution(object):

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        #epsilon string
        if(n == 0): return ['']

        rst = []
        for i in range(n) :
            for frnt in self.generateParenthesis(i) :
                for bck in self.generateParenthesis(n-1-i) :
                    rst.append(frnt + '(' + bck + ')')
        return rst

