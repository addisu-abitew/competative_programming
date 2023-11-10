class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        min_sum = r
        while l <= r:
            mid = l + (r-l)//2
            cur_sum = 0
            sub_arr = 0
            for n in nums:
                cur_sum += n
                if cur_sum > mid:
                    sub_arr += 1
                    cur_sum = n
                
            if sub_arr+1 <= k:
                r = mid-1
                min_sum = mid
            else:
                l = mid + 1
        return min_sum