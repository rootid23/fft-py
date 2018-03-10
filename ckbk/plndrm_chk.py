#!/usr/bin/env python

# Determine string is palindorme or not

import unittest


class Solution(object):

  def is_palindrome(self, s):
    sz = len(s)
    if sz == 0 or sz == 1:
      return True
    return self.is_palindrome(s[1:-1]) and s[0] == s[-1]


class Test(unittest.TestCase):

  def test_str_pal(self):
    s = Solution()
    self.assertEqual(s.is_palindrome(""), True)
    self.assertEqual(s.is_palindrome("aaa"), True)
    self.assertEqual(s.is_palindrome("aa"), True)
    self.assertEqual(s.is_palindrome("ab"), False)
    self.assertEqual(s.is_palindrome("abc"), False)


if __name__ == '__main__':
  unittest.main()

# vim: ai ts=2 sts=2 et sw=2 tw=100 fdm=syntax
