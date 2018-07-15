#!/usr/bin/env python


def permute_string(s, rest=""):
  if (len(s) == 0):
    print rest
  else:
    #Chose/explore/unchoose
    for i in range(len(s)):
      nxt = rest + s[i]
      permute_string(s[0:i] + s[i + 1:], nxt)


def main():
  """TODO: Docstring for main.
  :returns: TODO

  """
  permute_string("abcd")


if __name__ == "__main__":
  main()
