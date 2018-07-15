class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


#W/ Sorting
# Very similar with what we do in real life. Whenever you want to start a meeting,
# you go and check if any empty room available (available > 0) and
# if so take one of them ( available -=1 ). Otherwise,
# you need to find a new room someplace else ( numRooms += 1 ).
# After you finish the meeting, the room becomes available again ( available += 1 ).
def minMeetingRooms(self, intervals):
       starts = []
       ends = []
       for i in intervals:
           starts.append(i.start)
           ends.append(i.end)
       starts.sort()
       ends.sort()
       s = e = 0
       numRooms = available = 0
       while s < len(starts):
           if starts[s] < ends[e]:
               if available == 0:
                   numRooms += 1
               else:
                   available -= 1
               s += 1
           else:
               available += 1
               e += 1
       return numRooms

#W/ heap
import heapq

def minMeetingRooms(intvs) :
  if(not intvs) : return 0

  #sorted by the start time
  intvsnew = sorted(intvs, key=lambda item: item.start)
  cnt = 1
  h = []
  heapq.heappush(h ,intvsnew[0].end)
  for i in range(1, len(intvsnew)) :
    if(h[0] <= intvsnew[i].start) : #has meeting finished ?
      heapq.heappop(h)
    heapq.heappush(h, intvsnew[i].end)
    cnt = max(cnt, len(h))
  return cnt


#Given [[15, 20],[0, 30],[5, 10]],
lst = [ Interval(0, 30), Interval(5, 10), Interval(15, 20)]

print ( minMeetingRooms(lst) )

#Meeting Rooms II
#Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the
#minimum number of conference rooms required.
#For example,
#Given [[0, 30],[5, 10],[15, 20]],
#return 2.
