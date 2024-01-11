class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        wsum=0
        l=0
        ans=2**31
        for r in range(n):
            wsum+=nums[r]
            while wsum>=target:
                wsum-=nums[l]
                ans=min(ans, r-l+1)
                l+=1
        if ans==2**31:
            return 0
        else:
            return ans