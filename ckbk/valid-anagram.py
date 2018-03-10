#!/usr/bin/env python

#Given two strings s and t, write a function to determine if t is an anagram of s.
#For example,
#s = "anagram", t = "nagaram", return true.
#s = "rat", t = "car", return false.
#Note:
#You may assume the string contains only lowercase alphabets.
#Follow up:
#What if the inputs contain unicode characters? How would you adapt your solution to such case?


# W/ clean dict
def isAnagram1(self, s, t):
  dic1, dic2 = {}, {}
  for item in s:
    dic1[item] = dic1.get(item, 0) + 1
  for item in t:
    dic2[item] = dic2.get(item, 0) + 1
  return dic1 == dic2


#W/ Array
def isAnagram2(self, s, t):
  dic1, dic2 = [0] * 26, [0] * 26
  for item in s:
    dic1[ord(item) - ord('a')] += 1
  for item in t:
    dic2[ord(item) - ord('a')] += 1
  return dic1 == dic2


#W/ sorting
def isAnagram3(self, s, t):
  return sorted(s) == sorted(t)


# W/ dict
class Solution(object):

  def isAnagram(self, s, t):
    if (len(s) == len(t)):
      tmap = {}
      for i in range(len(s)):
        if (s[i] in tmap):
          tmap[s[i]] += 1
        else:
          tmap[s[i]] = 1
        if (t[i] in tmap):
          tmap[t[i]] -= 1
        else:
          tmap[t[i]] = -1
      for _, v in tmap.iteritems():
        if (v != 0):
          return False
      return True
    return False


# vim: ai ts=2 sts=2 et sw=2 tw=100 fdm=indent fdl=1
