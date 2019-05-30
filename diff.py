#Add 24 hour
t = "23:59:59"
t1 = "0:0:0"

# t = "1:0:0"
# t1 = "2:0:0"

import re
past = t.split(':')
current = t1.split(':')

total_sec = 24*60*60

past_sec = t[0] * 24 * 60 * 60 + (t[1] * 60) + (t[2])

def getSec(t) :
  #if(t[0] == '0') : t[0] = 24
  t[0] = int(t[0]) + 24  #Add 24 hours
  h,m,s = int(t[0]), int(t[1]), int(t[2])
  return (h * 60 * 60) + (m * 60) + s


diff = getSec(current) - getSec(past)

hr = diff/(60*60)
hr = hr % 24
rem = diff%(60*60)
m = rem/60
sec = rem % 60

ans = ("%d:%d:%d" % (hr, m, sec ) )

print(ans)
