class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mod_count = Counter({0: 1})
        mod = subarrays = 0
        for num in nums:
            mod = (mod + num) % k
            subarrays += mod_count[mod]
            mod_count[mod] += 1
        return subarrays