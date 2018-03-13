#!/usr/bin/env python


#Write a program that outputs the string representation of numbers from 1 to n.
#But for multiples of three it should output “Fizz” instead of the number and for the multiples of
#five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
#Example:
#n = 15,
#Return:
#[
#    "1",
#    "2",
#    "Fizz",
#    "4",
#    "Buzz",
#    "Fizz",
#    "7",
#    "8",
#    "Fizz",
#    "Buzz",
#    "11",
#    "Fizz",
#    "13",
#    "14",
#    "FizzBuzz"
#]
def fizzBuzz(self, n):
  return [
      'Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i)
      for i in range(1, n + 1)
  ]


def fizzBuzz(self, n):
  return [
      str(i) * (i % 3 != 0 and i % 5 != 0) + "Fizz" * (i % 3 == 0) + "Buzz" *
      (i % 5 == 0) for i in range(1, n + 1)
  ]


class Solution(object):

  def fizzBuzz(self, n):
    lst = []
    for i in range(1, n + 1):
      if (i % 3 == 0 and i % 5 == 0):
        lst.append("FizzBuzz")
      elif (i % 3 == 0):
        lst.append("Fizz")
      elif (i % 5 == 0):
        lst.append("Buzz")
      else:
        lst.append(str(i))
    return lst


# vim: ai ts=2 sts=2 et sw=2 tw=100 fdm=indent fdl=1
