class Solution(object):
    def minSetSize(self, arr):
        n = len(arr)
        vals = {}
        for i in range(n):
            if arr[i] in vals:
                vals[arr[i]] += 1
            else:
                vals[arr[i]] = 1
        s = 0
        r = 0
        values = []
        for val in vals.values():
            values.append(val)
        values.sort()
        for j in values[::-1]:
            print(j)
            s += j
            r += 1
            if s >= n//2:
                return r