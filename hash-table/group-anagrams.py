import collections

class Solution(object):
    def groupAnagrams(self, strs):
        #Group based on
        #1. Iterate  - O(n)
        #2. Sort - l * O(n lg n)
        #3. Scan + Collect - O(n)

        a_map = collections.defaultdict(list)
        for str_ in strs :
            a_map["".join(sorted(str_))] += [ str_ ]

        rst = []
        for k in a_map.keys() :
            rst += [ a_map[k] ]
        return rst



#Group Anagrams
#Given an array of strings, group anagrams together.
#Example:
#Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
#Output:
#[
#  ["ate","eat","tea"],
#  ["nat","tan"],
#  ["bat"]
#]
#Note:
#    All inputs will be in lowercase.
#    The order of your output does not matter.
