class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result = [0]*len(nums)
        pi, ni = 0, 1
        for num in nums:
            if num > 0:
                result[pi] = num
                pi += 2
            else:
                result[ni] = num
                ni += 2
        return result