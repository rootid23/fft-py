#!/usr/bin/env python

a = 0


def my_function(b):
  global a
  a = 3
  print(a)
  print("my_function b4 ", b)

  def inner_function(b):
    print " Inner _function b4 ", b
    b += 3
    print " Inner _function", b

  inner_function(b)
  print("my_function after", b)


my_function(10)

print(a)
