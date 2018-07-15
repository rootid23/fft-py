#!/usr/bin/env python

rst = []


# Left/right -> Choose/Not
def printSubList(lst, k=0, last=[]):
  global rst
  tlen = len(lst)
  if (k == tlen):
    #print last
    rst.append(last[:])
    return rst
  # for i in range(k, len(lst)) : #Note ordering is not important so get rid of the for loop
  last.append(lst[k])
  printSubList(lst, k + 1, last)
  last.pop()
  printSubList(lst, k + 1, last)


def main():
  printSubList(['Jane', 'Bob', 'Matt', 'Sara'])
  print rst


if __name__ == "__main__":
  main()
