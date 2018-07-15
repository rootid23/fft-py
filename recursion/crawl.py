#!/usr/bin/env python

import sys
import os

def crawl(user_dir, tab=' ') :

    print("%s%s" %(tab, user_dir.split('/')[-2] ))

    if(os.path.isfile(user_dir)):
      pass
    elif(os.path.isdir(user_dir)):
      root, dirs, files = os.walk(user_dir).next()
      #for next_file  in files :
      #  print("%s%s" %(tab, next_file))
      for next_dir in files + dirs :
        crawl(root + next_dir + '/'  , tab + '  ')

user_dir = sys.argv[1]
abs_dir = os.path.abspath(user_dir)
crawl(user_dir)
