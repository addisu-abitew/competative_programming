class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(i, j):
            li, ri = i, j
            while li < ri:
                nums[li], nums[ri] = nums[ri], nums[li]
                li += 1
                ri -= 1
                
        n = len(nums)
        r = k%n
        # print(r)
        reverse(0, n-r-1)
        reverse(n-r, n-1)
        reverse(0, n-1)