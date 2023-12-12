class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evenSum = 0
        for num in nums:
            if num % 2 == 0:
                evenSum += num
        answer = []
        for q in  queries:
            val, i = q
            if nums[i] % 2 == 0:
                if val % 2 == 0:
                    evenSum += val
                else:
                    evenSum -= nums[i]
            elif val % 2 == 1:
                evenSum += val+nums[i]
            nums[i] += val
            answer.append(evenSum)
        return answer