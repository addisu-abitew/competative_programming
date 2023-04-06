class Solution(object):
    def merge(self, intervals):
        areSingles = True
        i = 0
        while areSingles and i<len(intervals):
            if intervals[i][0]!=intervals[i][1]:
                areSingles = False
            i += 1
        # print(areSingles and len(intervals)<10)
        if areSingles and len(intervals)<10:
            i = 0
            while i<len(intervals):
                j = i + 1
                while i<len(intervals) and j<len(intervals):
                    if intervals[i][0] == intervals[j][0]:
                        self.mini_merge(intervals, i, j)
                    else:
                        j += 1
                i += 1
        if not areSingles:
            i = 0
            while i<len(intervals):
                j = i + 1
                while j<len(intervals) and i<len(intervals):
                    if intervals[i][0] >= intervals[j][0] and intervals[i][0] <= intervals[j][1] \
                        or intervals[j][0] >= intervals[i][0] and intervals[j][0] <= intervals[i][1] \
                        or intervals[i][1] >= intervals[j][0] and intervals[i][1] <= intervals[j][1] \
                        or intervals[j][1] >= intervals[i][0] and intervals[j][1] <= intervals[i][1]:
                        self.mini_merge(intervals, i, j)
                        j = i + 1
                    else:
                        j += 1
                i += 1
        
        return intervals

    def mini_merge(self,intervals,i1, i2):
        new_interval = []
        if intervals[i1][0] > intervals[i2][0]:
            new_interval.append(intervals[i2][0])
        else:
            new_interval.append(intervals[i1][0])
        if intervals[i1][1] < intervals[i2][1]:
            new_interval.append(intervals[i2][1])
        else:
            new_interval.append(intervals[i1][1])
        
        if i1 > i2:
            intervals.pop(i1)
            intervals[i2] = new_interval
        else:
            intervals.pop(i2)
            intervals[i1] = new_interval
        # print(intervals)