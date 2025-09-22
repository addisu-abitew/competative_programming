class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # count the number of occurence of each number
        freq = {}
        max_count, res = 0, 0
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
            if freq[num] > max_count:
                max_count = freq[num]
                res = max_count
            elif freq[num] == max_count:
                res += max_count
        
        return res
