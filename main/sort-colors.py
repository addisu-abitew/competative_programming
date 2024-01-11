class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = Counter(nums)
        i = 0
        for num in range(3):
            for _ in range(count[num]):
                nums[i] = num
                i += 1