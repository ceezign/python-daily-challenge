# Good morning! Here's your coding interview problem for today.
# This problem was asked by Snapchat.
# Given an array of time intervals (start, end) for classroom lectures
# (possibly overlapping), find the minimum number of rooms required.
# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
#
# Approach A

def  min_rooms(intervals):
    if not intervals:
        return 0

    starts = sorted(s for s, _ in intervals)
    ends = sorted(e for _, e in intervals)

    i = j = 0              # pointer into starts and ends
    rooms = 0
    max_rooms = 0

    while i < len(starts):
        if starts[i] < ends[j]:
            # a new lecture starts before the earliest current one ends -> need a room
            rooms += 1
            max_rooms = max(max_rooms, rooms)
            i += 1
        else:
            # earliest lecture ended -> free a room
            rooms -= 1
            j += 1

    return max_rooms

print(min_rooms([(30, 75), (0, 50), (60, 150)]))
# Edge cases
print(min_rooms([]))
print(min_rooms([(10, 20)] ))
print(min_rooms([(10, 20), (20, 30)] ))
print(min_rooms([(0, 10), (5, 15), (10, 20)] ))


# Approach B
import heapq

def min_room_heap(intervals):
    if not intervals:
        return 0

    intervals = sorted(intervals, key=lambda  x: x[0])   # sort by start
    heap = []                                            # stores end times of ongoing lectures
    max_rooms = 0

    for s, e in intervals:
        while heap and heap[0] <= s:
            heapq.heappop(heap)       # a room freed up
        heapq.heappush(heap, e)       # take a room (new or reused)
        max_rooms = max(max_rooms, len(heap))

    return  max_rooms

print(min_room_heap([(30, 75), (0, 50), (60, 150)]))

