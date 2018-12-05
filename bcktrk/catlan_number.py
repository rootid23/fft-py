
#Compute Nth catlan number

#W/ Recurrence rleation
def getNthCatlan(n) :
  rst = 0
  if(n <= 1) :
    return 1
  for i in range(n) :
    rst += getNthCatlan(i) * getNthCatlan(n-1-i)
  return rst


# st = ""
# for i in range(10) :
#   st += "(%d = %d)," % (i, getNthCatlan(i))
# print(st)


#W/ binamial equation
def bino(n , k) :
  if(k == 0 or k == n) : return 1
  return bino(n-1, k-1) + bino(n, k-1)


def getNthCatlanBin(n) :
  rst = 0
  rst = bino(2*n, n)
  rst = rst/(n+1)
  return rst

st = ""
for i in range(10) :
  st += "(%d = %d)," % (i, getNthCatlanBin(i))
print(st)
