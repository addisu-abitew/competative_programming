class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solutionList = []
        n = len(nums)
        i = 0
        while i<n-2:
            k = n-1
            j = i + 1
            while j<n-1:
                while k>j and nums[i] + nums[j] + nums[k] >= 0:
                    if nums[i] + nums[j] + nums[k] == 0:
                        solutionList.append([nums[i], nums[j], nums[k]])
                    while k>j and nums[k]==nums[k-1]:
                        k -= 1
                    k -= 1
                while j<n-1 and nums[j]==nums[j+1]:
                    j += 1
                j += 1
            while i<n-2 and nums[i]==nums[i+1]:
                i += 1
            i += 1
        return solutionList