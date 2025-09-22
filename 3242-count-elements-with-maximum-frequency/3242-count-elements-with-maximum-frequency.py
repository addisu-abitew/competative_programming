class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # count the number of occurence of each number
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
        
        max_count = 0
        res = 0
        for val in freq:
            if freq[val] > max_count:
                max_count = freq[val]
                res = max_count
            elif freq[val] == max_count:
                res += max_count
        return res
