
#Meeting Rooms
#Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine
#if a person could attend all meetings.
#For example,
#Given [[0, 30],[5, 10],[15, 20]],
#return false.


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

#Sorting w/ start time
#compare the next start time with max end time
def canAttendMeetings(intervals) :

  if(not intervals) : return True

  srtedInt = sorted(intervals, key=lambda item: item.start)
  m = len(srtedInt)
  lastEndTime = intervals[0].end
  for i in range(1, m) :
    if(srtedInt[i].start < lastEndTime) :
        return False
    lastEndTime = max(srtedInt[i].end, lastEndTime)
  return True


#Sorting w/ start time
#compare adjacent intervals
def canAttendMeetings(intervals) :

  if(not intervals) : return True

  srtedInt = sorted(intervals, key=lambda item: item.start)
  m = len(srtedInt)
  lastEndTime = intervals[0].end
  for i in range(1, m) :
    if(srtedInt[i].start < srtedInt[i-1].end) :
        return False
  return True

