class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = []
		# Maximum rooms needed (m)
        m = 0
		# Sort to get the increasing start timings
        intervals.sort()
        for x,y in intervals:
            if len(rooms):
				# Check if the start time of current meeting is greater or equal to the end time of the ongoing meeting in one of the acquired rooms (with least time remaining to end).
                if rooms[0] <= x:
                    heapq.heappop(rooms)
			# Push the current meeting's end time in min heap
            heapq.heappush(rooms,y)
			# Check the maximum rooms acquired
            m = max(m, len(rooms))
        return m