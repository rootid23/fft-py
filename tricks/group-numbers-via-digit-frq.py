

#NOTE : in python list are mutable while tuples are note
#So use tuple as the key not the list
lst = [1,3,303,330]

dict = {}
for i in lst :
  tm = sorted(str(i))
  tmp = tuple(tm)
  if( tmp not in dict) :
    dict[ tmp ] = []

  dict [ tmp ] += [ i ]

for key in dict.keys():
  print dict[key]
