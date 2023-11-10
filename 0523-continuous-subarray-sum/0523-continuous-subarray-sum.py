class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) <= 1: return False
        rems = {0:-1}
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            rem = cur_sum%k
            if rem in rems and i-rems[rem]>1:
                return True
            if rem not in rems:
                rems[rem] = i
        return False