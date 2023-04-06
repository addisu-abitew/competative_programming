class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals,key= list[1])
        merged = []
        for interval in intervals:
            if len(merged) == 0 or interval[0] > merged[len(merged)-1][1]:
                merged.append(interval)
            else:
                merged[len(merged)-1][1] = max(merged[len(merged)-1][1], interval[1])
        return merged