class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        arr = [[1], [1, 1]]
        for _ in range(numRows - 2):
            last_arr = arr[-1]
            cur_arr = [1]
            for i in range(len(last_arr) - 1):
                cur_arr.append(last_arr[i] + last_arr[i+1])
            cur_arr.append(1)
            arr.append(cur_arr)
        return arr