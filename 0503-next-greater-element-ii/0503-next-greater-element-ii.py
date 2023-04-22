class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        s = []
        i = 0
        while True:
            # print(s)
            while s and nums[s[-1]] < nums[i]:
                j = s.pop()
                res[j] = nums[i]
            if s and s[0]==i:
                break
            s.append(i)
            i = (i+1)%len(nums)
        while s:
            j = s.pop()
            res[j] = -1
        return res