
#W/ hashmap + sorting w/ heap
import collections
import heapq
class Solution(object):
    def frequencySort(self, s):

        cntr = collections.Counter(s)

        rst = []
        for k,v in cntr.items() :
            heapq.heappush(rst, (-v, k*v) )

        op = ""
        while rst :
            op += heapq.heappop(rst)[1]
        return op

#W/ hashmap sorting
from collections import defaultdict

class Solution(object):
    def frequencySort(self, s):
        counts = defaultdict(int)

        for c in s:
            counts[c] += 1

        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

        result = ""
        for c, times in sorted_counts:
            result += c * times
        return result

#W/ most_common API
class Solution(object):
    def frequencySort(self, s):
        import collections
        if not s:
            return ""
        count_s = collections.Counter(s)
        counter = count_s.most_common()
        rs = ''
        for i in counter:
            rs += i[0] * i[1]
        return rs

#Lambda alternative - > operator.itemgetter(1)
class Solution(object):
    def frequencySort(self, s):
        import operator
        if not s:
            return ""
        counter = {}; rs = ''
        for i in s:
            counter[i] = 1 if i not in counter else counter[i]+1
        sorted_counter = sorted(counter.items(), key=operator.itemgetter(1))
        sorted_counter.reverse()
        for i in sorted_counter:
            rs += i[0] * i[1]
        return rs

#instead of lambda
counter[i] = counter.get(i,0) + 1
def takeSecond(elem):
  return elem[1]
sorted_counter = sorted(counter.items(), key=takeSecond, reverse = True));


#Sort Characters By Frequency
#Given a string, sort it in decreasing order based on the frequency of characters.
#Example 1:
#Input:
#"tree"
#Output:
#"eert"
#Explanation:
#'e' appears twice while 'r' and 't' both appear once.
#So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
#Example 2:
#Input:
#"cccaaa"
#Output:
#"cccaaa"
#Explanation:
#Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
#Note that "cacaca" is incorrect, as the same characters must be together.
#Example 3:
#Input:
#"Aabb"
#Output:
#"bbAa"
#Explanation:
#"bbaA" is also a valid answer, but "Aabb" is incorrect.
#Note that 'A' and 'a' are treated as two different characters.
