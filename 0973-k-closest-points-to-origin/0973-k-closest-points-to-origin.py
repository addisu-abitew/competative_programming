def findPos(arr, val):
    # print(arr, val)
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        distSquared = arr[mid][0]**2 + arr[mid][1]**2
        # If x is greater, ignore left half
        if distSquared < val:
            low = mid + 1
        # If x is smaller, ignore right half
        elif distSquared > val:
            high = mid - 1
        else: break
    return low
            
# def posFinder(arr, val):
#     return findPos(arr, val, 0, len(arr)-1)
            
class Solution(object):
    def kClosest(self, points, k):
        ordered = []
        for point in points:
            x, y = point
            dist = x**2 + y**2
            # find the correct position
            pos = findPos(ordered, dist)
            # print(pos)
            # insert on the correct position
            ordered.insert(pos, point)
        # print(ordered)
        return ordered[:k]