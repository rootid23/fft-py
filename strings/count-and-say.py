# Count and Say
#The count-and-say sequence is the sequence of integers beginning as follows:
#1, 11, 21, 1211, 111221, ...
#1 is read off as "one 1" or 11.
#11 is read off as "two 1s" or 21.
#21 is read off as "one 2, then one 1" or 1211.
#Given an integer n, generate the nth sequence.
#Note: The sequence of integers will be represented as a string.


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        #freq, number
        #1 , 11, 21, 1211
        current = '1#'
        next_val =''
        frq = 1
        for _ in range(1, n):
            for i in range(1, len(current)):
              if(current[i-1] == current[i]) :
                frq += 1
              else :
                next_val += str(frq) + current[i-1]
                frq = 1
            current = next_val
            next_val = ""
            current += '#'

      return current[:-1]

