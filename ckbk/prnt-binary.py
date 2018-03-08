#!/usr/bin/env python

def print_bin(n):
  if (n >= 1):
    last = n%2
    print_bin(n/2)
    print last,


if __name__ == '__main__':
  print_bin(4)
  print ""
  print_bin(6)
  print ""

# vim: ai ts=2 sts=2 et sw=2 tw=100 fdm=indent fdl=1
