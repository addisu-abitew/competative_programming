class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        nice = odds = 0
        odd_pos = []
        for right in range(len(nums)):
            if nums[right] % 2 == 1:
                odds += 1
                odd_pos.append(right)
            while odds > k:
                if nums[left] % 2 == 1:
                    odds -= 1
                    odd_pos.pop(0)
                left += 1
            if odds == k:
                nice += odd_pos[0] - left + 1
        return nice