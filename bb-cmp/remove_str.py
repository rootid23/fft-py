#!/usr/bin/env python

#Input : aabbbaccddddc
#Output :ccdc

#1. scan string and and store in auxliarry string
#2. compare last charc and if equal increase match_count >= 3
#3. return auxillary string


def removeAdjacentChars(s) :
  m = len(s)
  if(m < 3) : return s
  tmp = ""

  #1. scan string and and store in auxliarry string
  match_cnt = 0
  for c in s:
    if(len(tmp) == 0 or tmp[-1] != c) :
      tmp += c
      match_cnt = 0
    elif(tmp[-1] == c and match_cnt < 2):
      match_cnt += 2
      tmp += c
      print (tmp , match_cnt)
  #print(tmp)
  return tmp


def remove_triplicate(string):
    res = ""
    i = 0
    while i < len(string):
        if i < len(string) - 2 and string[i]*3 == string[i:i+3]:
            i += 3
        else:
            res += string[i]
            i += 1

    if len(res) == len(string):
        return res
    else:
        return remove_triplicate(res)

if __name__ == '__main__':
  print('Running Test cses.')
  assert remove_triplicate("aabbbaccddddc") == "ccdc"
  assert removeAdjacentChars("aabbbaccddddc") == "ccdc"
  print('Done.')
