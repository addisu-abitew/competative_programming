class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        presum_count = Counter({0: 1})
        cur_sum = count = 0
        for num in nums:
            # compute prefix sum of the number from the start
            cur_sum += num
            # count the number of complementary sums to cur_sum
            # because the sum of the subarray from those indeces to the current index will
            # = cur_sum - (cur_sum - k) = k
            count += presum_count[cur_sum-k]
            # record the cur_sum
            presum_count[cur_sum] += 1
        return count