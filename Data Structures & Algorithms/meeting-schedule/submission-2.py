"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        ## first sort the starts by ascending start times
        for j in range(len(intervals)):
            for i in range(len(intervals)-1):
                temp = intervals[i]
                if intervals[i].start > intervals[i+1].start:
                    intervals[i] = intervals[i+1]
                    intervals[i+1] = temp
        ## now compare end to start, if end is greater than start, return false
        for i in range(len(intervals)-1):
            if intervals[i].end > intervals[i+1].start:
                return False
        return True
        