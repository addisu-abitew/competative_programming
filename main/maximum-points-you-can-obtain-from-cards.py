class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        score = 0
        left, right = 0, n-1
        left_sum, right_sum = sum(cardPoints[:k]), sum(cardPoints[n-k:n])
        for i in range(k):
            # print(left_sum, right_sum)
            if left_sum > right_sum:
                score += cardPoints[left]
                left_sum -= cardPoints[left]
                right_sum -= cardPoints[right-k+i+1]
                left += 1
            else:
                score +=  cardPoints[right]
                right_sum -= cardPoints[right]
                left_sum -= cardPoints[k-i-1+left]
                right -= 1
        return score