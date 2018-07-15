#!/usr/bin/env python


# Base case -
# Recusrive case
# DP - What are the subproblms
def printDecimal(num, prefx=""):
  #print("printDecimal(%d, %s) " % (num, prefx))
  if (num == 0):
    print prefx
  else:
    #Generate choices 0,10
    for i in range(0, 10):
      printDecimal(num - 1, prefx + str(i))
      #Choose the choices


def main():
  print printDecimal(2)
  # print printDecimal(0)


if __name__ == "__main__":
  main()
