#!/usr/bin/env python

from timeit import timeit
import unittest

#https://oeis.org/A000045
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
#Fib - O(1.6180)^n -> O(n) -> O(log n)
#F = F(n-1) + F(n-2)

class Fibo(object):

  mem = {}
  mem[0] = 0
  mem[1] = 1

  #Tp-dwn
  def fib(self, n):
    if n in self.mem:
      return self.mem[n]
    if n <= 1:
      f = n
    else :
      f = self.fib(n-1) + self.fib(n-2)
    self.mem[n] = f
    return self.mem[n]

  #Bup - save space + Topo ordered
  #TC - O(n)
  def fibBup(self, n):
    mema = [0,1]
    for k in range(2, n+1):
      mema.append(mema[k-1] + mema[k-2])
    return mema[n]

  #Rec - O(1.6180)^n
  def fibRec(self, n):
    if n <= 1:
      f = n
    else :
      f = self.fibRec(n-1) + self.fibRec(n-2)
    return f



class Test(unittest.TestCase):

  def test_fib_tpdwn(self):
    s = Fibo()
    self.assertEqual(s.fib(0), 0)
    self.assertEqual(s.fib(1), 1)
    self.assertEqual(s.fib(2), 1)
    self.assertEqual(s.fib(3), 2)
    self.assertEqual(s.fib(4), 3)
    self.assertEqual(s.fib(5), 5)
    self.assertEqual(s.fib(6), 8)

  def test_fib_bup(self):
    s = Fibo()
    self.assertEqual(s.fibBup(0), 0)
    self.assertEqual(s.fibBup(1), 1)
    self.assertEqual(s.fibBup(2), 1)
    self.assertEqual(s.fibBup(3), 2)
    self.assertEqual(s.fibBup(4), 3)
    self.assertEqual(s.fibBup(5), 5)
    self.assertEqual(s.fibBup(6), 8)

  def test_fib_rec(self):
    s = Fibo()
    self.assertEqual(s.fibRec(0), 0)
    self.assertEqual(s.fibRec(1), 1)
    self.assertEqual(s.fibRec(2), 1)
    self.assertEqual(s.fibRec(3), 2)
    self.assertEqual(s.fibRec(4), 3)
    self.assertEqual(s.fibRec(5), 5)
    self.assertEqual(s.fibRec(6), 8)



if __name__ == '__main__':
  unittest.main()


# vim: ai ts=2 sts=2 et sw=2 tw=100 fdm=indent fdl=1
