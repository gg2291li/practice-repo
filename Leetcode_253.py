class Solution:
    def minMeetingRooms(self, intervals):
        intervals.sort(key = lambda k:k[0])

        
        return