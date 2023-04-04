class Solution(object):
    def topKFrequent(self, nums, k):
        vals = {}
        for num in nums:
            if num in vals:
                vals[num] += 1
            else:
                vals[num] = 1
        values = []
        for val in vals.values():
            values.append(val)
        values.sort()
        res = []
        for i in values[::-1][:k]:
            for j in vals:
                # print(vals[j], i)
                if vals[j] == i and j not in res:
                    res.append(j)
        return res
                    