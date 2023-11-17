class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        inWin = Counter()
        winSize = 0
        winSum = maxSum = 0
        for i in range(len(nums)):
            if winSize < k and inWin[nums[i]] == 0:
                inWin[nums[i]] += 1
                winSize += 1
                winSum += nums[i]
            else:
                while winSize >= k or winSize > 0 and inWin[nums[i]] > 0:
                    inWin[nums[i-winSize]] -= 1
                    winSum -= nums[i-winSize]
                    winSize -= 1
                inWin[nums[i]] += 1
                winSize += 1
                winSum += nums[i]
            if winSize == k:
                maxSum = max(maxSum, winSum)
        return maxSum