class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # record the minimum sum from the root to the current item
        sums = {}
        min_sum = None
        for i in range(len(triangle)):
            for j in range(len(triangle[i])):
                if i == 0:
                    sums[(i, j)] = triangle[i][j]
                else:
                    sums[(i, j)] = None
                    if j > 0:
                        cur_sum = sums[(i-1, j-1)] + triangle[i][j]
                        if sums[(i, j)] == None or sums[(i, j)] > cur_sum:
                             sums[(i, j)] = cur_sum
                    if j < len(triangle[i]) - 1:
                        cur_sum = sums[(i-1, j)] + triangle[i][j]
                        if sums[(i, j)] == None or sums[(i, j)] > cur_sum:
                             sums[(i, j)] = cur_sum
                
                if i == len(triangle) - 1:
                    cur_min = sums[(i, j)]
                    if min_sum == None or min_sum > cur_min:
                        min_sum = cur_min
        return min_sum
