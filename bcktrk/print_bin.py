#!/usr/bin/env python

#Base-case
# 1. 1/0 -
# 1. Creating decisons and choosing the decision

## 2 -> print all poosible binaries
def printBinary(num, prefx=""):
  #print("printBinary(%d, %s) " % (num, prefx))
  if (num == 0):
    print prefx
  else:
    printBinary(num - 1, prefx + "0")
    printBinary(num - 1, prefx + "1")


def main():
  print printBinary(2)
  print printBinary(4)


if __name__ == "__main__":
  main()
