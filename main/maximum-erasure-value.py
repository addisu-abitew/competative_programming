class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        presum = [0]
        for num in nums:
            presum.append(presum[-1] + num)
        print(presum)
        
        max_score = 0
        left = 0
        uniques = {}
        for right in range(n):
            num = nums[right]
            if num in uniques and uniques[num] > left:
                left = uniques[num]
            uniques[num] = right + 1
            max_score = max(max_score, presum[right+1]-presum[left])
        return max_score