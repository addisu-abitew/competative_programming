class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        ones = [0]
        for num in nums:
            ones.append(ones[-1]+num)
        max_sum = -1
        max_idx = []
        for i in range(len(nums)+1):
            cur_sum = (i-ones[i])+(ones[-1]-ones[i]-1)
            if max_sum == cur_sum:
                max_idx.append(i)
            elif cur_sum > max_sum:
                max_idx = [i]
                max_sum = cur_sum
        return max_idx